import time
import unittest
#pip install HTMLTestRunner-rv
from selenium import webdriver

from Pages import loginPage
from Pages import homePage
from Util.logger import get_logger
logger = get_logger(__name__)
from HTMLTestRunner.runner import HTMLTestRunner


class testUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)
        cls.driver.get("https://www.saucedemo.com/")
        logger.info("URL is launched")


    def setUp(self):
        login = loginPage.loginPage(self.driver)
        login.enterUserName("standard_user")
        login.enterPassword("secret_sauce")
        login.clickLoginButton()
        logger.info("Login is completed")

    def test_a_SortZtoA(self):
        home = homePage.homePage(self.driver)
        home.dropDownSelect("Name (Z to A)")
        time.sleep(10)
        home.clickLogoutButton()
        logger.info("Sorted in Z to A")

    def test_b_SortLowtoHigh(self):
        home = homePage.homePage(self.driver)
        home.dropDownSelect("Price (low to high)")
        logger.info("Sorted in Low to High")
        time.sleep(10)
        home.clickLogoutButton()

if __name__ == '__main__':
    runner = HTMLTestRunner(log=True, verbosity=2, output='report', title='Test report', report_name='report',
                            open_in_browser=True, description="HTMLTestReport", tested_by="Vignesh",
                            add_traceback=False)
    unittest.main(testRunner=runner)