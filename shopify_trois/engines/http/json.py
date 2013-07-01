# -*- coding: utf-8 -*-
"""
    shopify_trois.engines.http.json

    Shopify-Trois JSON Engine

    :copyright: (c) 2013 by Martin Samson
    :license: MIT, see LICENSE for more details.
"""

import requests
from .engine import HttpEngine
from .json_request import JsonRequest

class Json(HttpEngine):
    extension = 'json'
    mime = 'application/json'

    '''
    Initialize a new instance of the Json engine with the supplied credentials.
    '''
    def __init__(self, credentials):
        print("Json engine loaded.")

        self._credentials = credentials;

