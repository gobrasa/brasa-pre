from flask import url_for


def test_mentees(client):
    assert client.get('/api/mentees').status_code == 200

    # ToDo - follow tutorial here
    # https://www.patricksoftwareblog.com/testing-a-flask-application-using-pytest/
