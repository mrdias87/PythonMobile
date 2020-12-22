from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Elementos_Seleciona_Produto:

    def __init__(self, driver):
        self.driver = driver
        self.element_menu_produto = WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located((
            MobileBy.XPATH,
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
            '.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout'
            '/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget'
            '.RelativeLayout[2]/androidx.viewpager.widget.ViewPager/android.widget.ImageView')))
