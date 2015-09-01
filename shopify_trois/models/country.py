# -*- coding: utf-8 -*-
'''
    shopify_trois.models.country

    Shopify-Trois Country

    :copyright: (c) 2015 Martin Samson
    :license: MIT, see LICENSE for more details.
'''

from .model import Model


class Country(Model):
    '''Country
    http://docs.shopify.com/api/country
    '''

    resource = 'countries'

    supported = ['index', 'count', 'view', 'create', 'update', 'delete']

    properties = [
        'carrier_shipping_rate_providers' 'code', 'id', 'name',
        'price_based_shipping_rates', 'tax', 'provinces',
        'weight_based_shipping_rates'
    ]
