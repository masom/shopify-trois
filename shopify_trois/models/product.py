# -*- coding: utf-8 -*-
"""
    shopify_trois.models.product

    Shopify-Trois Product

    :copyright: (c) 2013 by Martin Samson
    :license: MIT, see LICENSE for more details.
"""

from .model import Model


class Product(Model):
    """http://docs.shopify.com/api/product"""

    resource = "products"

    supported = ["index", "view", "create", "count", "update", "delete"]

    properties = [
        "body_html", "created_at", "handle", "id", "product_type",
        "published_at", "published_scope", "template_suffix", "title",
        "updated_at", "vendor", "tags", "variants", "options", "images",
        "image"
    ]
