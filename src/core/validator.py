from src.scraper.factory import ScraperFactory
from src.data.loader import DataLoader
from src.utils.logger import CallLogger

log = CallLogger().get() # Chama a única instância do logger

class Validator:
    def __init__(self, filepath, cr_type=None, auto=False, headless=False):
        self.filepath = filepath
        self.cr_type = cr_type
        self.auto = auto
        self.headless = headless
        self.scraper = None
        self.data = None

    def load_data(self):
        log.info("Carregando dados da planilha excel.")
        self.data = DataLoader(self.filepath,skiprows=1).load()
        log.info(f"{len(self.data)} registros encontrados.")

    def select_scraper(self):
        if self.auto:
            log.info("Modo automático. Será utilizado todos os scrapers.")
            self.scraper = None
        else:
            self.scraper = ScraperFactory.get_scraper(self.cr_type, headless=self.headless)
            if self.scraper is None:
                raise ValueError(f"Tipo de CR '{self.cr_type}' não suportado.")
    
    def validate(self):
        log.info('Iniciando validação.')
        for row in self.data.itertuples(index=False):
            
            pass

    def run(self):
        self.load_data()
        self.select_scraper()
        self.validate()
        log.info('Processo finalizado.')