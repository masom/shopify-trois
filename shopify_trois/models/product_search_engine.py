# -*- coding: utf-8 -*-
"""
    shopify_trois.models.product_search_engine

    Shopify-Trois ProductSearchEngine

    :copyright: (c) 2013 by Martin Samson
    :license: MIT, see LICENSE for more details.
"""

from .model import Model


class ProductSearchEngine(Model):
    """http://docs.shopify.com/api/productsearchengine"""

    resource = "product_search_engines"

    supported = ["index"]

    properties = [
        "created_at", "name"
    ]
