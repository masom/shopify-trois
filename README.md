Shopify API for Python 3.3

[![Build Status](https://travis-ci.org/masom/shopify-trois.png?branch=master)](https://travis-ci.org/masom/shopify-trois)

#Usage

from shopify_trois import Credentials
from shopify_trois.models import *
from shopify_trois.engines.http.json import Json as Shopify

credentials = Credentials(
    api_key = 'your api key'
    ,scope = ['read_orders']
    ,secret = 'your api key secret'
)

shopify = Shopify(shop_name = "your shopify store name", credentials = credentials)

# somehow redirect to the url provided by `shopify.oauth_authorize_url()`

# somehow receive the oauth temporary code and set it in the credentials object.

credentials.code = "oauth temporary code"
# fetch the access token
shopify.engine.oauth_access_token()

# set the access token in the credentials object.
credentials.oauth_access_token = "your access token"

#the following line will show your store information.
print(shopify.index(Shop).to_dict())

#Installation

#Requirements
- requests ( https://pypi.python.org/pypi/requests )

