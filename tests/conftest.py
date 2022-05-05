"""
This module contains shared fixtures.
"""
import pytest
import selenium.webdriver

clusters = [
    ('https://eu1.app.sysdig.com/#/login'),
    ('https://app.sysdigcloud.com/#/login'),
    ('https://us2.app.sysdig.com/#/login'),
    ('https://app.au1.sysdig.com/#/login')
]

@pytest.fixture
def browser():
  # Initialize the ChromeDriver instance
  driver = selenium.webdriver.Chrome(executable_path='C:\\Selenium\\chromedriver.exe')
  # Make its calls wait up to 10 seconds for elements to appear
  driver.implicitly_wait(10)
  # Return the WebDriver instance for the setup
  yield driver
  # Quit the WebDriver instance for the cleanup
  driver.quit()