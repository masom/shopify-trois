# -*- coding: utf-8 -*-
"""
    shopify_trois.credentials

    Shopify-Trois Credentials

    :copyright: (c) 2013 by Martin Samson
    :license: MIT, see LICENSE for more details.
"""


class Meta():
    def __init__(self):
        self.exists = False


class Model():
    """Base model class for all Shopify resources."""

    """Resource name.
    Maps to a database table name, URL resource name, etc.
    """
    resource = ''

    """The model primary key."""
    primary_key = "id"

    """Mark the model as being a subresource of another."""
    is_subresource_of = None

    """List of supported actions on the resource."""
    supported = []

    """List of properties expoded by the api."""
    properties = []

    def __init__(self, *args, **kwargs):

        for k, v in kwargs.items():
            setattr(self, k, v)

        original_state = dict(self.__dict__)

        self._meta__ = Meta()
        self._meta__.original_state = original_state

        if hasattr(self, self.primary_key):
            self._meta__.exists = True

    def exists(self):
        return self._meta__.exists

    def to_dict(self):
        data = dict(self.__dict__)
        del(data['_meta__'])
        return data

    def changes(self):
        missing = object()
        result = {}
        for key, original in self._meta__.original_state.items():
            current = self.__dict__.get(key, missing)
            if current == missing:
                continue

            if original != current:
                result[key] = current
        return result
