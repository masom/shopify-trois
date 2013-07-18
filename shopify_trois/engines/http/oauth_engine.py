# -*- coding: utf-8 -*-
"""
    shopify_trois.engines.http.engine

    Shopify-Trois HTTP Engine

    :copyright: (c) 2013 by Martin Samson
    :license: MIT, see LICENSE for more details.
"""
import hashlib
import requests
from requests.models import PreparedRequest
from requests.structures import CaseInsensitiveDict


class OAuthEngine():
    """The OAuth engine is a base adapter implementation for the
    Shopify API using the OAuth authentication mechanism.

    Requests made with this engine will automatically contain the
    X-Shopify-Access-Token header.

    :param shop_name: The shopify store name
    :param credentials: A :class:`~shopify_trois.credential.Credential`
                        instance.
    """

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

        self.api_call_limit = None

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
            ('redirect_uri', redirect_to)
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

    def verify_signature(self, query_parameters):
        """Verify the signature provided with the query parameters.

        http://docs.shopify.com/api/tutorials/oauth

        example usage::

            from shopify_trois import Credentials
            from shopify_trois.engines import Json as Shopify
            from urllib.parse import parse_qsl

            credentials = Credentials(
                api_key='your_api_key',
                scope=['read_orders'],
                secret='your_app_secret'
            )

            shopify = Shopify(shop_name="your_store_name", credentials=\
                    credentials)

            query_parameters = parse_qsl("code=238420989938cb70a609f6ece2e2586\
b&shop=yourstore.myshopify.com&timestamp=1373382939&\
signature=6fb122e33c21851c465345b8cb97245e")

            if not shopify.verify_signature(query_parameters):
                raise Exception("invalid signature")

            credentials.code = dict(query_parameters).get('code')

            shopify.setup_access_token()

        :returns: Returns True if the signature is valid.

        """
        params = CaseInsensitiveDict(query_parameters)
        signature = params.pop("signature", None)

        calculated = ["%s=%s" % (k, v) for k, v in params.items()]
        calculated.sort()
        calculated = "".join(calculated)

        calculated = "{secret}{calculated}".format(
            secret=self.credentials.secret,
            calculated=calculated
        )

        md5 = hashlib.md5()
        md5.update(calculated.encode('utf-8'))

        produced = md5.hexdigest()

        return produced == signature

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

    def _update_call_limit(self, response):
        """Update the api_call_limit value from Shopify's response."""

        header = 'x-shopify-shop-api-call-limit'
        if header in response.headers:
            self.api_call_limit = response.headers[header]

    def _put(self, req):
        """Perform a PUT request to Shopify.

        :param req: See :class:`~shopify_trois.engines.http.request.Request`
        """

        url = self.url_for_request(req)
        response = self.session.put(
            url,
            params=req.params,
            data=req.data,
            headers=req.headers()
        )

        self._update_call_limit(response)

        return response

    def _get(self, req):
        """Perform a GET request to Shopify.

        :param req: See :class:`~shopify_trois.engines.http.request.Request`
        """

        url = self.url_for_request(req)
        response = self.session.get(
            url,
            params=req.params,
            headers=req.headers()
        )

        self._update_call_limit(response)

        return response

    def _post(self, req):
        """Perform a POST request to Shopify
        :param req: See :class:`~shopify_trois.engines.http.request.Request`
        """

        url = self.url_for_request(req)
        response = self.session.post(
            url,
            params=req.params,
            data=req.data,
            headers=req.headers()
        )

        self._update_call_limit(response)

        return response

    def _delete(self, req):
        """Perform a DELETE request to Shopify
        :param req: See :class:`~shopify_trois.engines.http.request.Request`
        """

        url = self.url_for_request(req)
        response = self.session.delete(
            url,
            params=req.params,
            data=req.data,
            headers=req.headers()
        )

        self._update_call_limit(response)

        return response
