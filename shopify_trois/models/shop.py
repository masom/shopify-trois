# -*- coding: utf-8 -*-
"""
    shopify_trois.models.shop

    Shopify-Trois Shop

    :copyright: (c) 2013 by Martin Samson
    :license: MIT, see LICENSE for more details.
"""

from .model import Model

class Shop(Model):
    resource = "shops"

    def __init__(self, name):
        self.name = name
