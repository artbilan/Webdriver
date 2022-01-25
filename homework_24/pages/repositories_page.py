from .base_page import BasePage


class Repositories(BasePage):
    def __init__(self, driver=None) -> None:
        super().__init__(driver)
        self.__title = "Repositories"

    def get_title(self) -> str:
        return self._get_title(self.__title)

