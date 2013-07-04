# -*- coding: utf-8 -*-
"""
    shopify_trois.engines.http.json

    Shopify-Trois JSON Engine

    :copyright: (c) 2013 by Martin Samson
    :license: MIT, see LICENSE for more details.
"""
import requests

from shopify_trois.engines.http.oauth_engine import OAuthEngine
from shopify_trois.engines.http.request import Request
from shopify_trois.exceptions import *

class Json(OAuthEngine):
    extension = 'json'
    mime = 'application/json; charset=utf-8'

    def __init__(self, shop_name, credentials, ignore_supported = False,
            ignore_model_properties = False):
        """Initialize the Json engine.

        :param shop_name: The name of the shopify store.
        :param credentials: :class:`~shopify_trois.credential.Credential`
        :param ignore_supported: When set to True, the engine will ignore
                                 the ``supported`` property of the models.
        :param ignore_model_properties: When set to True, the engine will
                                        ignore the ``properties`` property of
                                        models when persisting them.
        """

        super().__init__(shop_name = shop_name, credentials = credentials)

        #: When set to True, ignore checking for supported actions on models.
        self.ignore_supported = ignore_supported

    def add(self, instance):
        """Add the model instance to the store.

        :param instance: The model instance being added.
        """

        self._can_request("create", instance)

        #TODO use the model `properties` when generating the json document.

        req = Request(instance)
        req.data = json.dumps(instance.to_dict())

        res = self.post(req)

        if res.status_code == requests.codes.created:
            return res.json()

        raise ShopifyException(res)

    def remove(self, instance):
        """Remove (delete) a model instance.

        An InvalidRequestException will be raised if the instance does not yet
        exists.

        :param instance: The model instance to remove.
        """

        self._can_request("delete", instance)

        if not instance._meta.exists:
            msg = "The supplied instance does not yet exists."
            raise InvalidRequestException(msg)

        req = Request(instance)
        res = self.delete(req)

        if res.status_code == requests.codes.ok:
            return res.json()

        raise ShopifyException(res)

    def update(self, instance, whitelist = None):
        """Update a model instance.

        An InvalidRequestException will be raised if the instance has not been
        marked as existing.

        :param instance: The model instance being updated.
        :param whitelist: A list of attributes to be updated. If set to None,
                          all modified attributes will be updated.
        """

        self._can_request("update", instance)

        if not instance._meta.exists:
            msg = "The supplied instance does not yet exists."
            raise InvalidRequestException(msg)

        #TODO use the model `properties` when generating the json document.

        req = Request(instance)
        req.data = json.dumps(instance.to_dict())

        res = self.post(req)

        if res.status_code == requests.status.ok:
            return res.json()

        raise ShopifyException(res)

    def view(self, model, primary_key):
        """Get a specific model instance by primary key.

        :param Model: The class being queried.
        :param primary_key: The primary key value of the instance.
        """

        self._can_request("view", instance)

        req = Request(model)
        req.resource += "/{primary_key}".format(primary_key=primary_key)

        res = self.get(req)

        if res.status_code == requests.codes.ok:
            return res.json()

        raise ShopifyException(res)

    def index(self, model, **params):
        """Fetch the index for a given model and supplied parameters.

        :param model: The model being queried.
        :param options: Query parameters (see shopify documentation)
        """

        self._can_request("index", instance)

        req = Request(model)
        req.params = params

        res = self.get(req)

        if res.status_code == requests.codes.ok:
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
        self.credentials.oauth_access_token = data['access_token']

    def oauth_access_token(self):
        """Fetch the OAuth access token from shopify.

        :meth:`setup_access_token` should be used.
        """

        url = self.oauth_access_token_url()
        headers = { "Content-Type": self.mime }

        r = requests.post(url, headers = headers)

        if r.status_code == requests.codes.ok:
            data = r.json()
            return data['access_token']

        raise ShopifyException(r.text())

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

