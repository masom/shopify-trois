# -*- coding: utf-8 -*-
'''
    shopify_trois.models.theme

    Shopify-Trois Theme

    :copyright: (c) 2015 Martin Samson
    :license: MIT, see LICENSE for more details.
'''

from .model import Model


class Theme(Model):
    ''' Theme
    http://docs.shopify.com/api/theme
    '''

    resource = 'themes'

    supported = ['index', 'view', 'create', 'update', 'delete']

    properties = [
        'created_at', 'id', 'name', 'previewable', 'processing', 'role', 'src',
        'updated_at'
    ]
