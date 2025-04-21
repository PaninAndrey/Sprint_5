from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
import time

class TestConstructorSwitchToRollsSection:

    def test_success_switch_to_rolls_section(self, driver, login):
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(LocatorsForLogIn.SAUCES_BUTTON, "Соусы"))
        driver.find_element(*LocatorsForLogIn.SAUCES_BUTTON).click()
        driver.find_element(*LocatorsForLogIn.ROLLS_BUTTON).click()
        active_tab = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'tab_type_current')]/span[contains(text(),'Булки')]")))
        assert active_tab.is_displayed()


class TestConstructorSwitchToSaucesSection:

    def test_success_switch_to_sauces_section(self, driver, login):
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(LocatorsForLogIn.SAUCES_BUTTON, "Соусы"))
        driver.find_element(*LocatorsForLogIn.SAUCES_BUTTON).click()
        active_tab = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'tab_type_current')]/span[contains(text(),'Соусы')]")))
        assert active_tab.is_displayed()


class TestConstructorSwitchToToppingsSection:

    def test_success_switch_to_toppings_section(self, driver, login):
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(LocatorsForLogIn.TOPPINGS_BUTTON, "Начинки"))
        driver.find_element(*LocatorsForLogIn.TOPPINGS_BUTTON).click()
        active_tab = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'tab_type_current')]/span[contains(text(),'Начинки')]")))
        assert active_tab.is_displayed()





