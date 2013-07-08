# -*- coding: utf-8 -*-
"""
    shopify_trois.credentials

    Shopify-Trois Credentials

    :copyright: (c) 2013 by Martin Samson
    :license: MIT, see LICENSE for more details.
"""

import re


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

    """Holds the model parent id value. Used with :attr:`is_subresource_of`."""
    parent_id = None

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

    @classmethod
    def to_underscore_name(cls):
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', cls.__name__)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

    def update(self, data, ignore_properties=False):

        entity_name = self.to_underscore_name()

        if not entity_name in data:
            msg = "The data set does not contain `%s`"
            raise KeyError(msg % self.resource)

        raw = data[entity_name]

        if ignore_properties:
            properties = raw.keys()
        else:
            properties = self.properties

        for k, v in raw.items():
            if k in properties:
                setattr(self, k, v)

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
