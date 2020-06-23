import pytest, time
from selenium.webdriver import Chrome


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
    driver.find_element_by_name('sex')

