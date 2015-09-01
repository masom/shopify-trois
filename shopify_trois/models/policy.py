# -*- coding: utf-8 -*-
'''
    shopify_trois.models.policy

    Shopify-Trois Policy

    :copyright: (c) 2015 Martin Samson
    :license: MIT, see LICENSE for more details.
'''

from .model import Model


class Policy(Model):
    '''http://docs.shopify.com/api/policy'''

    resource = 'policies'

    supported = ['index']

    properties = [
        'title', 'body', 'url'
    ]
