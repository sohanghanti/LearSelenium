from selenium import webdriver
from selenium.webdriver.support.select import Select


url='http://www.thetestingworld.com/testings'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

gender = Select(driver.find_element_by_name('sex'))
# gender.select_by_index(1)
# gender.select_by_value('1')

gender.select_by_visible_text('Male')


