import pytest
from selenium import webdriver
from utils.config import BASE_URL
from faker import Faker

@pytest.fixture
def faker():
    return Faker()

# Parameterize the browser and resolution via command line options
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on")
    parser.addoption("--width", action="store", default="1920", help="Browser window width")
    parser.addoption("--height", action="store", default="1080", help="Browser window height")

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    width = int(request.config.getoption("--width"))
    height = int(request.config.getoption("--height"))
    
    if browser.lower() == "chrome":
        driver = webdriver.Chrome()
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.set_window_size(width, height)
    driver.get(BASE_URL)
    yield driver
    driver.quit()


