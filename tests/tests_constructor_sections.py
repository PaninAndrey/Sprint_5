from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import *
from locators import *


class TestConstructorSwitchToRollsSection:

    def test_success_switch_to_rolls_section(self, driver, login):
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(LocatorsForLogIn.SAUCES_BUTTON, "Соусы"))
        driver.find_element(*LocatorsForLogIn.SAUCES_BUTTON).click()
        driver.find_element(*LocatorsForLogIn.ROLLS_BUTTON).click()
        rolls_title = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(LocatorsForLogIn.ROLLS_SECTION_TITLE, "Булки"))
        assert rolls_title


class TestConstructorSwitchToSaucesSection:

    def test_success_switch_to_sauces_section(self, driver, login):
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(LocatorsForLogIn.SAUCES_BUTTON, "Соусы"))
        driver.find_element(*LocatorsForLogIn.SAUCES_BUTTON).click()
        sauces_title = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(LocatorsForLogIn.SAUCES_SECTION_TITLE, "Соусы"))
        assert sauces_title


class TestConstructorSwitchToToppingsSection:

    def test_success_switch_to_toppings_section(self, driver, login):
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(LocatorsForLogIn.TOPPINGS_BUTTON, "Начинки"))
        driver.find_element(*LocatorsForLogIn.TOPPINGS_BUTTON).click()
        toppings_title = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(LocatorsForLogIn.TOPPINGS_SECTION_TITLE, "Начинки"))
        assert toppings_title





