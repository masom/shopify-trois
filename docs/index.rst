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

    from shopify_trois import Credentials, Collection
    from shopify_trois.models import *
    from shopify_trois.engines.http.json import Json as Shopify

    credentials = Credentials(
        api_key = 'your api key'
        ,scope = ['read_orders']
        ,secret = 'your api key secret'
    )
    shopify = Shopify(shop_name="your store name", credentials=credentials)

    # somehow redirect to the url provided by `shopify.oauth_authorize_url()`
    # print(shopify.oauth_authorize_url())
    # somehow receive the oauth temporary code and set it in the credentials object.

    credentials.code = "oauth temporary code"

    # fetch the access token
    shopify.setup_access_token()

    # credentials.oauth_access_token will contain the access token. It would be a good idea to save it somewhere.

    #the following line will show your store information.
    raw = shopify.index(Shop)
    shop = Shop(**raw['shop'])

    # Set the shop as public
    shop.public = True

    # Calling changes() on a model will show the modified properties.
    print(shop.changes())

    webhook = Webhook()
    webhook.address = "http://www.google.ca"
    webhook.format = "json"
    webhook.topic = "orders/create"

    # Create a new webhook, returning a dict. The original webhook is not modified.
    raw = shopify.add(webhook)

    # Get all the webhooks and iterates them
    raw = shopify.index(Webhook)
    webhooks = Collection(Webhook, raw)
    for webhook in webhooks:
        # webhook is a Webhook instance, created by iterating the Collection
        print(webhook.to_dict())


API
===

Initializing the API client
---------------------------
.. code-block:: python

    # import the credentials and the client
    from shopify_trois import Credentials
    from shopify_trois.engine.http.json import Json as Shopify

    credentials = Credentials(api_key="key", secret="secret")

    shopify = Shopify(shop_name="your_shop_name", credentials=credentials)

.. autoclass:: shopify_trois.engines.http.json.Json
    :members:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
