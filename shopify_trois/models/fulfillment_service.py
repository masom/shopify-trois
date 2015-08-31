# -*- coding: utf-8 -*-
'''
    shopify_trois.models.fulfillment_service

    Shopify-Trois FulfillmentService

    :copyright: (c) 2013 by Martin Samson
    :license: MIT, see LICENSE for more details.
'''

from .model import Model


class FulfillmentService(Model):
    '''FulfillmentService
    http://docs.shopify.com/api/fulfillmentservice
    '''

    resource = 'fulfillment_services'

    supported = ['index', 'count', 'view', 'create', 'update', 'delete']

    properties = [
        'callback_url', 'format', 'name', 'requires_shipping_method',
        'tracking_support',
        'credential1', 'email', 'handle', 'id', 'include_pending_stock',
        'name', 'service_name', 'inventory_management', 'provider_id',
        'credential2_exists'
    ]
