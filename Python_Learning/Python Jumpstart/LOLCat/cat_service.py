"""Cat service."""
import os
import requests
import shutil


def get_cat(folder, name):
    """Get the cat."""
    url = 'http://consuming-python-services-api.azurewebsites.net/cats/random'
    data = get_data_from_url(url)
    save_image(folder, name, data)


def get_data_from_url(url):
    """Get data from the url."""
    response = requests.get(url, stream=True)
    return response.raw


def save_image(folder, name, data):
    """Save image."""
    file_name = os.path.join(folder, name + '.jpg')
    with open(file_name, 'wb') as fout:
        shutil.copyfileobj(data, fout)
