from src.scraper.driver import Driver4Browser
from src.scraper.crm import CRMScraper
from src.utils.logger import CallLogger

# Inicializa o logger
log = CallLogger().get()

def test_browser():
    log.info("Iniciando..")
    driver = Driver4Browser()
    assert driver is not None
    log.info("Browser criado com sucesso")
    scrap = CRMScraper(driver)
    assert scrap is not None
    log.info("Scraper criado com sucesso")
    scrap.to_site()
    log.critical("Acesso ao site concedido")
    scrap.close()
    del driver