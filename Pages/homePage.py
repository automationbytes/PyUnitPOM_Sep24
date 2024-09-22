from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Locators.locators import locators


class homePage():

    def __init__(self,driver):
        self.driver = driver


    def dropDownSelect(self,value):
        dropdown = Select(self.driver.find_element(By.XPATH,locators.sort_dropdown))
        dropdown.select_by_visible_text(value)

    def clickLogoutButton(self):
        self.driver.find_element(By.XPATH,locators.openMenu_webElement).click()
        self.driver.find_element(By.XPATH,locators.logout_webElement).click()


