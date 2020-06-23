# when we know for how much time we should wait

from selenium.webdriver import Chrome
import pytest
import time


@pytest.fixture()
def setup():
    global driver
    driver = Chrome()
    driver.maximize_window()
    driver.set_page_load_timeout(1)
    yield
    driver.close()


@pytest.mark.Smoke
def test_launchApp(setup):
    url = 'http://www.thetestingworld.com/testings'
    driver.get(url)
    # time.sleep(20)

