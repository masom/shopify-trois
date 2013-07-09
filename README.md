Shopify API for Python 3.3

[![Build Status](https://travis-ci.org/masom/shopify-trois.png?branch=master)](https://travis-ci.org/masom/shopify-trois)

[Documentation](http://masom.github.io/shopify-trois/ "Documentation")

#Installation

    pip install shopify-trois



#Usage

## Authorization

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

## Client Setup Once Authorized

    credentials = Credentials(
        api_key='your api key',
        scope=['read_orders'],
        secret='your app secret',
        oauth_access_token="your access token"
    )

    shopify = Shopify(shop_name="your store name", credentials=credentials)

    # The client is now ready to communicate with Shopify
    shopify.fetch(Shop).to_dict()

## Fetching data

    # Fetch the store information
    shop = shopify.fetch(Shop)

    # Set the shop as public
    shop.public = True

    # Calling changes() on a model instance will show the modified properties.
    print(shop.changes())

## Creating data

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

#Requirements
- requests ( https://pypi.python.org/pypi/requests )

