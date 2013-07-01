from ... import ShopifyTroisTestCase

from shopify_trois.exceptions import ShopifyException

from shopify_trois import Shopify, Shop, Credentials

from shopify_trois.engines.http.oauth_engine import OAuthEngine

class OAuthEngineTestCase(ShopifyTroisTestCase):

    def test_class(self):
        expected = "https://{shop_name}.myshopify.com/admin"
        self.assertEqual(OAuthEngine._api_base, expected)

        expected = "{base_url}/admin/oauth/authorize"
        self.assertEqual(OAuthEngine._authorize_url, expected)

        self.assertEqual(OAuthEngine.extension, "")
        self.assertEqual(OAuthEngine.mime, "")

    def test_init(self):

        # __init__ should fail when a shopify instance is not passed.
        try:
            engine = OAuthEngine(None)
            self.fail()
        except AttributeError:
            pass

        # __init__ should fail when the shop or credentials were not passed.
        shopify = Shopify(engine = None)
        try:
            shopify.start_engine(OAuthEngine)
        except ShopifyException:
            pass

        shop = Shop(name = 'test')
        shopify = Shopify(engine = None, shop = shop)
        try:
            shopify.start_engine(OAuthEngine)
        except ShopifyException:
            pass


        credentials = Credentials()
        shopify = Shopify(engine = None, shop = shop, credentials = credentials)
        try:
            shopify.start_engine(OAuthEngine)
        except ShopifyException:
            pass

    def test_authorize(self):
        shop = Shop(name = 'test')
        credentials = Credentials()
        shopify = Shopify(shop = shop, credentials = credentials)

        url = shopify.engine.authorize_url()
        expected = "https://test.myshopify.com/admin/admin/oauth/authorize?client_id=&scope="
        self.assertEquals(url, expected)

        api_key = "2e6fff2c-e28d-11e2-b6bf-4061860bdbf3"
        credentials.api_key = api_key

        url = shopify.engine.authorize_url()
        expected = "https://test.myshopify.com/admin/admin/oauth/authorize?client_id={api_key}&scope=".format(api_key = api_key)
        self.assertEquals(url, expected)

        credentials.scope = ["fun", "things", "to", "scope", "W$%3'#"]
        url = shopify.engine.authorize_url()
        expected = "https://test.myshopify.com/admin/admin/oauth/authorize?client_id=2e6fff2c-e28d-11e2-b6bf-4061860bdbf3&scope=fun%2Cthings%2Cto%2Cscope%2CW%24%253%27%23"
        self.assertEquals(url, expected)

    def test_request(self):
        pass
