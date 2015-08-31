# -*- coding: utf-8 -*-
'''
    shopify_trois.models.transaction

    Shopify-Trois Transaction

    :copyright: (c) 2015 by Martin Samson
    :license: MIT, see LICENSE for more details.
'''

from .model import Model
from .order import Order


class Transaction(Model):
    '''Transaction
    http://docs.shopify.com/api/transactions
    '''

    resource = 'transactions'
    is_subresource_of = Order

    supported = ['index', 'count', 'view', 'create']

    properties = [
        'amount', 'authorization', 'created_at', 'currency', 'device_id',
        'error_code', 'gateway', 'id', 'kind', 'location_id', 'message',
        'order_id', 'payment_details', 'receipt', 'source_name',
        'status', 'user_id', 'device_id', 'test', 'receipt'
    ]
