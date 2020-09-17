from typing import Dict
from .logger import logger
from .endpoint import GeoserverEndpt
from .featuretype import GeoserverFeatureType


class GeoserverDatastore(GeoserverEndpt):
    """
    Geoserver PostGIS data store class, will try to create the
    datastore if it does not exist, but will return json error
    if it is not successful.  This allows the frontend to function
    independently from the datastore.
    """

    def __init__(
        self,
        parent,
        name: str,
        host: str,
        port: int,
        user: str,
        pwd: str,
    ) -> None:
        super().__init__(parent, 'datastores', name)
        self.name = name
        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd
        self.featuretypes = {}

    def create(self) -> bool:
        data = {"dataStore": {"name": self.name, "connectionParameters": {
            "entry": [
                {"@key": "host", "$": self.host},
                {"@key": "port", "$": self.port},
                {"@key": "database", "$": self.name},
                {"@key": "user", "$": self.user},
                {"@key": "passwd", "$": self.pwd},
                {"@key": "dbtype", "$": "postgis"}
            ]
        }}}
        response = self.parent.post(self.endpt, data=data)
        if response.status_code != 201:
            logger.error(f"could not create datastore {self.name} in {self.parent.name}")
            return False
        else:
            return True

    def featuretype(self, name: str, data: Dict) -> str:
        if not self.featuretypes.get(name):
            self.featuretypes[name] = GeoserverFeatureType(parent=self, name=name, data=data)
        return self.featuretypes[name]
