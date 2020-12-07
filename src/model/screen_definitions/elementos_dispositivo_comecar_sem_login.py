from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Elementos_Comecar_Sem_Login:

    def __init__(self, driver):
        self.driver = driver
        self.tv_start_without_login = WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located((
            MobileBy.ID, 'br.com.petz:id/tv_start_without_login')))
