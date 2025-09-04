import time

from selenium.webdriver.common import keys
from Object.homepage import Paths
from selenium.webdriver.support.ui import Select
from Utilities.baseclass import *


class Assignment(Baseclass):

    def test_check_url_link(self):
        log = self.getLogger()
        log.info("----- %s -----" % self.get_url())
        assert "https://rahulshettyacademy.com/angularpractice/" == self.get_url()

    def test_add_input_field(self):
        obj = Paths(self.driver)
        obj.name().send_keys("O")
        obj.name().send_keys(keys.ENTER)
        saved_msg = obj.save_msg().text()
        assert saved_msg == "Success! The Form has been submitted successfully!."

    def test_check_validation_input_field(self):
        obj = Paths(self.driver)
        obj.cancel_toast_msg().click()
        error_msg = obj.error_msg_name().text()
        assert error_msg == "Name should be at least 2 characters", f"Unexpected error: {error_msg}"
        self.clear_field(obj.name())
        time.sleep(2)

    def test_edit_input_field(self):
        obj = Paths(self.driver)
        self.clear_field(obj.name())
        time.sleep(1)
        obj.name().send_keys("Omkar")
        obj.name().send_keys(keys.ENTER)
        saved_msg = obj.save_msg().text()
        assert saved_msg == "Success! The Form has been submitted successfully!."

    def test_add_other_input_field(self):
        obj = Paths(self.driver)
        obj.email_id().send_keys("ohtester16@gmail.com")
        obj.password().send_keys("Abc@123")

    def test_select_checkbox(self):
        obj = Paths(self.driver)
        obj.click_checkbox().click()

    def test_handle_static_dropdown(self):
        obj = Paths(self.driver)
        self.scroll_down(0, 300)
        dropdown = Select(obj.select_option())
        dropdown.select_by_visible_text("Female")
        print("Successfully select.")

    def select_radio_button(self):
        obj = Paths(self.driver)
        radio_btn = obj.click_radio_button()
        radio_btn.click()
        assert radio_btn.is_selected()

