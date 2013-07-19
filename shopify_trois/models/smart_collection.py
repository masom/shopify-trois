# -*- coding: utf-8 -*-
"""
    shopify_trois.models.smart_collection

    Shopify-Trois SmartCollection

    :copyright: (c) 2013 by Martin Samson
    :license: MIT, see LICENSE for more details.
"""

from .model import Model


class SmartCollection(Model):
    """http://docs.shopify.com/api/smartcollection"""

    resource = "smart_collections"

    supported = ["index", "view", "count", "create", "update", "delete"]

    properties = [
        "body_html", "handle", "id", "products_count", "published_at",
        "published_scope", "sort_order", "template_suffix", "title",
        "updated_at", "rules", "image"
    ]
