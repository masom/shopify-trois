# -*- coding: utf-8 -*-
"""
    shopify_trois.models.customer_group

    Shopify-Trois CustomerGroup

    :copyright: (c) 2013 by Martin Samson
    :license: MIT, see LICENSE for more details.
"""

from .model import Model


class CustomerGroup(Model):
    """CustomerGroup
    http://docs.shopify.com/api/customergroup
    """

    resource = "customer_groups"

    supported = [
        "create", "delete", "index", "/customers", "update", "view"
    ]

    properties = [
        "created_at", "id", "name", "updated_at", "query"
    ]
