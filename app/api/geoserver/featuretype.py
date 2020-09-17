from typing import Dict
from .logger import logger
from .endpoint import GeoserverEndpt


class GeoserverFeatureType(GeoserverEndpt):
    """
    """

    def __init__(
        self,
        parent,
        name: str,
        data: Dict
    ) -> None:
        super().__init__(parent, 'featuretypes', name)
        self.data = data
        self.data['name'] = name

    def create(self) -> bool:
        logger.error(f"attempting to create {self.data}")
        response = self.parent.post(self.endpt, data=self.data)
        if response.status_code != 201:
            logger.error(f"could not create datastore {self.name} in {self.parent.name}")
            return False
        else:
            return True
