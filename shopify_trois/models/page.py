# -*- coding: utf-8 -*-
'''
    shopify_trois.models.page

    Shopify-Trois Page

    :copyright: (c) 2015 by Martin Samson
    :license: MIT, see LICENSE for more details.
'''

from .model import Model


class Page(Model):
    ''' Page
    http://docs.shopify.com/api/page
    '''

    resource = 'pages'

    supported = ['index', 'view', 'create', 'count', 'update', 'delete']

    properties = [
        'author', 'body_html', 'created_at', 'handle', 'id','metafield',
        'published_at', 'shop_id', 'template_suffix', 'title', 'updated_at'
    ]
