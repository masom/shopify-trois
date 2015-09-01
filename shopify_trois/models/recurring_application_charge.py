# -*- coding: utf-8 -*-
'''
    shopify_trois.models.recurring_application_charge

    Shopify-Trois RecurringApplicationCharge

    :copyright: (c) 2015 Martin Samson
    :license: MIT, see LICENSE for more details.
'''

from .model import Model


class RecurringApplicationCharge(Model):
    '''RecurringApplicationCharge
    http://docs.shopify.com/api/recurringapplicationcharge
    '''

    resource = 'recurring_application_charges'

    supported = ['index', 'view', 'create', '/activate']

    properties = [
        'activated_on', 'billing_on', 'cancelled_on', 'created_at', 'id',
        'name', 'price', 'return_url', 'status', 'test', 'trial_days',
        'trial_ends_on', 'updated_at', 'confirmation_url'
    ]
