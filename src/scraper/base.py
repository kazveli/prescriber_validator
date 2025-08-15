from abc import ABC, abstractmethod
from .driver import Driver4Browser

class ScraperBase(ABC):
    def __init__(self, driver: Driver4Browser):
        self.driver = driver

    @abstractmethod
    def to_site(self):
        pass