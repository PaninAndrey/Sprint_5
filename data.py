# Создаём класс для проверки появления ошибки
# при вводе невалидного пароля (пять символов)

class WrongCredentials:
    name='Геннадий'
    email='fortunteller_666@yandex.ru'
    password='22!!2'


# Создаём класс с валидными данными пользователя для авторизации

class RightCredentials:
    name='Андрей'
    email='panin_andrey_21_677@yandex.ru'
    password = '37!!99A'

timeout = 20
