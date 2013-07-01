# -*- coding: utf-8 -*-
"""
    shopify_trois.engines.http.engine

    Shopify-Trois HTTP Engine

    :copyright: (c) 2013 by Martin Samson
    :license: MIT, see LICENSE for more details.
"""

class HttpEngine:
    """The request extension."""
    extension = ''

    """The request mime type."""
    mime = ''

    '''
    Perform a request to Shopify
    '''
    def __request(self, request):
        pass
