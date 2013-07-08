# -*- coding: utf-8 -*-
"""
    shopify_trois.engines.http.engine

    Shopify-Trois HTTP Engine

    :copyright: (c) 2013 by Martin Samson
    :license: MIT, see LICENSE for more details.
"""

import requests
from requests.models import PreparedRequest


class OAuthEngine():
    """"""

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
        """
        :param shop_name: The shopify store name
        :param credentials: A :class:`~shopify_trois.credential.Credential`
                            instance.
        """

        self.credentials = credentials

        self.base_url = self._api_base.format(shop_name=shop_name)

        self.session = requests.Session()
        self.session.headers.update({'Content-Type': self.mime})

        if credentials.oauth_access_token:
            self.session.headers.update({
                'X-Shopify-Access-Token': credentials.oauth_access_token
            })

    def oauth_authorize_url(self, redirect_to=None):
        """Generates the oauth authorize url.

        :param redirect_to: URL shopify will redirect to once authorized.
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
        """Generate the OAuth access token url."""

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
        """Generates the url for the provided request.

        :param req: See :class:`~shopify_trois.engines.http.request.Request`
        """

        url = "{api_base}{resource}.{extension}".format(
            api_base=self.base_url,
            resource=req.resource,
            extension=self.extension
        )

        return url

    def put(self, req):
        """Perform a PUT request to Shopify.

        :param req: See :class:`~shopify_trois.engines.http.request.Request`
        """

        url = self.url_for_request(req)
        request = self.session.put(
            url,
            params=req.params,
            data=req.data,
            headers=req.headers()
        )

        return request

    def get(self, req):
        """Perform a GET request to Shopify.

        :param req: See :class:`~shopify_trois.engines.http.request.Request`
        """

        url = self.url_for_request(req)
        request = self.session.get(
            url,
            params=req.params,
            headers=req.headers()
        )
        return request

    def post(self, req):
        """Perform a POST request to Shopify
        :param req: See :class:`~shopify_trois.engines.http.request.Request`
        """

        url = self.url_for_request(req)
        request = self.session.post(
            url,
            params=req.params,
            data=req.data,
            headers=req.headers()
        )

        return request

    def delete(self, req):
        """Perform a DELETE request to Shopify
        :param req: See :class:`~shopify_trois.engines.http.request.Request`
        """

        url = self.url_for_request(req)
        request = self.session.delete(
            url,
            params=req.params,
            data=req.data,
            headers=req.headers()
        )

        return request
