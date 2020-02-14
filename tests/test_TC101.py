from time import sleep

from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass
from pagesObjects.LogInPage import LoginPage


class TestOne(BaseClass):

    def test_e2e(self):
        loginpage = LoginPage(self.driver)

        loginpage.enterUserName("seattletester")
        loginpage.enterPassword("Seattle123")
        loginpage.clickLoginButton()

