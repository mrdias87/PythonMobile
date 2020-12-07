from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Elementos_Ir_Carrinho:

    def __init__(self, driver):
        self.driver = driver
        self.relativelayout_go_to_shop = WebDriverWait(self.driver.instance, 30).until(
            EC.presence_of_element_located((MobileBy.ID, 'br.com.petz:id/rl_go_to_shopping_cart')))
