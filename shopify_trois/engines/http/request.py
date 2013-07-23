# -*- coding: utf-8 -*-
"""
    shopify_trois.engines.http.request

    Shopify-Trois Request.

    :copyright: (c) 2013 by Martin Samson
    :license: MIT, see LICENSE for more details.
"""

from shopify_trois.models.model import Model
from shopify_trois.exceptions import ShopifyException


class Request:
    """Shopify-Trois request wrapper.

    :param model: The model class or instance this request operates on.
    :param params: Query parameters.
    """

    def __init__(self, model=None, **params):
        self.__headers = {}

        '''
        HTTP parameters.
        '''
        self.params = params or None

        '''
        Relative path from the base api.
        '''
        self.resource = None

        self.data = None

        if model:
            self.resource = self.generate_resource_for_model(model)

    def headers(self, key=None, value=None):
        """Set request headers.

        :param key: The header name.
        :param value: The header value.
        """

        if key is None:
            return self.__headers
        else:
            self.__headers[key] = value

    def generate_resource_for_model(self, model):
        '''Generate the relative path of a given model.
        :param model: The model or instance this request operates on.
        '''

        is_instance = isinstance(model, Model)

        resource = model.resource

        if model.is_subresource_of:
            resource = self._generate_subresource_for_model(
                model,
                resource,
                is_instance
            )

        if is_instance and hasattr(model, model.primary_key):
            return "/{resource}/{id}".format(
                resource=resource,
                id=getattr(model, model.primary_key)
            )

        return "/%s" % resource

    def _generate_subresource_for_model(self, model, resource, is_instance):
        parent = model.is_subresource_of
        parent_id = None

        if is_instance:
            parent_pk = "{name}_{pk}".format(
                name=parent.__name__.lower(),
                pk=parent.primary_key
            )

            if not hasattr(model, parent_pk):
                raise ShopifyException(
                    "Missing parent primary key `%s`." % parent_pk
                )

            parent_id = getattr(model, parent_pk)

        else:
            parent_pk = "parent_id"
            if self.params:
                parent_id = self.params.pop("parent_id", None)

        if parent_id is None:
            raise ShopifyException(
                "Missing parent primary key `%s`." % (parent_pk,)
            )

        resource = "{parent}/{parent_id}/{resource}".format(
            parent=parent.resource,
            parent_id=parent_id,
            resource=model.resource
        )
        return resource
