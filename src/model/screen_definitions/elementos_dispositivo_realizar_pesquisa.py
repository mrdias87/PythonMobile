from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Elementos_Realizar_Pesquisa:

    def __init__(self, driver):
        self.driver = driver
        self.edit_text_search = WebDriverWait(self.driver.instance, 30).until(
            EC.presence_of_element_located((MobileBy.ID, 'br.com.petz:id/et_search')))
