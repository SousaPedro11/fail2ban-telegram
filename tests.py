import os

import pytest
import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

load_dotenv('.env')


@pytest.fixture
def url():
    # return 'http://localhost:5000/'
    return 'https://fail2ban-telegram.herokuapp.com/'

@pytest.fixture
def auth():
    user = str(os.environ.get('HTTPAUTH_USER'))
    password = str(os.environ.get('HTTPAUTH_PASS'))
    return HTTPBasicAuth(user, password)


def test_get_not_authorized(url):
    response = requests.get(url)
    assert response.status_code == 401


def test_get_authorized(url, auth):
    response = requests.get(url=url, auth=auth)
    assert response.status_code == 200


def test_post_not_authorized(url):
    response = requests.post(url=url)
    assert response.status_code == 401


def test_post_authorized_empty(url, auth):
    response = requests.post(url=url, auth=auth)
    assert response.status_code == 400


def test_post_authorized_only_origin(url, auth):
    json = {
        'origin_ip': '200.68.3.2'
    }
    response = requests.post(url=url, auth=auth, json=json)
    print(response.content)
    assert response.status_code == 400


def test_post_authorized_no_protocol(url, auth):
    json = {
        'origin_ip': '200.68.3.2',
        'target_ip': '209.67.4.2'
    }
    response = requests.post(url=url, auth=auth, json=json)
    print(response.content)
    assert response.status_code == 400


def test_post_authorized_no_origin(url, auth):
    json = {
        'target_ip': '209.67.4.2',
        'protocol': 'postgres_sql'
    }
    response = requests.post(url=url, auth=auth, json=json)
    print(response.content)
    assert response.status_code == 400


def test_post_authorized_no_target(url, auth):
    json = {
        'origin_ip': '209.67.4.2',
        'protocol': 'postgres_sql'
    }
    response = requests.post(url=url, auth=auth, json=json)
    print(response.content)
    assert response.status_code == 400


def test_post_authorized_invalid_ip(url, auth):
    json = {
        'origin_ip': '200.68.3.',
        'target_ip': '209.67.4.2',
        'protocol': 'postgres_sql'
    }
    response = requests.post(url=url, auth=auth, json=json)
    print(response.content)
    assert response.status_code == 400


def test_post_authorized_invalid_protocol(url, auth):
    json = {
        'origin_ip': '200.68.3.7',
        'target_ip': '209.67.4.2',
        'protocol': '158264'
    }
    response = requests.post(url=url, auth=auth, json=json)
    print(response.content)
    assert response.status_code == 400


def test_post_authorized_valid(url, auth):
    json = {
        'origin_ip': '200.68.3.7',
        'target_ip': '209.67.4.2',
        'protocol': 'postgres_sql'
    }
    response = requests.post(url=url, auth=auth, json=json)
    print(response.content)
    assert response.status_code == 200
