import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

driver = None


@pytest.fixture(scope="class")
def Invoke_Browser(request):
    global driver
    options = Options()

    options.add_experimental_option("detach", True)
    options.add_argument("--disable-notifications")
    options.add_argument('ignore-certificate-errors')
    options.add_argument("--disable-application-cache")
    options.add_argument("--incognito")

    options.add_argument("--disable-features=Notification")

    service_obj = Service()
    driver = webdriver.Chrome(service=service_obj, options=options)
    time.sleep(5)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.implicitly_wait(50)
    driver.maximize_window()
    time.sleep(1)
    request.cls.driver = driver
    yield
    driver.quit()


