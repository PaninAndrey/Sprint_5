from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Wrong_Credentials
from helper import generate_registration_data
from locators import Locators
from curl import *
import time

class TestRegistrationWithNewCredentials:

    def test_sucsess_registration(self, driver):
        name, email, password = generate_registration_data()
        driver.find_element(*Locators.PA_BUTTON).click()
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.NAME_FIELD).click()
        driver.find_element(*Locators.NAME_INPUT).send_keys(name)
        driver.find_element(*Locators.EMAIL_FIELD).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FIELD).click()
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        time.sleep(2)
        reg_text = driver.find_element(*Locators.REG_TITLE).text

        assert reg_text == 'Вход'
        assert driver.current_url == main_site + 'login'

class TestCheckingCreationWithWrongCredentials:

    def test_failed_registration(self, driver):
        driver.find_element(*Locators.PA_BUTTON).click()
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.NAME_FIELD).click()
        driver.find_element(*Locators.NAME_INPUT).send_keys(Wrong_Credentials.name)
        driver.find_element(*Locators.EMAIL_FIELD).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(Wrong_Credentials.email)
        driver.find_element(*Locators.PASSWORD_FIELD).click()
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Wrong_Credentials.password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        reg_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.INVALID_PASSWORD_POPUP)).text
        assert reg_text == 'Некорректный пароль'
