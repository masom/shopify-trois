# -*- coding: utf-8 -*-
'''
    shopify_trois.models.product_image

    Shopify-Trois ProductImage

    :copyright: (c) 2013 by Martin Samson
    :license: MIT, see LICENSE for more details.
'''

from .model import Model
from .product import Product


class ProductImage(Model):
    ''' ProductImage
    http://docs.shopify.com/api/productimage
    '''

    resource = 'images'
    is_subresource_of = Product
    enclosure = 'image'

    supported = ['index', 'view', 'create', 'delete']

    properties = [
        'created_at', 'id', 'position', 'product_id', 'updated_at',
        'variant_ids', 'src'
    ]
