from .. import ShopifyTroisTestCase
from shopify_trois.models.model import Model


class ModelTest(ShopifyTroisTestCase):
    def test(self):
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
        self.assertEquals(a.changes(), { 'name' : 'bob' })
        self.assertEquals(a.to_dict(), {'name' : 'bob', 'age' : 32})

        a = Model(name="test", id=2, age = 33)
        self.assertTrue(a.exists())
        self.assertEquals(a.changes(), {})
        self.assertEquals(a.to_dict(), {'name' : 'test', 'id': 2, 'age': 33})
