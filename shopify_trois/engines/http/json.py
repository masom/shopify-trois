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

    def __init__(self, shop, credentials):
        super().__init__(shop = shop, credentials = credentials)


    def add(self, model, data):
        request = Request(model)
        request.data = json.dumps(data)
        return self.post(req)

    def remove(self, model, primary_key):
        request = Request(model)
        return self.delete(req)

    def update(self, model, data):
        request = Request(model)
        request.data = json.dumps(data)
        return self.post(req)

    def index(self, model):
        pass

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
