from .. import ShopifyTroisTestCase
from shopify_trois.models.model import Model


class TestModel(Model):
    resource = 'test'
    properties = ["id"]


class ModelTest(ShopifyTroisTestCase):
    def test_init(self):
        a = Model()
        self.assertTrue(hasattr(a, '_meta__'))
        self.assertFalse(a.exists())
        self.assertEquals(a.to_dict(), {})
        self.assertEquals(a.changes(), {})

        a.name = "test"
        self.assertEquals(a.changes(), {})
        self.assertEquals(a.to_dict(), {'name': 'test'})

        a = Model(name="test", age=32)
        self.assertFalse(a.exists())
        self.assertEquals(a.changes(), {})
        self.assertEquals(a.to_dict(), {'name': 'test', 'age': 32})

        a.name = "bob"
        self.assertEquals(a.changes(), {'name': 'bob'})
        self.assertEquals(a.to_dict(), {'name': 'bob', 'age': 32})

        a = Model(name="test", id=2, age=33)
        self.assertTrue(a.exists())
        self.assertEquals(a.changes(), {})
        self.assertEquals(a.to_dict(), {'name': 'test', 'id': 2, 'age': 33})

    def test_to_underscore_name(self):

        expected = "test_model"
        result = TestModel.to_underscore_name()
        self.assertEquals(result, expected)

    def test_update(self):
        a = TestModel()

        #Calling update with a dictionary that does not contain
        #the entity name should fail
        try:
            a.update({"hola": {}})
            self.fail()
        except KeyError:
            pass

        a.update({"test_model": {}})
        if a.to_dict():
            self.fail("The model should not have been updated.")

        a.update({"test_model": {"id": 3}})
        self.assertEquals(a.to_dict(), {"id": 3})

        a = TestModel(id=1)
        a.update({"test_model": {"id": 3}})
        self.assertEquals(a.changes(), {"id": 3})
