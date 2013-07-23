The __awesome__ shopify api client for Python 3.3

[![Build Status](https://travis-ci.org/masom/shopify-trois.png?branch=master)](https://travis-ci.org/masom/shopify-trois)

[Documentation](http://masom.github.io/shopify-trois/ "Documentation")

#Installation

    pip install shopify-trois


### Example Flask Application

   [Flask-Trois](https://github.com/masom/flask-trois "Flask-Trois")

### Authorization

```python
    from shopify_trois import Credentials, Collection
    from shopify_trois.models import *
    from shopify_trois.engines.http import Json as Shopify

    credentials = Credentials(
        api_key='your api key',
        scope=['read_content', 'create_order'],
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
```

### Client Setup Once Authorized
```python
    credentials = Credentials(
        api_key='your api key',
        scope=['read_content'],
        secret='your app secret',
        oauth_access_token="your access token"
    )

    shopify = Shopify(shop_name="your store name", credentials=credentials)

    # The client is now ready to communicate with Shopify
    shopify.fetch(Shop).to_dict()
```

### Fetching

```python
    # Fetch the store information
    shop = shopify.fetch(Shop)

    # Set the shop as public
    shop.public = True

    # Calling changes() on a model instance will show the modified properties.
    print(shop.changes())
```

### Creating

```python
    webhook = Webhook()
    webhook.address = "http://do-not-just-copy-this.com"
    webhook.format = "json"
    webhook.topic = "orders/create"

    # Create the webhook
    shopify.add(webhook)

    # Get all the webhooks and iterates them
    webhooks = shopify.index(Webhook)
    for webhook in webhooks:
        # webhook is a Webhook instance, created by iterating the collection.
        print(webhook.to_dict())
```

### Flask Quick start

```python
    from flask import (Blueprint, render_template, session, redirect, url_for,
                    request, abort)

    from shopify_trois import Credentials
    from shopify_trois.engines.http import Json as Shopify

    from flask_trois import app

    auth = Blueprint('auth', __name__)


    @auth.route('/')
    @auth.route('/login', methods=['GET', 'POST'])
    def login():

        if 'store' in session:
            return redirect(url_for('store.view'))

        if request.method == 'POST':

            # Get the base app credentials. The SHOPIFY_CREDENTIALS
            # object should be a Credentials instance with the api_key, secret,
            # and scopes set.
            credentials = app.config.get('SHOPIFY_CREDENTIALS')

            #Setup a session to store the shop_name
            session['shop_name'] = shop_name = request.form['shop_name']

            #Setup a shopify adapter instance to create the authorization url
            shopify = Shopify(shop_name=shop_name, credentials=credentials)

            #Generate a url pointing back to an action on this blueprint
            redirect_to = url_for('.shopify_callback', _external=True)

            #Generate the oauth authorization url with a redirection to our app
            oauth_url = shopify.oauth_authorize_url(
                redirect_to=redirect_to
            )

            return redirect(oauth_url)

        return render_template('auth/login.html')


    @auth.route('/shopify_callback')
    def shopify_callback():
        if not 'shop_name' in session:
            abort(401)

        shop_name = session['shop_name']

        # Get the base app credentials
        base_credentials = app.config.get('SHOPIFY_CREDENTIALS')

        #Generate a new credential object with the base values
        credentials = Credentials(
            api_key=base_credentials.api_key,
            secret=base_credentials.secret
        )

        #Setup a shopify adapter instance to create the authorization url
        shopify = Shopify(shop_name=shop_name, credentials=credentials)

        #Verify the signature
        if not shopify.verify_signature(request.args):
            raise Exception("invalid signature")

        #Update the credentials object with the provided temporary code
        credentials.code = request.args.get('code')

        #Exchange the code for an access token
        shopify.setup_access_token()

        #Store the access token in the session
        session['access_token'] = credentials.oauth_access_token

        return redirect(url_for('shop.view'))
```

# Requirements
- requests ( https://pypi.python.org/pypi/requests )

