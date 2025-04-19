from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import WrongCredentials
from helper import generate_registration_data
from locators import Locators
from curl import *


class TestRegistrationWithNewCredentials:

    def test_success_registration(self, driver):
        name, email, password = generate_registration_data()
        driver.find_element(*Locators.LOG_IN_BUTTON).click()
        driver.find_element(*Locators.REG_TITLE).click()
        driver.find_element(*Locators.NAME_INPUT).send_keys(name)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        reg_text = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(Locators.MAIN_PAGE_TITLE, "Вход"))
        assert reg_text
        assert driver.current_url == main_site + 'login'


class TestCheckingCreationWithWrongCredentials:

    def test_failed_registration(self, driver):
        driver.find_element(*Locators.LOG_IN_BUTTON).click()
        driver.find_element(*Locators.REG_TITLE).click()
        driver.find_element(*Locators.NAME_INPUT).send_keys(WrongCredentials.name)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(WrongCredentials.email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(WrongCredentials.password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        reg_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.INVALID_PASSWORD_POPUP)).text
        assert reg_text == 'Некорректный пароль'
