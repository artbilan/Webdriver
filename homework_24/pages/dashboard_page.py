from .base_page import BasePage


class DashBoardPage(BasePage):
    def __init__(self, driver=None) -> None:
        super().__init__(driver)

        self._search_field = "/html/body/div[1]/header/div[3]/div/div/form/label/input[1]"
        self._overview = '/html/body/div[6]/main/div[1]/div/div/div[2]/div/nav/a[1]'
        self._repositories = '/html/body/div[6]/main/div[1]/div/div/div[2]/div/nav/a[2]'
        self._projects = '/html/body/div[6]/main/div[1]/div/div/div[2]/div/nav/a[3]'
        self._packages = '/html/body/div[6]/main/div[1]/div/div/div[2]/div/nav/a[4]'

    def select_repositories(self):
        self._click_on_element(self._repositories)

    def select_overview(self):
        self._click_on_element(self._overview)

    def select_projects(self):
        self._click_on_element(self._projects)

    def select_packages(self):
        self._click_on_element(self._packages)
