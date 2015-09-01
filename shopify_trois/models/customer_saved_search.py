# -*- coding: utf-8 -*-
'''
    shopify_trois.models.customer_saved_search

    Shopify-Trois CustomerSavedSearch

    :copyright: (c) 2015 Martin Samson
    :license: MIT, see LICENSE for more details.
'''

from .model import Model


class CustomerSavedSearch(Model):
    '''CustomerSsavedSearch
    http://docs.shopify.com/api/customersavedsearch
    '''

    resource = 'customer_saved_searches'

    supported = [
        'create', 'count', 'delete', 'index', '/customers', 'update', 'view'
    ]

    properties = [
        'created_at', 'id', 'name', 'updated_at', 'query'
    ]
