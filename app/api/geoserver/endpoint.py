import json
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
        try:
            self.parent.get(self.path).json()
        except json.JSONDecodeError:
            return False
        else:
            return True

    def create(self):
        return self.exists()

    def get(self, sub_path: str = ''):
        if not self.exists():
            if not self.create():
                return abort(400, f"{self.path} could not be created")
        return self.parent.get(f"{self.path}/{sub_path}")

    def post(self, sub_path: str = '', data: dict = {}):
        if not self.exists():
            if not self.create():
                return abort('400', f"{self.name} does not exist")
        return self.parent.post(f"{self.path}/{sub_path}", data)
