Shopify-Trois
===============

Links
-----

* `source <http://github.com/masom/shopify-trois>`_
* `Shopify API <http://api.shopify.com>`_

Docs
----
.. toctree::
   :maxdepth: 2

   models
   engines
   logging

API
===

App Authorization
-----------------
.. code-block:: python

    from shopify_trois import Credentials, Collection
    from shopify_trois.models import *
    from shopify_trois.engines.http import Json as Shopify

    credentials = Credentials(
        api_key='your api key',
        scope=['read_content', 'write_orders'],
        secret='your api key secret'
    )
    shopify = Shopify(shop_name="your store name", credentials=credentials)

    # Redirect the shop owner to the URL provided by `shopify.oauth_authorize_url()`
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
        scope=['read_content'],
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
    webhook.address = "http://do-not-copy-this.com"
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

    variant = ProductVariant(id=123, product_id=2)
    shopify.fetch(variant)


Metafields
----------

Shopify-Trois exposes metafields as it do for relationships.

Note: The ProductVariant metafield is currently unsupported.

.. code-block:: python

    shopify.index(BlogMetafield, parent_id=234224)

    metafield = BlogMetafield(id=2342, blog_id=3242424)
    shopify.fetch(metafield)

Accessing Multiple Shops
------------------------

Shopify-Trois can easily access multiple shops within
the same thread.

.. code-block:: python

    from shopify_trois import Credentials
    from shopify_trois.models import Shop
    from shopify_trois.engines.http import Json as Shopify

    credentials = {
        "a-store-name": Credentials(
            api_key='your-app-key',
            secret='your-app-secret',
            oauth_access_token='access-token',
            scope=['read_content']
        ),
        "another-store-name": Credentials(
            api_key='your-app-key',
            secret='your-app-secret',
            oauth_access_token='access-token',
            scope=['read_content']
        )
    }

    instances = [Shopify(shop_name=k, credentials=v) for k, v in credentials.items()]

    stores = [instance.fetch(Shop) for instance in instances]

    for store in stores:
        print(store.name)


Classes
----------

.. autoclass:: shopify_trois.engines.http.json.Json
    :members:
    :inherited-members:

.. autoclass:: shopify_trois.credentials.Credentials
    :members:

.. autoclass:: shopify_trois.collection.Collection
    :members:

Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
