# -*- coding: utf-8 -*-
"""
    shopify_trois.credentials

    Shopify-Trois Credentials

    :copyright: (c) 2013 by Martin Samson
    :license: MIT, see LICENSE for more details.
"""

'''
Base model class for all Shopify resources.
'''
class Model:
    """Resource name.
    Maps to a database table name, URL resource name, etc.
    """
    resource = ''

    primary_key = "id"
