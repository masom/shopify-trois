# -*- coding: utf-8 -*-
"""
    shopify_trois.engines.http.engine

    Shopify-Trois HTTP Engine

    :copyright: (c) 2013 by Martin Samson
    :license: MIT, see LICENSE for more details.
"""

from collections import OrderedDict

from shopify_trois.exceptions import ShopifyException

import requests
from requests.models import PreparedRequest


class OAuthEngine():

    ERR_CREDENTIALS_NOT_SET = "The shopify instance does not yet know about" \
                              " the shop credentials."

    """The api base url."""
    _api_base = "https://{shop_name}.myshopify.com/admin"

    """The oauth authorize url."""
    _authorize_url = "{base_url}/oauth/authorize"
    _access_token_url = "{base_url}/oauth/access_token"

    """The request extension."""
    extension = ''

    """The request mime type."""
    mime = ''

    def __init__(self, shop_name, credentials):
        self.credentials = credentials

        # Validate the shopify instance configuration before proceeding.
        self.validate_config()

        self.base_url = self._api_base.format(shop_name=shop_name)

    def validate_config(self):
        if self.credentials is None:
            raise ShopifyException(ERR_CREDENTIALS_NOT_SET)

    def oauth_authorize_url(self, redirect_to=None):
        """Generates the oauth authorize url.

        redirect_to string URL shopify will redirect to once authorized.
        """

        url = self._authorize_url.format(base_url=self.base_url)

        params = [
            ('client_id', self.credentials.api_key),
            ('scope', ",".join(self.credentials.scope)),
            ('redirect_to', redirect_to)
        ]

        request = PreparedRequest()
        request.prepare_url(url=url, params=params)
        return request.url

    def oauth_access_token_url(self):
        url = self._access_token_url.format(base_url=self.base_url)

        params = [
            ('client_id', self.credentials.api_key),
            ('client_secret', self.credentials.secret),
            ('code', self.credentials.code)
        ]

        parser = PreparedRequest()
        parser.prepare_url(url=url, params=params)
        return parser.url

    def url_for_request(self, req):

        url = "{api_base}/{resource}.{extension}".format(
            api_base=self.base_url,
            resource=req.resource,
            extension=self.extension
        )

        return url

    def _prepare_request(self, req, use_access_token=True):
        if use_access_token:
            req.headers(
                'X-Shopify-Access-Token',
                self.credentials.oauth_access_token
            )

        req.headers('Content-Type', self.mime)

    def put(self, req):
        """Perform a PUT request to Shopify."""

        self._prepare_request(req)
        url = self.url_for_request(req)
        request = requests.put(
            url,
            params=req.params,
            data=req.data,
            headers=req.headers()
        )

        return request

    def get(self, req):
        """Perform a GET request to Shopify."""

        self._prepare_request(req)
        url = self.url_for_request(req)
        request = requests.get(url, params=req.params, headers=req.headers())
        return request

    def post(self, req):
        """Perform a POST request to Shopify"""

        self._prepare_request(req)
        url = self.url_for_request(req)
        request = requests.post(
            url,
            params=req.params,
            data=req.data,
            headers=req.headers()
        )

        return request
