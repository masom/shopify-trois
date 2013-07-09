# -*- coding: utf-8 -*-
"""
    shopify_trois.models.redirect

    Shopify-Trois Redirect

    :copyright: (c) 2013 by Martin Samson
    :license: MIT, see LICENSE for more details.
"""

from .model import Model


class Redirect(Model):
    """ Redirect
    http://docs.shopify.com/api/redirect
    """

    resource = "redirects"

    supported = ["index", "view", "count", "create", "update", "delete"]

    properties = [
        "created_at", "id", "path", "target", "updated_at"
    ]
