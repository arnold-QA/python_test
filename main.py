import time
import data

from selenium import webdriver
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from helpers import is_url_reachable

class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        # Configura o Chrome com logging para capturar o código do SMS
        options = Options()
        options.set_capability("goog:loggingPrefs",{"performance": "ALL"})
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        cls.driver.implicitly_wait(5)

    def test_set_route(self):

        if is_url_reachable(data.URBAN_ROUTES_URL):
           print("Conectado ao servidor Urban Routes")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado ainda em execução")
        self.driver.get(data.URBAN_ROUTES_URL)
        time.sleep(10)

    def test_select_plan(self):
        # Adicionar em S8
        print("Função criada para selecionar o plano")
        pass

    def test_fill_phone_number(self):
        # Adicionar em S8
        print("Função criada para preencher o número de telefone")
        pass

    def test_fill_card(self):
        # Adicionar em S8
        print("Função criada para preencher o cartão")
        pass

    def test_comment_for_driver(self):
        # Adicionar em S8
        print("Função criada para adicionar comentário ao motorista")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Adicionar em S8
        print("Função criada para pedir cobertor e lenços")
        pass

    def test_order_2_ice_creams(self):
        # Adicionar em S8
        print("Função criada para pedir sorvete")
        for i in range(2):
            # Adicionar em S8
            pass

    def test_car_search_model_appears(self):
        # Adicionar em S8
        print("Função criada para verificar se o modelo do carro aparece")
        pass