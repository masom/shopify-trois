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

    def __init__(self, shop_name, credentials, ignore_supported=False):
        super().__init__(shop_name = shop_name, credentials = credentials)

        """When set to True, ignore checking for supported actions on models."""
        self.ignore_supported = ignore_supported

    def add(self, instance, fields):
        self._can_request("create", instance)

        req = Request(instance)
        req.data = json.dumps(instance.to_dict())

        res = self.post(req)

        if res.status_code == requests.codes.created:
            return res.json()

        raise ShopifyException(res)

    def remove(self, instance):
        self._can_request("delete", instance)

        req = Request(instance)

        res = self.delete(req)

        if res.status_code == requests.codes.ok:
            return res.json()

        raise ShopifyException(res)

    def update(self, instance, fields):
        self._can_request("update", instance)

        req = Request(instance)
        req.data = json.dumps(instance.to_dict())

        res = self.post(req)

        if res.status_code == requests.status.ok:
            return res.json()

        raise ShopifyException(res)

    def view(self, Model, primary_key):
        self._can_request("view", instance)

        req = Request(model)
        req.resource += "/{primary_key}".format(primary_key=primary_key)

        res = self.get(req)

        if res.status_code == requests.codes.ok:
            return res.json()

        raise ShopifyException(res)

    def index(self, model, **params):
        self._can_request("index", instance)

        req = Request(model)
        req.params = params

        res = self.get(req)

        if res.status_code == requests.codes.ok:
            return res.json()

        raise ShopifyException(res)

    def authorize_app_url(self):
        return self.oauth_authorize_url()

    def setup_access_token(self):
        oauth_token = self.oauth_access_token()
        self.credentials.code = None
        self.credentials.oauth_access_token = data['access_token']

    def oauth_access_token(self):
        url = self.oauth_access_token_url()
        headers = { "Content-Type": self.mime }

        r = requests.post(url, headers = headers)

        if r.status_code == requests.codes.ok:
            data = r.json()
            return data['access_token']
        else:
            raise ShopifyException(r.text())

    def _can_request(self, method, model):
        if not method in model.supported and not self.ignore_supported:
            msg = "`%s` is not supported by %s."

            if isinstance(model, type):
                model_name = model.__name__
            else:
                model_name = model.__class__.__name__

            raise InvalidRequestException(msg % (method, model_name))

