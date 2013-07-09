# -*- coding: utf-8 -*-
"""
    shopify_trois.models.fulfillment

    Shopify-Trois Fulfillment

    :copyright: (c) 2013 by Martin Samson
    :license: MIT, see LICENSE for more details.
"""

from .model import Model
from .order import Order


class Fulfillment(Model):
    """Fulfillment
    http://docs.shopify.com/api/fulfillment
    """

    resource = "fulfillments"
    is_subresource_of = Order

    supported = ["count", "create", "index", "/cancel", "update", "view"]

    properties = [
        "fulfillment_service", "fulfillment_status", "grams", "id", "price",
        "product_id", "quantity", "requires_shipping", "sku", "title",
        "variant_id", "variant_title", "vendor", "name",
        "variant_inventory_management", "properties", "product_exists"
    ]
