from abc import ABC, abstractmethod
from typing import List, Tuple

from dora.store.models.incidents import (
    OrgIncidentService,
    IncidentsBookmark,
    Incident,
    IncidentOrgIncidentServiceMap,
)


class IncidentsProviderETLHandler(ABC):
    @abstractmethod
    def check_pat_validity(self) -> bool:
        """
        This method checks if the PAT is valid.
        :return: True if PAT is valid, False otherwise
        :raises: Exception if PAT is invalid
        """
        pass

    @abstractmethod
    def get_updated_incident_services(
        self, incident_services: List[OrgIncidentService]
    ) -> List[OrgIncidentService]:
        """
        This method returns the updated incident services.
        :param incident_services: List of incident services
        :return: List of updated incident services
        """
        pass

    @abstractmethod
    def process_service_incidents(
        self, incident_service: OrgIncidentService, bookmark: IncidentsBookmark
    ) -> Tuple[List[Incident], List[IncidentOrgIncidentServiceMap], IncidentsBookmark]:
        """
        This method processes the incidents for the incident services.
        :param incident_service: Incident service object
        :param bookmark: IncidentsBookmark object
        :return: Tuple of incidents, incident service map and incidents bookmark
        """
        pass
