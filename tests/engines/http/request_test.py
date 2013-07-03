from ... import ShopifyTroisTestCase

from shopify_trois.engines.http.request import Request
from shopify_trois.models.model import Model


class TestModel(Model):
    resource = 'test'

class RequestTestCase(ShopifyTroisTestCase):

    def test_init(self):
        r = Request()
        self.assertEquals(r.params, None)
        self.assertEquals(r.resource, None)
        self.assertEquals(r.data, None)

    def test_headers(self):

        r = Request()
        self.assertEquals(r.headers(), {})

        r.headers('test', 'value')
        self.assertEquals(r.headers(), {'test': 'value'})

        r.headers('test', None)
        self.assertEquals(r.headers(), {'test': None})

        r.headers('test2', None)
        self.assertEquals(r.headers(), {'test': None, 'test2': None})

    def test_generate_resource_for_model(self):

        r = Request()
        result = r.generate_resource_for_model(TestModel)
        self.assertEquals(result, '/test')

        r = Request()
        model = TestModel()
        model.id = '1'
        result = r.generate_resource_for_model(model)
        self.assertEquals(result, '/test/1')

