# -*- coding: utf-8 -*-
"""
    shopify_trois.models.custom_collection

    Shopify-Trois CustomCollection

    :copyright: (c) 2013 by Martin Samson
    :license: MIT, see LICENSE for more details.
"""

from .model import Model


class CustomCollection(Model):
    """CustomCollection
    http://docs.shopify.com/api/customcollection
    """

    resource = "custom_collections"

    supported = [
        "count", "create", "delete", "index", "update", "view"
    ]

    properties = [
        "body_html", "handle", "id", "products_count", "published_at",
        "published_scope", "sort_order", "template_suffix", "title",
        "updated_at", "image"
    ]
