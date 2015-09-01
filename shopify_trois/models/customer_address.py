# -*- coding: utf-8 -*-
'''
    shopify_trois.models.customer_address

    Shopify-Trois CustomerAddress

    :copyright: (c) 2015 Martin Samson
    :license: MIT, see LICENSE for more details.
'''

from .model import Model
from .customer import Customer


class CustomerAddress(Model):
    '''CustomerAddress
    https://docs.shopify.com/api/customeraddress
    '''

    resource = 'addresses'
    is_subresource_of = Customer

    supported = [
        'index', 'view', 'delete', 'update', 'create', '/set', '/default'
    ]

    properties = [
        'address1', 'address2', 'city', 'company', 'first_name',
        'last_name', 'phone', 'province', 'zip', 'name', 'province_code',
        'country_code', 'country_name'
    ]
