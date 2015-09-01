# -*- coding: utf-8 -*-
'''
    shopify_trois.models.carrier_service

    Shopify-Trois CarrierService

    :copyright: (c) 2015 Martin Samson
    :license: MIT, see LICENSE for more details.
'''

from .model import Model


class CarrierService(Model):
    '''CarrierService
    http://docs.shopify.com/api/carrierservice
    '''

    resource = 'carrier_services'

    supported = [
        'index', 'create', 'view', 'delete', 'update'
    ]

    properties = [
        'active', 'callback_url', 'carrier_service_type'
        'name', 'service_discovery',
    ]
