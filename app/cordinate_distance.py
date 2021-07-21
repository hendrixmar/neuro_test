from flask import Blueprint
import numpy as np
import urllib.request
import os

example_blueprint = Blueprint('example_blueprint', __name__)
API_KEY = os.environ.get('API_YANDEX_KEY', None)

def haversine_distance(lat1, lon1, lat2, lon2):
    r = 6371
    phi1 = np.radians(lat1)
    phi2 = np.radians(lat2)
    delta_phi = np.radians(lat2 - lat1)
    delta_lambda = np.radians(lon2 - lon1)
    a = np.sin(delta_phi / 2) ** 2 + np.cos(phi1) * np.cos(phi2) * np.sin(delta_lambda / 2) ** 2
    res = r * (2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a)))
    return np.round(res, 2)


@example_blueprint.route('/distance/<address>')
def index(address : str):

    ADDRESS = address.replace(" ", "+")

    contents = urllib.request.urlopen(
        f"https://geocode-maps.yandex.ru/1.x/?apikey={API_KEY}&geocode={ADDRESS}&lang=en-US&format=json").read()
    return contents