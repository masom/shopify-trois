Shopify API for Python 3.3

[![Build Status](https://travis-ci.org/masom/shopify-trois.png?branch=master)](https://travis-ci.org/masom/shopify-trois)

#Usage

    from shopify_trois import Credentials, Collection
    from shopify_trois.models import *
    from shopify_trois.engines.http.json import Json as Shopify

    credentials = Credentials(
        api_key='your api key',
        scope=['create_webhooks'],
        secret='your api key secret'
    )
    shopify = Shopify(shop_name = "your store name", credentials = credentials)

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

#Installation

#Requirements
- requests ( https://pypi.python.org/pypi/requests )

