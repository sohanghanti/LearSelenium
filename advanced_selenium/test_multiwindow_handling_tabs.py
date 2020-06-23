from selenium.webdriver import Chrome
import pytest


@pytest.fixture()
def setup():
    global driver
    driver = Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield
    driver.close()


@pytest.mark.Smoke
def test_popup_window_handling_tabs(setup):
    url = 'http://www.thetestingworld.com/testings/'
    driver.get(url)
    print(driver.current_url)

    driver.find_element_by_xpath('//label[text()="Login"]').click()
    print('Login tab clicked')
    driver.find_element_by_name('_txtUserName').send_keys('test')
    driver.find_element_by_name('_txtPassword').send_keys('test')
    driver.find_element_by_xpath('//input[@type = "submit" and @value="Login"]').click()

    # allTabs = driver.window_handles
    # print(allTabs)
    # myTab = ''
    # for tab in allTabs:
    #     driver.switch_to.window(tab)

    tabURL = driver.current_url
    print(tabURL)
    if tabURL == 'https://www.thetestingworld.com/testings/dashboard.php':
        print(driver.current_url)
        # myTab = driver.current_url

    # driver.switch_to.window(myTab)
    # print(driver.current_url)
