# -*- coding: utf-8 -*-
"""
    shopify_trois.credentials

    Shopify-Trois Credentials

    :copyright: (c) 2013 by Martin Samson
    :license: MIT, see LICENSE for more details.
"""
class Credentials:
    def __init__(self, api_key = "", scope = ""):
        self.api_key = api_key
        self.scope = scope

        self.oauth_token = None
        self.oauth_secret = None

        self.consumer_token = None
        self.consumer_secret = None
