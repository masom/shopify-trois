# -*- coding: utf-8 -*-
"""
    shopify_trois.engines.http.request

    Shopify-Trois Request.

    :copyright: (c) 2013 by Martin Samson
    :license: MIT, see LICENSE for more details.
"""

from .mapping import mapping as ResourceMapping

class Request:

    def __init__(self, model = None):
        self.__headers = {}

        '''
        HTTP parameters.
        '''
        self.params = None

        '''
        Relative path from the base api.
        '''
        self.resource = None

        self.result = None

        self.data = None

        if model is object:
            self.resource = self.generate_resource_for_model(model)

    def data(self):
        raise NotImplemented()

    def headers(self, key = None, value = None):
        if key is None:
            return self.__headers
        else:
            self.__headers[key] = value

    '''
    Generate the relative path of a given model.
    '''
    @classmethod
    def generate_resource_for_model(cls, model):

        """The ResourceMapping dict contains model resources mapping to
        a different name on the Shopify API.
        """

        resource = ResourceMapping.get(model.resource, model.resource)
        return "/%s" % resource
