# -*- coding: utf-8 -*-
'''
    shopify_trois.models.blog

    Shopify-Trois Blog

    :copyright: (c) 2015 Martin Samson
    :license: MIT, see LICENSE for more details.
'''

from .model import Model


class Blog(Model):
    '''Blog
    http://docs.shopify.com/api/blog
    '''

    resource = 'blogs'

    supported = ['index', 'count', 'view', 'create', 'update', 'delete']

    properties = [
        'commentable', 'created_at', 'feedburner', 'feedburner_location',
        'handle', 'id', 'metafield', 'template_suffix', 'title', 'updated_at',
        'tags'
    ]
