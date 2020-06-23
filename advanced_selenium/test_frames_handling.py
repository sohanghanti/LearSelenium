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
def test_frame_handles(setup):
    url = 'https://www.toolsqa.com/iframe-practice-page/'
    driver.get(url)

    # control to frame
    driver.switch_to.frame("iframe2")
    driver.find_element_by_xpath('//a[contains(text(), "Read more")]').click()

    # control back to the parent window
    driver.switch_to.default_content()
    driver.find_element_by_xpath('//span[text()= "VIDEOS"]').click()
