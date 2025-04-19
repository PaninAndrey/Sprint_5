import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from curl import *
from data import RightCredentials
from locators import *


# Фикстура для запуска браузера и закрытия окна
# браузера после выполнения теста

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--window-size=1200,600")
    browser = webdriver.Chrome(options=options)
    browser.get(main_site)
    yield browser
    browser.quit()


# Фикстура для авторизации зарегистрированного пользователя:

@pytest.fixture
def login(driver):
    driver.find_element(*Locators.LOG_IN_BUTTON).click()
    driver.find_element(*LocatorsForLogIn.EMAIL_INPUT_LOG_IN).send_keys(RightCredentials.email)
    driver.find_element(*LocatorsForLogIn.PASSWORD_INPUT_LOG_IN).send_keys(RightCredentials.password)
    driver.find_element(*LocatorsForLogIn.ENTER_BUTTON_CLICK).click()
    return driver
