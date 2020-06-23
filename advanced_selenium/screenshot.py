from selenium.webdriver import Chrome


driver = Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

url = 'http://www.thetestingworld.com/testings'
driver.get(url)

driver.get_screenshot_as_file('beforeRegistration.png')
