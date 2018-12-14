from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from values import strings
from webdriver import Driver
import allure
import string
import random


class TflxLogInScrn:

    def __init__(self, driver):
        self.driver = driver
        self.driver.navigate(strings.tflx_p_url)
        self.user_name_field = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.XPATH, ".//input[@id='username']")))
        self.password_field = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.XPATH, ".//input[@id='password']")))
        self.log_in_btn = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.XPATH, ".//button[@id='loginButton']")))


    def test_tflx_login(self):
        self.user_name_field.send_keys(strings.shared_un)
        self.password_field.send_keys(strings.shared_pw)
        self.log_in_btn.click()

        tflx_header = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.XPATH, ".//div[@id='mainheadercontainer']")))
        assert tflx_header.is_displayed()