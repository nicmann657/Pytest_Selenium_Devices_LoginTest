import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import *

@pytest.mark.usefixtures("driver")
class TestLoginPage:

    @pytest.mark.parametrize("username,password,passit", [("standard_user","secret_sauce",True),("locked_out_user","secret_sauce",False),
                                                   ("problem_user","secret_sauce",True),("performance_glitch_user","secret_sauce",True)])
    def test_login(self, driver,username,password,passit):

        driver.find_element(By.ID,"user-name").send_keys(username)
        driver.find_element(By.ID,"password").send_keys(password)
        driver.implicitly_wait(5)
        driver.find_element(By.ID, "login-button").click()

        wait = WebDriverWait(driver, 10)
        wait.until(presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))

        items = driver.find_elements(By.CLASS_NAME, "inventory_item")
        for i in items:
            assert i.is_visible()
            print(i.text)
