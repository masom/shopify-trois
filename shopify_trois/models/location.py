# -*- coding: utf-8 -*-
'''
    shopify_trois.models.location

    Shopify-Trois Location

    :copyright: (c) 2015 Martin Samson
    :license: MIT, see LICENSE for more details.
'''

from .model import Model


class Location(Model):
    '''Location
    http://docs.shopify.com/api/location
    '''

    resource = 'locations'

    supported = ['index', 'view']

    properties = [
        'id', 'name', 'location_type', 'address1', 'address2', 'zip', 'city',
        'province', 'country', 'phone', 'created_at', 'updated_at'
    ]
