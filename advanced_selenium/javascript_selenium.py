# to perform any task on the things outside the web page i.e. browser like scrollbar, browser popup etc.
# we use javascript


from selenium.webdriver import Chrome


driver = Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
url = 'http://thetestingworld.com/testings'
driver.get(url)

# vertical scroll of 400 pixels
# javascript code of one line is entered#
# if we have two line separate the lines by semicolon

driver.execute_script("window.scrollTo(0,400);window.scrollTo(200,0);")

