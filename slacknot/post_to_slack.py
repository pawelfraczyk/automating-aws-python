# coding: utf-8
import requests
url ='' # add slack channel here
data = {"text":"Hello, World!"}
requests.post(url, json=data)