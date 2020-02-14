from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    #Locator
    userName = (By.NAME, "username") #data type Tuple
    password = (By.NAME, "password")
    loginButton = (By.NAME, "login")

    #Actions
    def getUserName(self):
        return self.driver.find_element(*LoginPage.userName) #data type is Tuple so have to use *

    def getPassword(self):
        return self.driver.find_element(*LoginPage.password)

    def getLoginButton(self):
        return self.driver.find_element(*LoginPage.loginButton)

    def enterUserName(self, username):
        self.getUserName().send_keys(username)

    def enterPassword(self, password):
        self.getPassword().send_keys(password)

    def clickLoginButton(self):
        self.getLoginButton().click()

    def login(self, username, password):
        self.enterUserName(username)
        self.enterPassword(password)
        self.clickLoginButton()

