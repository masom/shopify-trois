from . import ShopifyTroisTestCase
from shopify_trois.collection import Collection
from shopify_trois.models.model import Model

class CollectionTest(ShopifyTroisTestCase):

    def test(self):

        Model.resource = "test"

        try:
            c = Collection(Model, {})
            self.fail()
        except KeyError:
            pass

        try:
            c = Collection(Model, {"nope": 1})
            self.fail()
        except KeyError:
            pass

        try:
            c = Collection(Model, {"test": 3})
            self.fail()
        except TypeError:
            pass

        c = Collection(Model, {"test" : []})
        for entity in c:
            self.fail("The collection should be empty")

        c = Collection(Model, {"test": [{}]})
        for entity in c:
            self.assertIsInstance(entity, Model)

        c = Collection(Model, {"test": [{"name": "test"}]})
        for entity in c:
            self.assertEquals(entity.name, "test")
