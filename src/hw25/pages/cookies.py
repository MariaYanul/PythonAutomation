from dashboard_page import DashboardPage
from src.hw25.conftest import driver

class Cookies(DashboardPage):
    def __init__(self):
        self.__cookies = driver.get_cookies()

    def getting_cookie(self):
        print(driver.get_cookies())
        driver.add_cookie({"name": "access_token", "value": "test_token"})
        return print(driver.get_cookies())
