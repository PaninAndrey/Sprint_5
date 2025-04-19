from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import *
from locators import *

class TestConstructorSwitchToRollsSection:

    def test_success_switch_to_rolls_section(self, driver):
        driver.find_element(*LocatorsForLogIn.LOG_IN_BUTTON).click()
        driver.find_element(*LocatorsForLogIn.EMAIL_FIELD_LOG_IN).click()
        driver.find_element(*LocatorsForLogIn.EMAIL_INPUT_LOG_IN).send_keys(Right_Credentials.email)
        driver.find_element(*LocatorsForLogIn.PASSWORD_FIELD_LOG_IN).click()
        driver.find_element(*LocatorsForLogIn.PASSWORD_INPUT_LOG_IN).send_keys(Right_Credentials.password)
        driver.find_element(*LocatorsForLogIn.REGISTER_BUTTON).click()
        log_in_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LocatorsForLogIn.ORDER_BUTTON)).text
        assert log_in_text == 'Оформить заказ'

