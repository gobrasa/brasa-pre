""" Script for adding users to brasa-pre's database """

import json
import os

import requests
from dotenv import load_dotenv

from auth_utils import get_auth0_token, create_new_user_in_db

load_dotenv('auth0.env')

domain = os.getenv('DOMAIN')
audience = os.getenv('AUDIENCE_BACKEND')
non_interactive_client_id = os.getenv('CLIENT_ID_INTERACT_BACKEND')
non_interactive_client_secret = os.getenv('CLIENT_SECRET_INTERACT_BACKEND')
users_endpoint = os.getenv('HEROKU_USERS_ENDPOINT')

mgmt_api_token = get_auth0_token(domain,
                                 non_interactive_client_id,
                                 non_interactive_client_secret,
                                 audience)

# example - get all users
# r = requests.get('https://brasa-pre.herokuapp.com/api/users',
#                 headers={'Authorization': 'Bearer {}'.format(mgmt_api_token)})

create_new_user_in_db('johnny1234', 'test@test.com', 'mentee', users_endpoint, mgmt_api_token)
