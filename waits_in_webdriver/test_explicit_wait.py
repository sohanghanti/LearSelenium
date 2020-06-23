import pytest, time
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.common.by import By


@pytest.fixture()
def setup():
    global driver
    driver = Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield
    driver.close()


@pytest.mark.Smoke
def test_launch_app(setup):
    url = 'http://www.thetestingworld.com/testings'
    driver.get(url)

    wait = WebDriverWait(driver, 100)
    wait.until(ec.text_to_be_present_in_element(By.NAME, 'sex'), 'Male')

    gender = Select(driver.find_element_by_name('sex'))
    gender.select_by_visible_text('Male')












