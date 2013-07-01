# -*- coding: utf-8 -*-
"""
    shopify_trois.engines.http.json_request

    Shopify-Trois JSON engine request.

    :copyright: (c) 2013 by Martin Samson
    :license: MIT, see LICENSE for more details.
"""

class JsonRequest:
    def __init__(self, method, params = None, model = None):

        '''
        HTTP method.
        '''
        self.method = method

        '''
        HTTP parameters.
        '''
        self.params = params

        '''
        Relative path from the base api.
        '''
        self.path = None
        self.body = None

        '''
        If we have a model, automatically generate the path and request body.
        '''
        if model is object:
            self.path = generate_url_for_model(model)

            if method in ['put', 'post']:
                self.body = json.dumps(model.export())


