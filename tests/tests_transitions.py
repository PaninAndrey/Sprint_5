from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *


class TestTransitionToPersonalAccount:

    def test_success_transition_to_personal_account(self, driver, login):
        driver.find_element(*LocatorsForLogIn.PA_BUTTON).click()
        personal_account_text = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(LocatorsForLogIn.COMMON_TITLE, "В этом разделе вы можете изменить свои персональные данные"))
        assert personal_account_text


class TestTransitionToConstructorWindowByConstructorButton:

    def test_success_transition_to_constructor_window_by_constructor_button(self, driver, login):
        driver.find_element(*LocatorsForLogIn.PA_BUTTON).click()
        driver.find_element(*LocatorsForLogIn.CONSTRUCTOR_BUTTON).click()
        constructor_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LocatorsForLogIn.CONSTRUCTOR_WINDOW_TITLE)).text
        assert constructor_text == 'Соберите бургер'


class TestTransitionToConstructorWindowByLogoButton:

    def test_success_transition_to_constructor_window_by_logo_button(self, driver, login):
        driver.find_element(*LocatorsForLogIn.PA_BUTTON).click()
        driver.find_element(*LocatorsForLogIn.LOGO_BUTTON).click()
        constructor_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LocatorsForLogIn.CONSTRUCTOR_WINDOW_TITLE)).text
        assert constructor_text == 'Соберите бургер'


class TestLogOut:

    def test_success_log_out(self, driver, login):
        driver.find_element(*LocatorsForLogIn.PA_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LocatorsForLogIn.LOG_OUT_BUTTON)).click()
        log_out_text = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(Locators.MAIN_PAGE_TITLE, "Вход"))
        assert log_out_text
