from django.test import TestCase
import requests


def test_status():
    url = 'http://127.0.0.1:8000/post/1'
    response = requests.head(url)
    assert response == response.status_code == 200

