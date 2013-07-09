# -*- coding: utf-8 -*-
"""
    shopify_trois.models.script_tag

    Shopify-Trois ScriptTag

    :copyright: (c) 2013 by Martin Samson
    :license: MIT, see LICENSE for more details.
"""

from .model import Model


class ScriptTag(Model):
    """ ScriptTag
    http://docs.shopify.com/api/scriptag
    """

    resource = "script_tags"

    supported = ["index", "view", "count", "create", "update", "delete"]

    properties = [
        "created_at", "id", "event", "src", "updated_at"
    ]
