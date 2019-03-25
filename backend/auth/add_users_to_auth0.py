""" Script for adding users to auth0 interface """

import os
from dotenv import load_dotenv
from auth0.v3.management import Auth0
from auth_utils import get_auth0_token, id_generator, create_new_user_in_auth0

load_dotenv('auth0.env')

domain = os.getenv("DOMAIN")
non_interactive_client_id  = os.getenv('CLIENT_ID_INTERACT_AUTH0')
non_interactive_client_secret = os.getenv('CLIENT_SECRET_INTERACT_AUTH0')
audience = 'https://{}/api/v2/'.format(domain)

mgmt_api_token = get_auth0_token(domain,
                                 non_interactive_client_id,
                                 non_interactive_client_secret,
                                 audience)

auth0 = Auth0(domain, mgmt_api_token)
#print (auth0.users.list(search_engine='v3'))

user_created = create_new_user_in_auth0(auth0, "test123444@test123.com")
# ToDo - use username (user_created['username]) and store it in DB
