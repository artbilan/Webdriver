import pytest
from selenium.webdriver import Chrome


@pytest.fixture(autouse=True)
def driver():
    driver = Chrome('../chromedriver/chromedriver.exe')
    driver.get("https://github.com/artbilan")
    yield
    driver.quit()
