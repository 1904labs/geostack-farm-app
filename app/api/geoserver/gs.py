import requests
from flask import abort
from .logger import logger
from .workspace import GeoserverWorkspace


class Geoserver(object):
    """
    allows geoserver to be defined but if connection fails it will return
    errors as json instead of croaking
    """

    def __init__(self, url: str, username: str, password: str) -> None:
        self.base = url
        self.url = f"{url}/rest"
        self.username = username
        self.password = password
        self.workspaces = {}

    def is_alive(self) -> bool:
        try:
            requests.get(self.url, auth=(self.username, self.password))
        except Exception:
            return False
        else:
            return True

    def workspace(self, name):
        if not self.workspaces.get(name):
            self.workspaces[name] = GeoserverWorkspace(parent=self, name=name)
        return self.workspaces[name]

    def get(self, path: str = '') -> str:
        if not self.is_alive():
            return abort(400, f"{self.url} is offline")
        url = f"{self.url}/{path}"
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        response = requests.get(
            url,
            headers=headers,
            auth=(self.username, self.password)
        )
        return response

    def post(self, path: str, data: dict) -> str:
        if not self.is_alive():
            return abort(400, f"{self.url} is offline")
        url = f"{self.url}/{path}"
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        response = requests.post(
            url, json=data,
            headers=headers,
            auth=(self.username, self.password))
        return response
