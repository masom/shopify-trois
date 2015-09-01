# -*- coding: utf-8 -*-
'''
    shopify_trois.models.checkout

    Shopify-Trois Checkout

    :copyright: (c) 2015 Martin Samson
    :license: MIT, see LICENSE for more details.
'''

from .model import Model


class Checkout(Model):
    '''Checkout
    http://docs.shopify.com/api/checkout
    '''

    resource = 'checkouts'

    supported = [
        'count', 'index'
    ]

    properties = [
        'abandoned_checkout_url', 'billing_address', 'buyer_accepts_marketing',
        'cancel_reason', 'cart_token', 'closed_at', 'completed_at',
        'created_at', 'currency', 'customer', 'discount_codes', 'email',
        'gateway', 'id', 'landing_site', 'line_items', 'note',
        'referring_site', 'shipping_address', 'shipping_lines', 'source_name',
        'subtotal_price', 'tax_lines', 'taxes_included', 'token',
        'total_discounts', 'total_line_items_price', 'total_price',
        'total_tax', 'total_weight', 'updated_at'
    ]
