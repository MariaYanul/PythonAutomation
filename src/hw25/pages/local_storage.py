from dashboard_page import DashboardPage
from src.hw25.conftest import driver

class LocalStorage(DashboardPage):
    def __init__(self):
        self.__local_storage = driver.execute_script()

    def getting_cookie(self):
        driver.execute_script("window.localStorage['access_token'] = 'test_token';")
        return print(driver.execute_script("return window.localStorage;"))
