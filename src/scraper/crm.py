from .base import ScraperBase
from selenium.webdriver.common.by import By
from config import TIMEOUT_1, TIMEOUT_2
from src.utils.logger import logging

class CRMScraper(ScraperBase):
    def __init__(self, driver):
        super().__init__(driver) # Puxa o init do ScraperBase
    
    def to_site(self):
        self.driver.control.get("https://guiamedico.cremesp.org.br/")
        self.driver.visibility_element(TIMEOUT_1, (By.ID, 'crm'))
    
    def close(self):
        self.driver.control.quit()
