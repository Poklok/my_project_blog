from django.test import TestCase
import requests


def get_status():
    url = 'http://127.0.0.1:8000/post/1'
    try:
        response = requests.head(url)
        if response and response.status_code == 200:
            print('url ok')
    except requests.ConnectionError:
        print("url not ok")
