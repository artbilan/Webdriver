from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep


def test_01():
    exp_url = "https://github.com/artbilan/Hilel"
    driver = Chrome("C:\\Users\\Art\\PycharmProjects\\main\\venv\\chromedriver\\chromedriver.exe")
    driver.get("https://github.com/artbilan?tab=repositories")
    driver.maximize_window()
    sleep(3)
    search_button = driver.find_element(By.XPATH, '//a[@href="/artbilan/Hilel"]')
    search_button.click()
    sleep(3)
    result_url = driver.current_url
    driver.minimize_window()
    sleep(3)
    driver.close()
    assert result_url == exp_url










