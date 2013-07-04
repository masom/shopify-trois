# -*- coding: utf-8 -*-
"""
    shopify_trois.credentials

    Shopify-Trois Credentials

    :copyright: (c) 2013 by Martin Samson
    :license: MIT, see LICENSE for more details.
"""
class Credentials:
    def __init__(self, api_key = "", secret = "", scope = "", code = "",
            oauth_access_token = None):

        self.api_key = api_key
        self.secret= secret
        self.scope = scope
        self.code = code
        self.oauth_access_token = oauth_access_token
