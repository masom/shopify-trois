# -*- coding: utf-8 -*-
"""
    shopify_trois.models.model

    Shopify-Trois Model

    :copyright: (c) 2013 by Martin Samson
    :license: MIT, see LICENSE for more details.
"""

from .model import Model


class ApplicationCharge(Model):
    """ApplicationCharge
    http://docs.shopify.com/api/applicationcharge
    """

    resource = "application_charges"

    supported = ["index", "view", "create", "/activate"]

    properties = [
        "created_at", "id", "name", "price", "return_url", "status", "test",
        "updated_at", "confirmation_url"
    ]
