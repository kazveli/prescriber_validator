import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Driver4Browser:
    def __init__(self, headless=True, timeout=4):
        options = uc.ChromeOptions()
        if headless: # Verifica se o modo não supervisionado está ativo
            options.add_argument('--headless')
        self.control = uc.Chrome(options=options) # Cria o navegador com as opções do drivers
        self.control.maximize_window() # Ocupar todo o monitor e ampliar a visão do site

    # Aplicando funções de espera para o driver
    def visibility_element(self, select_time, element: tuple):
        return WebDriverWait(self.control, select_time).until(EC.visibility_of_element_located(element))
    
    def element_clickable(self, select_time, element: tuple):
        return WebDriverWait(self.control, select_time).until(EC.element_to_be_clickable(element))