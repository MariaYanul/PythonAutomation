import pytest
from selenium.webdriver import Chrome
from src.hw24.pages.dashboard_page import DashboardPage

@pytest.fixture(scope="session")
def driver() -> Chrome:
    driver = Chrome("core/infrastructure/bin/chromedriver.exe")
    driver.get("https://ua.sinoptik.ua/")
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def dashboard_page(driver):
    yield DashboardPage(driver)
