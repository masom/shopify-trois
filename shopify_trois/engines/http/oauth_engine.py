# -*- coding: utf-8 -*-
"""
    shopify_trois.engines.http.engine

    Shopify-Trois HTTP Engine

    :copyright: (c) 2013 by Martin Samson
    :license: MIT, see LICENSE for more details.
"""

"""
if shopify.shop is None:
"""

from collections import OrderedDict

from shopify_trois.exceptions import ShopifyException

from requests.models import PreparedRequest

class OAuthEngine:
    """The api base url."""
    _api_base = "https://{shop_name}.myshopify.com/admin"

    """The oauth authorize url."""
    _authorize_url = "{base_url}/admin/oauth/authorize"

    """The request extension."""
    extension = ''

    """The request mime type."""
    mime = ''

    def __init__(self, shopify):
        # Validate the shopify instance configuration before proceeding.
        shopify.validate_config()

        self.shopify = shopify
        self.base_url = self._api_base.format(shop_name=shopify.shop.name)

    def authorize_url(self):
        """Generates the oauth authorize url."""

        url = self._authorize_url.format(base_url = self.base_url)

        params = [
            ('client_id', self.shopify.credentials.api_key)
            ,('scope', ",".join(self.shopify.credentials.scope))
        ]

        request = PreparedRequest()
        request.prepare_url(url=url, params=params)
        return request.url

    def __request(self, request):
        """Perform a request to Shopify"""
