"""
This module contains Sysdig Login Page,
the page object for the Sysdig Login Page.
"""
from locators.login_locators import LoginLocators
from selenium.webdriver.common.keys import Keys

class SysdigLoginPage:

    def __init__(self, browser):
        self.browser = browser

    def load(self, cluster):
        self.browser.get(cluster)

    def enter_email(self, email):
        email_input = self.browser.find_element(*LoginLocators.EMAIL_INPUT)
        email_input.send_keys(email + Keys.RETURN)

    def enter_password(self, password):
        password_input = self.browser.find_element(*LoginLocators.PASSWORD_INPUT)
        password_input.send_keys(password + Keys.RETURN)

    def click_login(self):
        login_button = self.browser.find_element(*LoginLocators.LOGIN_BUTTON)
        login_button.click()

    def error_message_displayed(self):
        login_error = self.browser.find_element(*LoginLocators.LOGIN_ERROR)
        return login_error.is_displayed()

    def click_forgot_password(self):
        forgot_password_link = self.browser.find_element(*LoginLocators.FORGOT_PASSWORD_LINK)
        forgot_password_link.click()

    def click_sign_up(self):
        sign_up_link = self.browser.find_element(*LoginLocators.SIGN_UP_LINK)
        sign_up_link.click()

    def click_google(self):
        google_button = self.browser.find_element(*LoginLocators.GOOGLE_BUTTON)
        google_button.click()

    def signin_with_google_displayed(self):
        signin_with_google_label = self.browser.find_element(*LoginLocators.SIGN_IN_WITH_GOOGLE_LABEL)
        return signin_with_google_label.is_displayed()

    def title(self):
        return self.browser.title
