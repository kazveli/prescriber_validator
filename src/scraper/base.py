from abc import ABC, abstractmethod
from .driver import Driver4Browser

class ScraperBase(ABC):
    def __init__(self, driver: Driver4Browser):
        self.driver = driver

    @abstractmethod
    def to_site(self):
        pass

    @abstractmethod
    def search_prescriber(self, crm):
        pass

    @abstractmethod
    def verify_activity(self):
        pass