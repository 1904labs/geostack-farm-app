from .logger import logger
from .endpoint import GeoserverEndpt
from .datastore import GeoserverDatastore


class GeoserverWorkspace(GeoserverEndpt):
    """
    Geoserver workspace class, will try to create the workspace
    if it does not exist, but will return json error if it is
    not successful.  This allows the frontend to function
    independently from geoserver.
    """

    def __init__(self, parent, name: str) -> None:
        super().__init__(parent, 'workspaces', name)
        self.datastores = {}

    def create(self) -> str:
        data = {"workspace": {"name": self.name}}
        response = self.parent.post(self.endpt, data=data)
        if response.status_code == 201:
            return True
        else:
            return False

    def pg_datastore(self, name: str, host: str, port: int, user: str, pwd: str) -> str:
        if not self.datastores.get(name):
            self.datastores[name] = GeoserverDatastore(
                parent=self, name=name, host=host, port=port, user=user, pwd=pwd)
        return self.datastores[name]
