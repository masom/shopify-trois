# -*- coding: utf-8 -*-
'''
    shopify_trois.models.product_variant

    Shopify-Trois ProductVariant

    :copyright: (c) 2013 by Martin Samson
    :license: MIT, see LICENSE for more details.
'''

from .model import Model
from .product import Product


class ProductVariant(Model):
    ''' ProductVariant
    http://docs.shopify.com/api/productvariant
    '''

    resource = 'variants'
    is_subresource_of = Product
    enclosure = 'variant'

    supported = ['index', 'view', 'count', 'create', 'update', 'delete']

    properties = [
        'barcode', 'compare_at_price', 'created_at', 'fulfillment_service',
        'grams', 'id', 'inventory_management', 'inventory_policy', 'option1',
        'option2', 'option3', 'position', 'price', 'product_id',
        'requires_shipping', 'sku', 'taxable', 'title', 'updated_at',
        'inventory_quantity', 'old_inventory_quantity',
        'inventory_quantity_adjustment', 'metafield', 'weight', 'weight_unit',
        'image_id'
    ]
