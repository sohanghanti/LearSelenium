from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

url = 'http://www.thetestingworld.com/testings'

driver = Chrome()
driver.maximize_window()
driver.get(url)

driver.find_element_by_name('fld_username').send_keys('testuser')

# for keyboard actions
keyboard = ActionChains(driver)

# press tab key
keyboard.key_down(Keys.TAB).perform()

# ctrl +a
keyboard.key_down(Keys.CONTROL).send_keys('a').perform()
