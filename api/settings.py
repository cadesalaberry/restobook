# Let's just use the local mongod instance. Edit as needed.

# Please note that MONGO_HOST and MONGO_PORT could very well be left
# out as they already default to a bare bones local 'mongod' instance.
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_USERNAME = 'user'
MONGO_PASSWORD = 'password'
MONGO_DBNAME = 'restobook'

# Allows CORS
X_DOMAINS = '*'


# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']


restaurants = {

  'schema': {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'owner_id': {
      'type': 'integer',
    },
    'capacity': {
      'type': 'integer',
    },
    'name': {
      'type': 'string',
      'minlength': 1,
      'maxlength': 20,
      'required': True,
    },

    'lat': {
      'type': 'float',
      'required': True,
    },
    'lng': {
      'type': 'float',
      'required': True,
    },
  }
}

reservations = {

  'schema': {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'restaurant_id': {
      'type': 'string',
    },
    'headcount': {
      'type': 'integer',
    },
    'name': {
      'type': 'string',
      'minlength': 1,
      'maxlength': 20,
    },

    'phone_number': {
      'type': 'string',
    }
  }
}


DOMAIN = {'restaurants': restaurants, 'reservations': reservations}
