# -*- coding: utf-8 -*-
'''
    shopify_trois.models.refund

    Shopify-Trois Refund

    :copyright: (c) 2015 by Martin Samson
    :license: MIT, see LICENSE for more details.
'''

from .model import Model
from .order import Order


class Refund(Model):
    '''http://docs.shopify.com/api/refund'''

    resource = 'refunds'

    is_subresource_of = Order

    supported = ['view']

    properties = [
        'created_at', 'id', 'note', 'refund_line_items', 'restock',
        'transactions', 'user_id'
    ]
