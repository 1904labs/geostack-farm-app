import json
from .logger import logger
from flask import abort


class GeoserverEndpt(object):
    """
    Base class for geoserver rest api endpoitns
    """

    def __init__(self, parent, endpt: str, name: str) -> None:
        self.parent = parent
        self.endpt = endpt
        self.name = name
        self.path = f"{endpt}/{name}"

    def exists(self) -> bool:
        response = self.parent.get(self.path)
        if response.status_code != 200:
            return False
        else:
            return True

    def create(self):
        return self.exists()

    def get(self, sub_path: str = ''):
        if not self.exists():
            if not self.create():
                return abort(400, f"{self.path} could not be created")
        path = f"{self.path}/{sub_path}" if sub_path else self.path
        return self.parent.get(path)

    def post(self, sub_path: str = '', data: dict = {}):
        if not self.exists():
            if not self.create():
                return abort('400', f"{self.name} does not exist")
        path = f"{self.path}/{sub_path}" if sub_path else self.path
        return self.parent.post(path, data)
