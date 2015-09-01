# -*- coding: utf-8 -*-
'''
    shopify_trois.models.customer

    Shopify-Trois Customer

    :copyright: (c) 2015 Martin Samson
    :license: MIT, see LICENSE for more details.
'''

from .model import Model


class Customer(Model):
    '''Customer
    http://docs.shopify.com/api/customer
    '''

    resource = 'customers'

    supported = [
        'count', 'create', 'delete', 'index', 'search', 'update', 'view'
    ]

    properties = [
        'accepts_marketing', 'addresses', 'created_at', 'default_address',
        'email', 'first_name', 'id', 'last_name', 'last_order_id',
        'last_order_name', 'metafield', 'muiltipass_identifier', 'note',
        'orders_count', 'state', 'tags', 'tax_exempt', 'total_spent',
        'updated_at', 'verified_email'
    ]
