from selenium.webdriver.common.by import By

from Locators.locators import locators


class loginPage():

    def __init__(self,driver):
        self.driver = driver





    def enterUserName(self,username):
        self.driver.find_element(By.XPATH,locators.username_inputbox).send_keys(username)

    def enterPassword(self,password):
        self.driver.find_element(By.XPATH,locators.password_inputbox).send_keys(password)


    def clickLoginButton(self):
        self.driver.find_element(By.XPATH,locators.login_button).click()

