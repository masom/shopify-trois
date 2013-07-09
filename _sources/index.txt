.. Shopify-Trois documentation master file, created by
   sphinx-quickstart on Thu Jul  4 14:14:16 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Shopify-Trois
===============

Introduction
------------
Shopify-Trois provides a somewhat loose API to access and modify Shopify
store resources.

Links
-----

* `source <http://github.com/masom/shopify-trois>`_
* `Shopify API <http://api.shopify.com>`_


Example
-------
.. code-block:: python



API
===

App Authorization
-----------------
.. code-block:: python

    from shopify_trois import Credentials, Collection
    from shopify_trois.models import *
    from shopify_trois.engines.http.json import Json as Shopify

    credentials = Credentials(
        api_key='your api key',
        scope=['create_webhooks'],
        secret='your api key secret'
    )
    shopify = Shopify(shop_name="your store name", credentials=credentials)

    # Redirect the shop owner to the url provided by `shopify.oauth_authorize_url()`
    # print(shopify.oauth_authorize_url())
    # Get the oauth temporary code and set it in the credentials object.

    credentials.code = "oauth temporary code"

    # fetch the access token
    shopify.setup_access_token()

    # credentials.oauth_access_token will contain the access token. It would be a good idea to save it somewhere.

Client Setup Once Authorized
----------------------------

.. code-block:: python

    credentials = Credentials(
        api_key='your api key',
        scope=['read_orders'],
        secret='your app secret',
        oauth_access_token="your access token"
    )

    shopify = Shopify(shop_name="your store name", credentials=credentials)

    # The client is now ready to communicate with Shopify
    shopify.fetch(Shop).to_dict()

Working With Data
-----------------

.. code-block:: python

    # Fetch the store information
    shop = shopify.fetch(Shop)

    # Set the shop as public
    shop.public = True

    # Calling changes() on a model instance will show the modified properties.
    print(shop.changes())

    webhook = Webhook()
    webhook.address = "http://www.google.ca"
    webhook.format = "json"
    webhook.topic = "orders/create"

    # Create the webhook
    shopify.add(webhook)

    # Get all the webhooks and iterates them
    webhooks = shopify.index(Webhook)
    for webhook in webhooks:
        # webhook is a Webhook instance, created by iterating the Collection
        print(webhook.to_dict())

Relationships
-------------

Shopify-Trois has basic entity relationship support.
Some entities have been marked as subresources of another.

.. code-block:: python

    shopify.index(ProductVariant, parent_id=2)

    variant = ProductVariant(product_id=2)
    shopify.fetch(variant)

Classes
----------

.. autoclass:: shopify_trois.engines.http.json.Json
    :members:

.. autoclass:: shopify_trois.credentials.Credentials
    :members:

.. autoclass:: shopify_trois.collection.Collection
    :members:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
