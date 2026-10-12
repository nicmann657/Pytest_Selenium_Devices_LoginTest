from config import *
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("driver")
class Test_Login:
    USERS_LIST = [("standard_user", "secret_sauce"),
                  ("locked_out_user", "secret_sauce"),
                  ("problem_user", "secret_sauce"),
                  ("performance_glitch_user", "secret_sauce"),
                  ("error_user", "secret_sauce"),
                  ("visual_user", "secret_sauce")]
    DEVICES = [(414, 896),(430,932),(360,740)]

    @pytest.mark.parametrize("user_name,password", USERS_LIST)
    def test_login(self, driver, user_name, password):
        assert 'Swag Labs' in driver.title
        assert driver.find_element(By.ID, "user-name").is_enabled()
        assert driver.find_element(By.ID, "password").is_enabled()
        driver.find_element(By.ID,"user-name").send_keys(user_name)
        driver.find_element(By.ID,"password").send_keys(password)

        assert driver.find_element(By.ID, "login-button").is_enabled()

        driver.find_element(By.ID, "login-button").click()
        nextUrl = "https://www.saucedemo.com/inventory.html"
        load_time = driver.execute_script("return performance.timing.loadEventEnd - performance.timing.navigationStart") / 1000
        if load_time > 0.40:
            driver.save_screenshot(f"Test_Pages/Timing_Error/{user_name}.png")
            assert load_time < 0.40

        if nextUrl != driver.current_url:
            driver.save_screenshot(f"Test_Pages/Failed_Login/{user_name}.png")
            assert nextUrl in driver.current_url

    @pytest.mark.parametrize("user_name,password", USERS_LIST)
    @pytest.mark.parametrize("width,height", DEVICES)
    @pytest.mark.mobile
    def test_mobile_login(self, driver,user_name, password,width,height):
            # iPhone XR , iPhone 15 , Samsung Galaxy S8+
            assert 'Swag Labs' in driver.title
            driver.set_window_size(width,height)
            driver.find_element(By.ID, "user-name").send_keys(user_name)
            driver.find_element(By.ID, "password").send_keys(password)

            driver.find_element(By.ID, "login-button").click()

            nextUrl = "https://www.saucedemo.com/inventory.html"
            load_time = driver.execute_script(
                "return performance.timing.loadEventEnd - performance.timing.navigationStart") / 1000
            if load_time > 0.40:
                driver.save_screenshot(f"Test_Pages/Timing_Error/{user_name}.png")
                assert load_time < 0.40

            if nextUrl != driver.current_url:
                driver.save_screenshot(f"Test_Pages/Failed_Login/{user_name}.png")
                assert nextUrl in driver.current_url



