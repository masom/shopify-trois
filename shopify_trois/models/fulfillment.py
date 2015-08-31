# -*- coding: utf-8 -*-
'''
    shopify_trois.models.fulfillment

    Shopify-Trois Fulfillment

    :copyright: (c) 2015 by Martin Samson
    :license: MIT, see LICENSE for more details.
'''

from .model import Model
from .order import Order


class Fulfillment(Model):
    '''Fulfillment
    http://docs.shopify.com/api/fulfillment
    '''

    resource = 'fulfillments'
    is_subresource_of = Order

    supported = [
        'index', 'count', 'view', 'create', 'update', '/complete', '/cancel'
    ]

    properties = [
        'created_at', 'id', 'order_id', 'service', 'status',
        'tracking_company', 'updated_at', 'tracker_number', 'tracking_numbers',
        'tracking_url', 'tracking_urls', 'receipt', 'line_items'
    ]
