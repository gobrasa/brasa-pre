""" Script for adding users to auth0 interface """

import os
from dotenv import load_dotenv
from auth0.v3.management import Auth0
from auth_utils import get_auth0_token, id_generator, create_new_user_in_auth0
import pandas as pd

load_dotenv('auth0.env')

domain = os.getenv("DOMAIN")
non_interactive_client_id = os.getenv('CLIENT_ID_INTERACT_AUTH0')
non_interactive_client_secret = os.getenv('CLIENT_SECRET_INTERACT_AUTH0')
audience = 'https://{}/api/v2/'.format(domain)

mgmt_api_token = get_auth0_token(domain,
                                 non_interactive_client_id,
                                 non_interactive_client_secret,
                                 audience)

auth0 = Auth0(domain, mgmt_api_token)
# print (auth0.users.list(search_engine='v3'))

# user_created = create_new_user_in_auth0(auth0, "test123444@test123.com")
# TODO: Use username (user_created['username]) and store it in DB
usuarios1 = pd.read_excel(r'usuarios1.xlsx')
print(usuarios1.shape)
print(usuarios1)
senhas = []
for index, row in usuarios1.iterrows():
    email = row[1]
    print(email, row[2], '<--')
    password = row[2]
    try:
        user_created = create_new_user_in_auth0(auth0, email, password)
    except Exception as x:
        print(x)
        continue

    senhas.append([email, password])
    print(password)

test = pd.DataFrame(senhas, columns=['email', 'senha'])
print(test)
test.to_csv('senhas.csv')
