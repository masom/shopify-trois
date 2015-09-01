# -*- coding: utf-8 -*-
'''
    shopify_trois.models.event

    Shopify-Trois Event

    :copyright: (c) 2015 Martin Samson
    :license: MIT, see LICENSE for more details.
'''

from .model import Model


class Event(Model):
    '''Event
    http://docs.shopify.com/api/event
    '''

    resource = 'events'

    supported = ['count', 'index', 'view']

    properties = [
        'arguments', 'body', 'created_at', 'id', 'description',
        'path', 'subject_id', 'subject_type',
        'verb', 'message'
    ]
