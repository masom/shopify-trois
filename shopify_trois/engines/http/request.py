# -*- coding: utf-8 -*-
"""
    shopify_trois.engines.http.request

    Shopify-Trois Request.

    :copyright: (c) 2013 by Martin Samson
    :license: MIT, see LICENSE for more details.
"""

from .mapping import mapping as ResourceMapping

class Request:
    '''
    Generate the relative path of a given model.
    '''
    @classmethod
    def generate_path_for_model(cls, model):

        """The ResourceMapping dict contains model resources mapping to
        a different name on the Shopify API.
        """

        resource = ResourceMapping.get(model.resource, model.resource)
        return "/%s" % resource
