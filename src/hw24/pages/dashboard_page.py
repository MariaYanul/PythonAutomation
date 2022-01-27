from __future__ import annotations

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:
    def __init__(self, driver: Chrome) -> None:
        self.__driver = driver
        self.__wait = WebDriverWait(driver, 5)
        self.__search_field_locator = '//*[@id="search_city"]'
        self.__search_button_locator = '//*[@id="form-search"]/p[1]/input[2]'
        self.__results_search_lviv_locator = '//*[@id="header"]/div[4]/h1/strong'

    def find_new_city(self) -> DashboardPage:
        search_field = self.__driver.find_element(By.XPATH, self.__search_field_locator)
        search_field.send_keys('Львів')

        search_button = self.__driver.find_element(By.XPATH, self.__search_button_locator)
        search_button.click()

        search_result = self.__wait.until(
            EC.visibility_of_element_located(self.__results_search_lviv_locator)
        )

        return search_result
