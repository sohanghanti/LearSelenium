from selenium import webdriver

url = 'http://www.thetestingworld.com/testings'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

driver.find_element_by_name('add_type').click()
driver.find_element_by_name('terms').click()  # checkbox
driver.find_element_by_class_name('displayPopup').click()  # link

driver.close()
driver.quit()
