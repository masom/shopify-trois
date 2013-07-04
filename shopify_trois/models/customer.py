# -*- coding: utf-8 -*-
"""
    shopify_trois.models.customer

    Shopify-Trois Customer

    :copyright: (c) 2013 by Martin Samson
    :license: MIT, see LICENSE for more details.
"""

from .model import Model

class Customer(Model):
    """Customer
    http://docs.shopify.com/api/customer
    """

    resource="customers"

    supported = [
        "count", "create", "delete", "index", "search", "update", "view"
    ]

    properties = [
        "accepts_marketing", "created_at", "email", "first_name", "id"
        ,"last_name", "last_order_id", "muiltipass_identifier", "note"
        ,"order_count", "state", "total_spent", "updated_at", "verified_email"
        ,"tags", "last_order_name", "default_address", "addresses"
    ]
