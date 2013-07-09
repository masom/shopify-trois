# -*- coding: utf-8 -*-
"""
    shopify_trois.models.order

    Shopify-Trois Order

    :copyright: (c) 2013 by Martin Samson
    :license: MIT, see LICENSE for more details.
"""

from .model import Model


class Order(Model):
    """Order
    http://docs.shopify.com/api/order
    """

    resource = "orders"

    supported = [
        "count", "create", "delete", "index", "/close", "/open", "/cancel",
        "update", "view"
    ]

    properties = [
        "buyer_accepts_marketing", "cancel_reason", "cancelled_at",
        "cart_token", "checkout_token", "closed_at", "confirmed",
        "created_at", "currency", "email", "financial_status",
        "fulfillment_status", "gateway", "id", "landing_site", "location_id",
        "name", "note", "number", "reference", "referring_site", "source",
        "subtotal_price", "taxes_included", "test", "token",
        "total_discounts", "total_line_items_price", "total_price",
        "total_price_usd", "total_tax", "total_weight", "updated_at",
        "user_id", "browser_ip", "landing_site_ref", "order_number",
        "discount_codes", "note_attributes", "processing_method",
        "checkout_id", "line_items", "shipping_lines", "tax_lines",
        "payment_details", "billing_address", "shipping_address",
        "fulfillments", "client_details", "customer"
    ]
