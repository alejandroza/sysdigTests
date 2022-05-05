"""
This module contains Sysdig Login Page,
the page object for the Sysdig Login Page.
"""
from locators.forgot_password_locators import ForgotPasswordLocators
from selenium.webdriver.common.keys import Keys

class SysdigFotgotPasswordPage:

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    def enter_email_displayed(self):
        email_input = self.browser.find_element(*ForgotPasswordLocators.EMAIL_INPUT)
        return email_input.is_displayed()

    def enter_email(self, email):
        email_input = self.browser.find_element(*ForgotPasswordLocators.EMAIL_INPUT)
        email_input.send_keys(email + Keys.RETURN)

    def click_request_password_reset(self):
        forgot_password_button = self.browser.find_element(*ForgotPasswordLocators.REQUEST_PASSWORD_RESET_BUTTON)
        forgot_password_button.click()

    def feedback_message_displayed(self):
        feedback_message = self.browser.find_element(*ForgotPasswordLocators.FEEDBACK_MESSAGE)
        return feedback_message.is_displayed()
