"""
This module contains Sysdig Login Locators,
the page object for the Sysdig Login Locators.
"""
from selenium.webdriver.common.by import By

class ForgotPasswordLocators(object):
    
    EMAIL_INPUT = (By.XPATH, '//*[@data-test="forgot-password-username"]')
    REQUEST_PASSWORD_RESET_BUTTON = (By.XPATH, '//*[@data-test="submit-forgot-password"]')
    FEEDBACK_MESSAGE = (By.CLASS_NAME, 'login__feedback-message')
    LOGIN_LINK = (By.XPATH, '//a[contains(@href, "login")]')