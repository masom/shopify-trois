# -*- coding: utf-8 -*-
"""
    shopify_trois.shopify

    Shopify-Trois Shopify

    :copyright: (c) 2013 by Martin Samson
    :license: MIT, see LICENSE for more details.
"""

from shopify_trois.engines.http.oauth_engine import OAuthEngine
from shopify_trois.exceptions import ShopifyException

ERR_SHOP_NOT_SET = "The shopify instance does not yet know about the shop it is bound to."
ERR_CREDENTIALS_NOT_SET = "The shopify instance does not yet know about the shop credentials."

class Shopify:
    def __init__(self, shop = None, credentials = None, engine = OAuthEngine):
        self.shop = shop
        self.credentials = credentials

        self.engine = None

        if engine is not None:
            self.engine = engine(self)

    def start_engine(self, engine):
        self.engine = engine(self)

    def validate_config(self):
        if self.shop is None:
            raise ShopifyException(ERR_SHOP_NOT_SET)

        if self.credentials is None:
            raise ShopifyException(ERR_CREDENTIALS_NOT_SET)
