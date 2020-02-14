import pytest
import chromedriver_binary
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):
    url = "http://adactin.com/HotelApp/index.php"
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(url)
    request.cls.driver = driver
    yield
    driver.close()