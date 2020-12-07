from appium import webdriver


class Driver:

    def __init__(self):
        desired_cap = dict(
            automationName='UiAutomator2',
            platformName='Android',
            deviceName='GCAZB6010134RCH',
            appPackage='br.com.petz',
            appActivity='br.com.hanzo.petz.view.MainActivity',
            autoGrantPermissions=True
            # noReset=True,
            # fullReset=False
        )

        self.instance = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)