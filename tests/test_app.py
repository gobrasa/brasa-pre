import requests
from flask import url_for

from backend.auth.auth import requires_auth


def test_mentees(client):

    assert client.get('/api/mentees').status_code == requests.codes.UNAUTHORIZED

    # ToDo - follow tutorial here
    # https://www.patricksoftwareblog.com/testing-a-flask-application-using-pytest/
