from selenium.webdriver import Chrome
import pytest


@pytest.fixture()
def setup():
    global driver
    driver = Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    # yield
    # driver.close()


@pytest.mark.Smoke
def test_launchApp(setup):
    url = 'https://www.naukri.com'
    driver.get(url)
    allWindows = driver.window_handles
    print(allWindows)
    mainWindow = ''

    for win in allWindows:
        driver.switch_to.window(win)
        print(driver.current_url)
        if driver.current_url == 'https://www.naukri.com/':
            mainWindow = win
            break
        else:
            driver.close()

    driver.switch_to.window(mainWindow)
    print(driver.current_url)

