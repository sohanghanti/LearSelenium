from selenium import webdriver

#page objects


url = 'http://www.thetestingworld.com/testings'
driver = webdriver.Chrome()
driver.maximize_window()

driver.get(url)
driver.find_element_by_name('fld_username').clear()
driver.find_element_by_name('fld_username').send_keys('testuser')

