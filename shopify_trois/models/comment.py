# -*- coding: utf-8 -*-
'''
    shopify_trois.models.comment

    Shopify-Trois Comment

    :copyright: (c) 2015 Martin Samson
    :license: MIT, see LICENSE for more details.
'''

from .model import Model


class Comment(Model):
    '''Comment
    http://docs.shopify.com/api/comment
    '''

    resource = 'comments'

    supported = [
        'count', 'create', 'index', 'update', 'view',
        '/spam', '/not_spam', '/approve', '/remove'
    ]

    properties = [
        'article_id', 'author', 'blog_id', 'body', 'body_html', 'created_at',
        'email', 'id', 'ip', 'published_at', 'status', 'updated_at',
        'user_agent'
    ]
