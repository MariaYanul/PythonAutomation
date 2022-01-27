from time import sleep
from selenium.webdriver import Chrome

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains


driver = Chrome("./chromedriver.exe")
driver.get("https://multiplex.ua/")
driver.maximize_window()
sleep(3)

element: WebElement = driver.find_element(By.XPATH, '//*[@id="tocinemas"]/div')
element.click()
sleep(1)

ActionChains(driver).move_to_element(driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/p[17]/span')).perform()
element: WebElement = driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/p[16]')
element.click()
sleep(1)

element: WebElement = driver.find_element(By.XPATH, '/html/body/div[6]/div[16]/div/div/p[1]/span')
element.click()
sleep(1)

driver.quit()


# from time import sleep
# from selenium.webdriver import Chrome
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.common.action_chains import ActionChains
#
# search_field = '//*[@id="search_city"]'
# search_button = '//*[@id="form-search"]/p[1]/input[2]'
#
# driver = Chrome("./chromedriver.exe")
# driver.get("https://ua.sinoptik.ua/")
# driver.maximize_window()
# sleep(3)
#
# element: WebElement = driver.find_element(By.XPATH, search_field)
# element.send_keys('Львів')
# sleep(1)
#
# element: WebElement = driver.find_element(By.XPATH, search_button)
# element.click()
# sleep(2)

# ActionChains(driver).move_to_element(driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/p[17]/span')).perform()
# element: WebElement = driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/p[16]')
# element.click()
# sleep(1)
#
# element: WebElement = driver.find_element(By.XPATH, '/html/body/div[6]/div[16]/div/div/p[1]/span')
# element.click()
# sleep(1)

# driver.quit()
