# -*- encoding: utf-8 -*-
__author__ = 'GalaIO'
import requests

def download(url):
    response = requests.get(url)

    return response.content