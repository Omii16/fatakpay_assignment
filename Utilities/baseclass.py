import os
import pytest


@pytest.mark.usefixtures("Invoke_Browser")
class Baseclass:

    def get_url(self):
        return self.driver.current_url

    def clear_field(self, inp):
        self.driver.execute_script("arguments[0].value = '';", inp)

    def scroll_down(self, x, y):
        return self.driver.execute_script("window.scrollBy(arguments[0], arguments[1]);", x, y)
