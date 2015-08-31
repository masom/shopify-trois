from .application_charge import ApplicationCharge
from .article import Article
from .asset import Asset
from .blog import Blog
from .carrier_service import CarrierService
from .checkout import Checkout
from .collect import Collect
from .comment import Comment
from .country import Country
from .custom_collection import CustomCollection
from .customer import Customer
from .customer_saved_search import CustomerSavedSearch
from .event import Event
from .fulfillment import Fulfillment
from .fulfillment_service import FulfillmentService
from .location import Location
from .metafield import Metafield
from .order import Order
from .order_risk import OrderRisk
from .page import Page
from .product import Product
from .product_image import ProductImage
from .product_search_engine import ProductSearchEngine
from .product_variant import ProductVariant
from .province import Province
from .recurring_application_charge import RecurringApplicationCharge
from .redirect import Redirect
from .shop import Shop
from .smart_collection import SmartCollection
from .theme import Theme
from .transaction import Transaction
from .webhook import Webhook

#
# One file per class seems overkill for these 'aliases'
#


class ShopMetafield(Metafield):
    pass


class BlogMetafield(Metafield):
    is_subresource_of = Blog


class CustomCollectionMetafield(Metafield):
    is_subresource_of = CustomCollection


class CustomerMetafield(Metafield):
    is_subresource_of = Customer


class OrderMetafield(Metafield):
    is_subresource_of = Order


class PageMetafield(Metafield):
    is_subresource_of = Page


class ProductMetafield(Metafield):
    is_subresource_of = Product


# ProductVariantMetafield is currently disabled due to the relative complexity
# of implementing it compared to the others.
#
# Boils down to looping the class resource ancestry.
#
# class ProductVariantMetafield(Metafield):
#     is_subresource_of = ProductVariant


__all__ = [
    'ApplicationCharge',
    'Article',
    'Asset',
    'Blog',
    'CarrierService',
    'Checkout',
    'Collect',
    'Comment',
    'Country',
    'CustomCollection',
    'Customer',
    'CustomerAddress',
    'CustomerSavedSearch',
    'Event',
    'Fulfillment',
    'FulfillmentService',
    'Location',
    'Metafield',
    'Order',
    'OrderRisk',
    'Page',
    'Product',
    'ProductImage',
    'ProductSearchEngine',
    'ProductVariant',
    'Province',
    'RecurringApplicationCharge',
    'Redirect',
    'Shop',
    'SmartCollection',
    'Theme',
    'Transaction',
    'Webhook'
]
