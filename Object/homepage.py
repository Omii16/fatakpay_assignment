from selenium.webdriver.common.by import By


class Paths:

    def __init__(self, driver):
        self.driver = driver

    enter_name = (By.XPATH, "//div[@class='form-group']//input[@name='name']")
    saved_validation_msg = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
    cancel_mark = (By.XPATH, "//a[normalize-space()='×']")
    name_validation = (By.XPATH, "//div[@class='alert alert-danger']")
    enter_email_id = (By.XPATH, "//input[@name='email']")
    enter_password = (By.XPATH, "//input[@id='exampleInputPassword1']")
    static_dropdown = (By.XPATH, "//select[@id='exampleFormControlSelect1']")
    select_checkbox = (By.XPATH, "//input[@id='exampleCheck1']")
    select_radio_button = (By.XPATH, "//input[@id='inlineRadio2']")

    def name(self):
        return self.driver.find_element(*Paths.enter_name)

    def save_msg(self):
        return self.driver.find_element(*Paths.saved_validation_msg)

    def cancel_toast_msg(self):
        return self.driver.find_element(*Paths.cancel_mark)

    def error_msg_name(self):
        return self.driver.find_element(*Paths.name_validation)

    def email_id(self):
        return self.driver.find_element(*Paths.enter_email_id)

    def password(self):
        return self.driver.find_element(*Paths.enter_password)

    def select_option(self):
        return self.driver.find_element(*Paths.static_dropdown)

    def click_checkbox(self):
        return self.driver.find_element(*Paths.select_checkbox)

    def click_radio_button(self):
        return self.driver.find_element(*Paths.select_radio_button)
