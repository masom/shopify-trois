# -*- coding: utf-8 -*-
'''
    shopify_trois.models.model

    Shopify-Trois Model

    :copyright: (c) 2015 Martin Samson
    :license: MIT, see LICENSE for more details.
'''

import re


class Meta():
    '''Holds model instance metadata'''

    def __init__(self):
        self.exists = False


class Model():
    '''Base model class for all Shopify resources.'''

    #: Holds the data enclosure name if not normalized.
    enclosure = None

    #: Mark the model as being a subresource of another.
    is_subresource_of = None

    #: Holds the model parent id value. Used with :attr:`is_subresource_of`.
    parent_id = None

    #: The model primary key.
    primary_key = 'id'

    #: List of properties exposed by the api.
    properties = []

    #: The shopify url resource.
    resource = ''

    #: List of supported actions on the resource.
    supported = []

    def __init__(self, *args, **kwargs):

        for k, v in kwargs.items():
            setattr(self, k, v)

        original_state = dict(self.__dict__)

        self._meta__ = Meta()
        self._meta__.original_state = original_state

        if hasattr(self, self.primary_key):
            self._meta__.exists = True

    def exists(self):
        '''Determine if the instance has been persisted.'''

        return self._meta__.exists

    def to_dict(self):
        '''Returns the instance as a dictionary.'''

        data = dict(self.__dict__)
        del(data['_meta__'])
        return data

    @classmethod
    def to_underscore_name(cls):
        '''Underscore the class name.'''

        # If an enclosure has been specified, use it.
        if cls.enclosure is not None:
            return cls.enclosure

        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', cls.__name__)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

    def update(self, data, ignore_properties=False):
        '''Update the instance with the provided data.

        :param data: Properties to update.
        :param ignore_properties: Only update known properties when set
                                  to false
        '''

        entity_name = self.to_underscore_name()

        if entity_name not in data:
            msg = 'The data set does not contain `%s`'
            raise KeyError(msg % entity_name)

        raw = data[entity_name]

        if ignore_properties:
            properties = raw.keys()
        else:
            properties = self.properties

        for k, v in raw.items():
            if k in properties:
                setattr(self, k, v)

    def changes(self):
        '''Returns a dictionary of attributes that have changed.

        http://stackoverflow.com/a/111364/1014879
        '''

        missing = object()
        result = {}
        for key, original in self._meta__.original_state.items():
            current = self.__dict__.get(key, missing)
            if current == missing:
                continue

            if original != current:
                result[key] = current
        return result
