

from Object.homepage import Paths
from selenium.webdriver.support.ui import Select
from Utilities.baseclass import *


class TestSignUpStudent(Baseclass):

    def test_check_url(self):
        log = self.getLogger()
        log.info("----- %s -----" % self.get_url())
        assert "https://rahulshettyacademy.com/angularpractice/" == self.get_url()