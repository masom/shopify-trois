import os
from shopify_trois import Credentials, Collection
from shopify_trois.models import *
from shopify_trois.engines.http.json import Json as Shopify

credentials = Credentials(
    api_key='7a1fbc5d5334a54286d1c1bdf3233873',
    scope=['read_orders'],
    secret='ba59073ff9aa21cec90845e36c177ccf'
)

#credentials.oauth_access_token = '8971481c4143fab4e00b2149e4cb295d'
shopify = Shopify(shop_name="masom-apps", credentials=credentials)

# somehow redirect to the url provided by `shopify.oauth_authorize_url()`
print(shopify.oauth_authorize_url())
# somehow receive the oauth temporary code and set it in the credentials object.

#os.exit()
from urllib.parse import parse_qsl
qs = parse_qsl("code=86cbee47eae00249e7042167b90e38c7&shop=masom-apps.myshopify.com&timestamp=1373383855&signature=35d7d5b7565ef34797768df89fdc9f2c")
if not (shopify.verify_signature(qs)):
    raise Exception("Invalid signature")

credentials.code = dict(qs).get('code')
print(credentials.code)
print(shopify.credentials.code)
# fetch the access token
shopify.setup_access_token()

# credentials.oauth_access_token will contain the access token. It would be a good idea to save it somewhere.
print(shopify.credentials.oauth_access_token)

#the following line will show your store information.
try:
    raw = shopify.view(Shop)
except Exception as e:
    print(e.args[0].request.headers)
    os.exit(1)

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
