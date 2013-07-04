# -*- coding: utf-8 -*-
"""
    shopify_trois.models.shop

    Shopify-Trois Webhook

    :copyright: (c) 2013 by Martin Samson
    :license: MIT, see LICENSE for more details.
"""

from .model import Model


class Webhook(Model):
    """ Webhook
    http://docs.shopify.com/api/webhook
    """

    resource = "webhooks"

    supported = ["index", "count", "view", "create", "update", "delete"]

    properties = [
        "address", "created_at", "format", "id", "topic", "updated_at"
    ]
