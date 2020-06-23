from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

url = 'http://www.thetestingworld.com/testings'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

# object for mouse actions
mouse = ActionChains(driver)

# left click
mouse.click().perform()

# right click
mouse.context_click().perform()

# click on a particular element
mouse.click(driver.find_element_by_xpath("//a(text()='Login')")).perform()

# double click
mouse.double_click().perform()

# mouse hover
mouse.move_to_element(driver.find_element_by_xpath("//span(contains(text(),'TUTORIAL')")).perform()
mouse.key_up()