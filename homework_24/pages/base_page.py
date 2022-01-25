from __future__ import annotations

from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from .singleton import Singleton


class BasePage(Singleton):
    def __init__(self, driver: Chrome = None) -> None:
        super().__init__(driver)
        self.wait = WebDriverWait(self._driver, 15)
        self.title_locator = "//div[@id='main']//h1"

    def _click_on_element(self, by: str) -> None:
        element = self.wait.until(ec.visibility_of_element_located((By.XPATH, by)))
        element.click()

    def _get_title(self, text: str) -> str:
        locator = f"{self.title_locator}[contains(text(), '{text}')]"
        return self.wait_element(locator).text

    def wait_element(self, locator: str) -> WebElement:
        return self.wait.until(ec.presence_of_element_located((By.XPATH, locator)))
