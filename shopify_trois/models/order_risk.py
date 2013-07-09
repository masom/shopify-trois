# -*- coding: utf-8 -*-
"""
    shopify_trois.models.order_risk

    Shopify-Trois OrderRisk

    :copyright: (c) 2013 by Martin Samson
    :license: MIT, see LICENSE for more details.
"""

from .model import Model
from .order import Order


class OrderRisk(Model):
    """ Page
    http://docs.shopify.com/api/orderrisk
    """

    resource = "risks"
    is_subresource_of = Order

    enclosure = "risk"

    supported = ["create", "update", "delete"]

    properties = [
        "cause_cancel", "checkout_id", "display", "id", "message", "order_id",
        "recommendation", "score", "source"
    ]
