# -*- coding: utf-8 -*-
"""
    shopify_trois.models.checkout

    Shopify-Trois Checkout

    :copyright: (c) 2013 by Martin Samson
    :license: MIT, see LICENSE for more details.
"""

from .model import Model


class Checkout(Model):
    """Checkout
    http://docs.shopify.com/api/checkout
    """

    resource = "checkouts"

    supported = [
        "count", "index"
    ]

    properties = [
        "buyer_accepts_marketing", "cart_token", "closed_at", "completed_at",
        "created_at", "currency", "email", "gateway", "id", "landing_site",
        "note", "referring_site", "shipping_lines", "subtotal_price",
        "tax_lines", "taxes_included", "token", "total_discounts",
        "total_line_items_price", "total_price", "total_tax", "total_weight",
        "updated_at", "line_items", "name", "note_attributes",
        "discount_codes", "billing_address", "shipping_address", "customer"
    ]
