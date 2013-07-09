from ... import ShopifyTroisTestCase

from shopify_trois.exceptions import ShopifyException
from shopify_trois.engines.http.request import Request
from shopify_trois.models.model import Model


class TestModel(Model):
    resource = 'test'


class TestSubModel(TestModel):
    is_subresource_of = TestModel


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

        instance = TestModel(id=1)
        r = Request(instance)
        self.assertEquals(r.resource, '/test/1')

        r = Request(TestModel)
        self.assertEquals(r.resource, '/test')

    def test_generate_subresource_for_model(self):

        # This should fail due to not having a parent_id value
        # set on the class
        try:
            r = Request(TestSubModel)
            result = r.generate_resource_for_model()
            self.fail("A resource location should not have been generated."
                      " `%s` " % result)
        except ShopifyException:
            pass

        # This should fail due to not having a parent_id value
        # set on the instance
        m = TestSubModel()
        try:
            r = Request(m)
            result = r.generate_resource_for_model()
            self.fail()
        except ShopifyException:
            pass

        r = Request(TestSubModel, parent_id=2)
        self.assertEquals(r.resource, '/test/2/test')

        m.testmodel_id = 1
        r = Request(m)
        self.assertEquals(r.resource, '/test/1/test')

        m.id = 3
        r = Request(m)
        self.assertEquals(r.resource, '/test/1/test/3')
