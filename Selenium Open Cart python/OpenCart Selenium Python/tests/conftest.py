import pytest
from selenium import webdriver
import string

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver

####### HTML REPORT ##########

def pytest_configure(config):
    config._metadata = {
        "Project Name": "Open Cart",
        "Module Name": "Customers",
        "Tester":"Srivardhan"
    }

# It is hook for delete/Modify Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)