# -*- coding: utf-8 -*-
'''
    shopify_trois.models.collect

    Shopify-Trois Collect

    :copyright: (c) 2015 Martin Samson
    :license: MIT, see LICENSE for more details.
'''

from .model import Model


class Collect(Model):
    '''Collect
    http://docs.shopify.com/api/collect
    '''

    resource = 'collects'

    supported = [
        'count', 'create', 'index', 'view', 'delete'
    ]

    properties = [
        'collection_id', 'created_at', 'featured', 'id', 'product_id',
        'sort_value', 'updated_at', 'position'
    ]
