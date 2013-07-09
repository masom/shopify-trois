# -*- coding: utf-8 -*-
"""
    shopify_trois.models.carrier_service

    Shopify-Trois CarrierService

    :copyright: (c) 2013 by Martin Samson
    :license: MIT, see LICENSE for more details.
"""

from .model import Model


class CarrierService(Model):
    """CarrierService
    http://docs.shopify.com/api/carrierservice
    """

    resource = "carrier_services"

    supported = [
        "index", "create", "view", "delete", "update"
    ]

    properties = [
        "name", "callback_url", "format", "service_discovery", "active",
        "carrier_service_type"
    ]
