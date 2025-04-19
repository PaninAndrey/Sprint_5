from selenium.webdriver.common.by import By


class Locators:
    # Локаторы для регистрации
    LOG_IN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]") # Кнопка "Войти в аккаунт" на главной странице
    REG_TITLE = (By.LINK_TEXT, "Зарегистрироваться") # Надпись "Зарегистрироваться" на странице входа в аккаунт
    NAME_INPUT = (By.XPATH, "//fieldset[1]/div/div/input[@class = 'text input__textfield text_type_main-default']") # Поле для ввода имени при регистрации
    EMAIL_INPUT = (By.XPATH, "//fieldset[2]/div/div/input[@class = 'text input__textfield text_type_main-default']") # Поле для ввода email при регистрации
    PASSWORD_INPUT = (By.XPATH, "//fieldset[3]/div/div/input[@class = 'text input__textfield text_type_main-default']") # Поле для ввода пароля при регистрации
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]") # Кнопка "Зарегистрироваться" при регистрации нового пользователя
    MAIN_PAGE_TITLE = (By.XPATH, "//h2") # Надпись "Вход" на странице после успешной регистрации
    INVALID_PASSWORD_POPUP = (By.XPATH, "//p[@class='input__error text_type_main-default']") # Всплывающая надпись при вводе невалидного пароля


class LocatorsForLogIn:
    # Локаторы для авторизации различными способами, переходов между окнами,
    # выхода из аккаунта и проверки раздела "Конструктор"
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]") # Кнопка "Оформить заказ" на главной странице после успешной авторизации
    EMAIL_INPUT_LOG_IN = (By.XPATH, "//fieldset[1]/div/div/input[@class = 'text input__textfield text_type_main-default']") # Поле для ввода email при авторизации
    PASSWORD_INPUT_LOG_IN = (By.XPATH, "//fieldset[2]/div/div/input[@class = 'text input__textfield text_type_main-default']") # Поле для ввода пароля при авторизации
    ENTER_TITLE = (By.LINK_TEXT, "Войти") # Надпись "Войти"
    PA_BUTTON = (By.LINK_TEXT, "Личный Кабинет") # Надпись "Личный кабинет"
    ENTER_BUTTON_CLICK = (By.XPATH, "//button[contains(text(), 'Войти')]") # Кнопка "Войти"
    PASSWORD_RECOVERY_BUTTON = (By.LINK_TEXT, "Восстановить пароль") # Надпись "Восстановить пароль"
    COMMON_TITLE = (By.XPATH, "//p[@class='Account_text__fZAIn text text_type_main-default']") # Надпись на странице после входа в личный кабинет
    CONSTRUCTOR_BUTTON = (By.LINK_TEXT, "Конструктор") # Кнопка "Конструктор"
    CONSTRUCTOR_WINDOW_TITLE = (By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10']") # Заголовок "Соберите бургер" на главной странице после авторизации
    LOGO_BUTTON = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']") # Кнопка логотипа
    LOG_OUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]") # Кнопка "Выход"
    ROLLS_BUTTON = (By.XPATH, "//span[contains(text(),'Булки')]") # Надпись для перехода в раздел "Булки"
    SAUCES_BUTTON = (By.XPATH, "//span[contains(text(),'Соусы')]") # Надпись для перехода в раздел "Соусы"
    TOPPINGS_BUTTON = (By.XPATH, "//span[contains(text(),'Начинки')]") # Надпись для перехода в раздел "Начинки"
    ROLLS_SECTION_TITLE = (By.XPATH, "//h2[contains(text(), 'Булки')]") # Заголовок раздела "Булки"
    SAUCES_SECTION_TITLE = (By.XPATH, "//h2[contains(text(), 'Соусы')]") # Заголовок раздела "Соусы"
    TOPPINGS_SECTION_TITLE = (By.XPATH, "//h2[contains(text(), 'Начинки')]") # Заголовок раздела "Начинки"