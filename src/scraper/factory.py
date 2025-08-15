from src.scraper.crm import CRMScraper

class ScraperFactory:
    @staticmethod
    def get_scraper(cr_type, headless=False):
        match cr_type.upper():
            case 'CRM':
                return CRMScraper(headless=headless)
            case _:
                return None