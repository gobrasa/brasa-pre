import json
import random
import string

import requests
from auth0.v3.authentication import GetToken


def get_auth0_token(domain, client_id, client_secret, audience):
    """ Generates token for interacting with auth0 based apps """
    get_token = GetToken(domain)
    token = get_token.client_credentials(client_id,
                                         client_secret, audience)
    return token['access_token']


def id_generator(size=16, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    """ Generates random ID for being used as temporary password """
    return ''.join(random.choice(chars) for _ in range(size))


def create_new_user_in_db(username, email, role_name, users_endpoint, token, verbose=True):
    # create new user
    payload = {'username': username,
               'email': email,
               'role_name': role_name}
    r = requests.post('https://brasa-pre.herokuapp.com/api/users',
                      headers={'Authorization': 'Bearer {}'.format(token),
                               'Content-Type': 'application/json'},
                      data=json.dumps(payload))

    if verbose:
        print(r, r.json())


def create_new_user_in_auth0(auth0, email, password=id_generator(16)):
    body = {"email": email,
            "password": password,
            "connection": "Username-Password-Authentication"}

    return auth0.users.create(body=body)
