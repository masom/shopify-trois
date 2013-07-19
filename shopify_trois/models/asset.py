# -*- coding: utf-8 -*-
"""
    shopify_trois.models.asset

    Shopify-Trois Asset

    :copyright: (c) 2013 by Martin Samson
    :license: MIT, see LICENSE for more details.
"""

from .model import Model
from .theme import Theme


class Asset(Model):
    """Asset is probably the weirdest resource exposed by Shopify.
    Create/Update is actually a PUT on theme/#{id}/assets.json
    Delete is a DELETE on theme/#{id}/assets.json and the asset key
    is passed by parameter...

    http://docs.shopify.com/api/asset
    """

    resource = "assets"
    is_subresource_of = Theme

    supported = ["index"]

    properties = [
        "key", "public_url", "created_at", "updated_at", "content_type",
        "size", "theme_id"
    ]
