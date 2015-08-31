# -*- coding: utf-8 -*-
'''
    shopify_trois.models.webhook

    Shopify-Trois Webhook

    :copyright: (c) 2015 by Martin Samson
    :license: MIT, see LICENSE for more details.
'''

from .model import Model


class Webhook(Model):
    ''' Webhook
    http://docs.shopify.com/api/webhook
    '''

    resource = 'webhooks'

    supported = ['index', 'count', 'view', 'create', 'update', 'delete']

    properties = [
        'address', 'created_at', 'fields', 'format', 'id',
        'metafield_namespaces', 'topic', 'updated_at'
    ]

    available_topics = [
        'orders/create',
        'orders/delete',
        'orders/updated',
        'orders/paid',
        'orders/cancelled',
        'orders/fulfilled',
        'orders/partially_fulfilled',
        'order_transactions/create',
        'carts/create',
        'carts/update',
        'checkouts/create',
        'checkouts/update',
        'checkouts/delete',
        'refunds/create',
        'products/create',
        'products/update',
        'products/delete',
        'collections/create',
        'collections/update',
        'collections/delete',
        'customer_groups/create',
        'customer_groups/update',
        'customer_groups/delete',
        'customers/create',
        'customers/enable',
        'customers/disable',
        'customers/update',
        'customers/delete',
        'fulfillments/create',
        'fulfillments/update',
        'shop/update',
        'disputes/create',
        'disputes/update',
        'app/uninstalled'
    ]
