from src.scraper.crm import CRMScraper
from src.scraper.driver import Driver4Browser
from src.utils.logger import CallLogger

log = CallLogger().get()

def test_crm_scraper():
    driver = Driver4Browser()
    scraper = CRMScraper(driver)

    scraper.to_site()
    scraper.search_prescriber('159683')
    stts,name = scraper.verify_activity('159683', 'CLAUDIO')
    print(stts,name)
    data = scraper.collect_all_data()
    print(data)