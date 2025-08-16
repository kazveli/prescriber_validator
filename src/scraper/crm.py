from .base import ScraperBase
from selenium.webdriver.common.by import By
from config import TIMEOUT_1, TIMEOUT_2
from src.utils.logger import CallLogger

log = CallLogger().get()

class CRMScraper(ScraperBase):
    def __init__(self, driver):
        super().__init__(driver) # Puxa o init do ScraperBase
    
    def to_site(self):
        self.driver.control.get("https://guiamedico.cremesp.org.br/")
        self.driver.visibility_element(TIMEOUT_1, (By.ID, 'crm'))
    
    def search_prescriber(self, crm):
        # Esperando os elementos necessários estarem presentes
        input_box_search = self.driver.element_clickable(TIMEOUT_1, (By.ID, 'crm'))
        button_query = self.driver.element_clickable(TIMEOUT_1, (By.CLASS_NAME, 'btn-crm'))
        # Percurso
        input_box_search.clear()
        input_box_search.send_keys(crm)
        input_box_search.send_keys('\t') # Impedir erro de inputs
        button_query.click()

    def verify_activity(self, crm, name):
        # Esperando a tabela de resultados aparecer
        line_primary_check = self.driver.visibility_element(TIMEOUT_1, (By.ID, 'DataTables_Table_0'))
        # Capturando todos os elementos que apareceram
        line_identity_regs = line_primary_check.find_elements(By.XPATH, '/tbody/tr')
        # Verificando linha por linha se algum registro é compatível
        for line in line_identity_regs:
            l_name = line.find_element(By.XPATH, '/td[1]').text
            l_stts = line.find_element(By.XPATH, '/td[2]').text
            l_crm = line.find_element(By.XPATH, '/td[3]').text
            if name in l_name and crm == l_crm:
                if l_stts.upper == 'ATIVO':
                    line.click() # Abre o modal que mostra as informações detalhadas
                    return True, l_name
                else:
                    return False, l_name
        return None, None

    def collect_all_data(self):
        # Esperando o modal aparecer
        modal_data = self.driver.visibility_element(TIMEOUT_1, (By.CSS_SELECTOR, '.modal.fade.center-modal.in.show'))
        # Puxando primeiro bloco de informações
        all_data = modal_data.find_element(By.CLASS_NAME, 'col-8')
        all_data = dict(i.split(': ',1) for i in all_data.strip().split('\n'))
        return all_data

    def close(self):
        self.driver.control.quit()

