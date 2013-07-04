# -*- coding: utf-8 -*-
"""
    shopify_trois.collection

    Shopify-Trois Collection

    :copyright: (c) 2013 by Martin Samson
    :license: MIT, see LICENSE for more details.
"""

class Collection():
    def __init__(self, model, data):
        """Initialize a new collection for the given model and associated data.
        """
        self.model = model

        if not self.model.resource in data:
            msg = "The data set does not contain `%s`"
            raise KeyError(msg % self.model.resource)

        if not isinstance(data[self.model.resource], list):
            msg = "The data does not contain a list of `%s`."
            raise TypeError(msg % self.model.resource)

        self.data = data[self.model.resource]


    def __iter__(self):
        """Iterates the data array yielding a model instance."""

        for row in self.data:
            yield self.model(**row)
