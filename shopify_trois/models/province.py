# -*- coding: utf-8 -*-
'''
    shopify_trois.models.province

    Shopify-Trois Province

    :copyright: (c) 2015 Martin Samson
    :license: MIT, see LICENSE for more details.
'''

from .model import Model
from .country import Country


class Province(Model):
    '''http://docs.shopify.com/api/province'''

    resource = 'provinces'

    is_subresource_of = Country

    supported = ['index', 'view', 'count', 'update']

    properties = [
        'code', 'country_id', 'id', 'name', 'tax', 'tax_name', 'tax_type',
        'tax_percentage'
    ]
