from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import *
from locators import *


class TestLogInByLogInButton:

    def test_success_log_in_by_log_in_button(self, driver, login):
        assert WebDriverWait(driver, 10).until(EC.presence_of_element_located(LocatorsForLogIn.ORDER_BUTTON))


class TestLogInByPersonalAccountButton:

    def test_success_log_in_by_personal_account_button(self, driver):
        driver.find_element(*LocatorsForLogIn.PA_BUTTON).click()
        driver.find_element(*LocatorsForLogIn.EMAIL_INPUT_LOG_IN).send_keys(RightCredentials.email)
        driver.find_element(*LocatorsForLogIn.PASSWORD_INPUT_LOG_IN).send_keys(RightCredentials.password)
        driver.find_element(*LocatorsForLogIn.ENTER_BUTTON_CLICK).click()
        assert WebDriverWait(driver, 10).until(EC.presence_of_element_located(LocatorsForLogIn.ORDER_BUTTON))


class TestLogInByButtonInRegistrationForm:

    def test_success_log_in_by_button_in_registration_form(self, driver):
        driver.find_element(*LocatorsForLogIn.PA_BUTTON).click()
        driver.find_element(*Locators.REG_TITLE).click()
        driver.find_element(*LocatorsForLogIn.ENTER_TITLE).click()
        driver.find_element(*LocatorsForLogIn.EMAIL_INPUT_LOG_IN).send_keys(RightCredentials.email)
        driver.find_element(*LocatorsForLogIn.PASSWORD_INPUT_LOG_IN).send_keys(RightCredentials.password)
        driver.find_element(*LocatorsForLogIn.ENTER_BUTTON_CLICK).click()
        assert WebDriverWait(driver, 10).until(EC.presence_of_element_located(LocatorsForLogIn.ORDER_BUTTON))


class TestLogInByButtonInPasswordRecoveryForm:

    def test_success_log_in_by_button_in_password_recovery_form(self, driver):
        driver.find_element(*Locators.LOG_IN_BUTTON).click()
        driver.find_element(*LocatorsForLogIn.PASSWORD_RECOVERY_BUTTON).click()
        driver.find_element(*LocatorsForLogIn.ENTER_TITLE).click()
        driver.find_element(*LocatorsForLogIn.EMAIL_INPUT_LOG_IN).send_keys(RightCredentials.email)
        driver.find_element(*LocatorsForLogIn.PASSWORD_INPUT_LOG_IN).send_keys(RightCredentials.password)
        driver.find_element(*LocatorsForLogIn.ENTER_BUTTON_CLICK).click()
        assert WebDriverWait(driver, 10).until(EC.presence_of_element_located(LocatorsForLogIn.ORDER_BUTTON))
