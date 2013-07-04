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


class Json(OAuthEngine):
    extension = 'json'
    mime = 'application/json; charset=utf-8'

    def __init__(self, shop_name, credentials):
        super().__init__(shop_name = shop_name, credentials = credentials)


    def add(self, instance, fields):
        req = Request(instance)
        req.data = json.dumps(instance.to_dict())
        return self.post(req)

    def remove(self, instance):
        req = Request(instance)
        return self.delete(req)

    def update(self, instance, fields):
        req = Request(instance)
        req.data = json.dumps(instance.to_dict())
        return self.post(req)

    def find_by_id(self, Model, primary_key):
        req = Request(model)
        req.resource += "/{primary_key}".format(primary_key=primary_key)
        return self.get(req)

    def index(self, model, **params):
        req = Request(model)
        req.params = params

        res = self.get(req)

        if res.status_code == requests.codes.ok:
            return model(**res.json())

        # todo raise an exception


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
