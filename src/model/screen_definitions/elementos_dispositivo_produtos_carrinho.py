from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Elementos_Produtos_Carrinho:

    def __init__(self, driver):
        self.driver = driver
        self.textviewer_nome_produto = WebDriverWait(self.driver.instance, 30).until(
            EC.presence_of_element_located((MobileBy.ID, 'br.com.petz:id/tv_prod_name')))
        self.textview_nome_fornecedor = WebDriverWait(self.driver.instance, 30).until(
            EC.presence_of_element_located((MobileBy.ID, 'br.com.petz:id/tv_prod_name')))
        self.textviewer_preco_produto = WebDriverWait(self.driver.instance, 30).until(
            EC.presence_of_element_located((MobileBy.ID, 'br.com.petz:id/tv_prod_main_price')))
        

