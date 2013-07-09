# -*- coding: utf-8 -*-
"""
    shopify_trois.engines.http.json

    Shopify-Trois JSON Engine

    :copyright: (c) 2013 by Martin Samson
    :license: MIT, see LICENSE for more details.
"""
import requests
import json

from shopify_trois.collection import Collection
from shopify_trois.engines.http.oauth_engine import OAuthEngine
from shopify_trois.engines.http.request import Request
from shopify_trois.exceptions import ShopifyException, InvalidRequestException


class Json(OAuthEngine):
    """The Json engine implements an http transport using JSON with OAuth
    authentication.

    :param shop_name: The name of the shopify store.
    :param credentials: :class:`~shopify_trois.credential.Credential`
    :param ignore_supported: When set to True, the engine will ignore
                                the ``supported`` property of the models.
    :param ignore_model_properties: When set to True, the engine will
                                    ignore the ``properties`` property of
                                    models when persisting them.
    """

    extension = 'json'
    mime = 'application/json; charset=utf-8'

    def __init__(self, shop_name, credentials, ignore_supported=False,
                 ignore_model_properties=False):

        super().__init__(shop_name=shop_name, credentials=credentials)

        #: When set to True, ignore checking for supported actions on models.
        self.ignore_supported = ignore_supported
        self.ignore_model_properties = ignore_model_properties

    def count(self, model, **params):
        """Return the count of a model, filtered by parameters"""

        self._can_request("count", model)

        req = Request(model)
        req.resource += "/count"
        req.params = params

        res = self._get(req)
        if res.status_code == requests.codes.ok:
            data = res.json()
            return data["count"]

        raise ShopifyException(res)

    def custom_post(self, instance, action, data=None):
        """Executes a custom post method on an instance.
        :param instance: The model instance being modified.
        :param action: The action to be executed.
        """

        self._can_request(action, instance)

        req = Request(instance)
        req.resource += action
        req.data = data

        res = self._post(req)
        if res.status_code == requests.codes.ok:
            return res.json()

        raise ShopifyException(res)

    def add(self, instance, auto_update=True):
        """Add the model instance to the store.

        :param instance: The model instance being added.
        :param auto_update: Auto-update the instance with the values from
                            Shopify. When set to false, the raw JSON object
                            will be returned.
        """

        self._can_request("create", instance)

        req = Request(instance)

        enclosure = instance.enclosure or instance.to_underscore_name()

        if self.ignore_model_properties:
            data = instance.to_dict()
        else:
            data = dict([
                (k, v) for k, v in instance.to_dict().items()
                if k in instance.properties
            ])

        req.data = json.dumps({enclosure: data})

        res = self._post(req)

        if res.status_code == requests.codes.created:
            if auto_update:
                instance.update(
                    res.json(),
                    ignore_properties=self.ignore_model_properties
                )
                return
            else:
                return res.json()

        raise ShopifyException(res)

    def delete(self, instance):
        """Delete a model instance.

        An InvalidRequestException will be raised if the instance does not yet
        exists.

        :param instance: The model instance to remove.
        """

        self._can_request("delete", instance)

        if not instance._meta__.exists:
            msg = "The supplied instance does not yet exists."
            raise InvalidRequestException(msg)

        req = Request(instance)
        res = self._delete(req)

        if res.status_code == requests.codes.ok:
            return True

        raise ShopifyException(res)

    def update(self, instance, auto_update=True, whitelist=None):
        """Update a model instance.

        An InvalidRequestException will be raised if the instance has not been
        marked as existing.

        :param instance: The model instance being updated.
        :param auto_update: Auto-update the instance with the values from
                            Shopify. When set to False, the raw JSON object
                            will be returned.
        :param whitelist: A list of attributes to be updated. If set to None,
                          all modified attributes will be updated.
        """

        self._can_request("update", instance)

        if not instance._meta__.exists:
            msg = "The supplied instance does not yet exists."
            raise InvalidRequestException(msg)

        enclosure = instance.enclosure or instance.to_underscore_name()

        if self.ignore_model_properties:
            data = instance.to_dict()
        else:
            data = dict([
                (k, v) for k, v in instance.to_dict().items()
                if k in instance.properties
            ])

        req = Request(instance)
        req.data = json.dumps({enclosure: data})

        res = self._put(req)

        if res.status_code == requests.codes.ok:
            if auto_update:
                instance.update(
                    res.json(),
                    ignore_properties=self.ignore_model_properties
                )
                return
            else:
                return res.json()

        raise ShopifyException(res)

    def fetch(self, model, primary_key=None, auto_instance=True, **params):
        """Get a specific model instance by primary key.

        :param Model: The class being queried.
        :param primary_key: The primary key value of the instance.
        :param auto_instance: Automatically create an instance instead of
                              returning a json object.
        :param params: Query parameters.
        """

        self._can_request("view", model)

        req = Request(model)
        req.params = params

        # Shop is the sole resource not following the same naming
        # convention for its resource url.
        if not model.__name__.lower() == "shop":
            req.resource += "/{primary_key}".format(primary_key=primary_key)

        res = self._get(req)

        if res.status_code == requests.codes.ok:
            data = res.json()
            if auto_instance:
                enclosure = model.enclosure or model.to_underscore_name()
                return model(**data[enclosure])
            else:
                return data

        raise ShopifyException(res)

    def index(self, model, auto_instance=True, **params):
        """Fetch the index for a given model and supplied parameters.

        :param model: The model being queried.
        :param options: Query parameters (see shopify documentation)
        """

        self._can_request("index", model)

        req = Request(model, **params)

        res = self._get(req)

        if res.status_code == requests.codes.ok:
            if auto_instance:
                return Collection(model, res.json())
            else:
                return res.json()

        raise ShopifyException(res)

    def authorize_app_url(self):
        """Generates the oauth authorization url."""

        return self.oauth_authorize_url()

    def setup_access_token(self):
        """Utility function wrapping getting the oauth token and setting
        the credential values.
        """

        oauth_token = self.oauth_access_token()
        self.credentials.code = None
        self.credentials.oauth_access_token = oauth_token

        self.session.headers.update({
            'X-Shopify-Access-Token': self.credentials.oauth_access_token
        })

    def oauth_access_token(self):
        """Fetch the OAuth access token from shopify.

        :meth:`setup_access_token` should be used.
        """

        url = self.oauth_access_token_url()
        headers = {"Content-Type": self.mime}

        r = self.session.post(url, headers=headers)

        if r.status_code == requests.codes.ok:
            data = r.json()
            return data['access_token']

        raise ShopifyException(r)

    def _can_request(self, method, model):
        """Verify the request method is supported by the provided model.

        If the request method is not supported, an InvalidRequestException
        will be raised.

        :param method: The method to be executed (index, create, delete, etc.)
        :param model: A class or instance the request will be made for.
        """

        if method in model.supported or self.ignore_supported:
            #The method is either supported or the engine completely ignores
            #the check
            return

        msg = "`%s` is not supported by %s."

        if isinstance(model, type):
            model_name = model.__name__
        else:
            model_name = model.__class__.__name__

        raise InvalidRequestException(msg % (method, model_name))
