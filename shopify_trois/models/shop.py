# -*- coding: utf-8 -*-
"""
    shopify_trois.models.shop

    Shopify-Trois Shop

    :copyright: (c) 2013 by Martin Samson
    :license: MIT, see LICENSE for more details.
"""

from .model import Model


class Shop(Model):
    """Shop
    http://docs.shopify.com/api/shop
    """
    resource = "shops"

    supported = ["index"]

    properties = [
        "address1", "city", "country", "created_at", "customer_email",
        "currency", "domain", "email", "google_apps_domain",
        "google_apps_login_enabled", "id", "latitude", "longitude",
        "money_format", "money_with_currency_format", "myshopify_domain",
        "name", "plan_name", "phone", "province", "public", "shop_owner",
        "source", "tax_shipping", "taxes_included", "timezone", "zip"
    ]
