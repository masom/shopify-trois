# -*- coding: utf-8 -*-
'''
    shopify_trois.models.shop

    Shopify-Trois Shop

    :copyright: (c) 2015 Martin Samson
    :license: MIT, see LICENSE for more details.
'''

from .model import Model


class Shop(Model):
    '''http://docs.shopify.com/api/shop'''

    resource = 'shop'

    supported = ['view']

    properties = [
        'address1', 'city', 'country', 'country_code', 'country_nane',
        'created_at', 'customer_email', 'currency', 'domain', 'email',
        'google_apps_domain', 'google_apps_login_enabled', 'id', 'latitude',
        'longitude', 'money_format', 'money_with_currency_format',
        'myshopify_domain', 'name', 'plan_name', 'password_enabled', 'phone',
        'primary_locale', 'province', 'province_code', 'ship_to_countries',
        'public', 'shop_owner', 'source', 'tax_shipping', 'taxes_included',
        'county_taxes', 'timezone', 'iana_timezone', 'zip', 'has_storefront',
        'setup_required'
    ]
