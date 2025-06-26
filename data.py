import random

class UrlKey:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/api/'
    REG_URL = 'auth/register'
    AUTH_URL = 'auth/login'
    CHANGE_URL = 'auth/user'
    INGREDIENTS_URL = 'ingredients'
    ORDERS_URL = 'orders'
    ALL_ORDERS_URL = 'orders/all'
    LOG_OUT_URL = 'auth/logout'


class CreateUsers:

    EMAIL = f"numberOfMail{random.randint(1000, 100000)}@ya.ru"
    PASSWORD = str(random.randint(10, 100))
    NAME = "Ivan"