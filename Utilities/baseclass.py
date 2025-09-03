import os
import pytest

from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("Invoke_Browser")
class Baseclass:

    def get_url(self):
        return self.driver.current_url
