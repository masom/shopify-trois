# -*- coding: utf-8 -*-
"""
    shopify_trois.models.country

    Shopify-Trois Country

    :copyright: (c) 2013 by Martin Samson
    :license: MIT, see LICENSE for more details.
"""

from .model import Model


class Country(Model):
    """Country
    http://docs.shopify.com/api/country
    """

    resource = "countries"

    supported = ["index", "count", "view", "create", "update", "delete"]

    properties = [
        "code", "id", "name", "tax", "provinces",
        "weight_based_shipping_rates", "price_based_shipping_rates",
        "carrier_shipping_rate_providers"
    ]
