
def test_check_search_field(dashboard_page):
    assert "Львові" in dashboard_page.find_new_city()



# ActionChains(driver).move_to_element(driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/p[17]/span')).perform()
# element: WebElement = driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/p[16]')
# element.click()
# sleep(1)
#
# element: WebElement = driver.find_element(By.XPATH, '/html/body/div[6]/div[16]/div/div/p[1]/span')
# element.click()
# sleep(1)


