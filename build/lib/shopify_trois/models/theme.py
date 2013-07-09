# -*- coding: utf-8 -*-
"""
    shopify_trois.models.theme

    Shopify-Trois Theme

    :copyright: (c) 2013 by Martin Samson
    :license: MIT, see LICENSE for more details.
"""

from .model import Model


class Theme(Model):
    """ Theme
    http://docs.shopify.com/api/theme
    """

    resource = "themes"

    supported = ["index", "view", "create", "update", "delete"]

    properties = [
        "created_at", "id", "name", "role", "updated_at", "src"
    ]
