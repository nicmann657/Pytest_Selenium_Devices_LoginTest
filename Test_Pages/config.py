import pytest

from selenium import webdriver


@pytest.fixture
def driver(request):

    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com")
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield driver
    driver.quit()
