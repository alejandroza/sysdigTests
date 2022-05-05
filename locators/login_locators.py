"""
This module contains Sysdig Login Locators,
the page object for the Sysdig Login Locators.
"""
from selenium.webdriver.common.by import By

class LoginLocators(object):
    
    EMAIL_INPUT = (By.ID, 'ember1642')
    PASSWORD_INPUT = (By.ID, 'ember1643')
    LOGIN_BUTTON = (By.ID, 'ember1652')
    LOGIN_ERROR = (By.CLASS_NAME, 'login__error-display')
    FORGOT_PASSWORD_LINK = (By.ID, 'ember1656')
    SIGN_UP_LINK = (By.XPATH, '//a[@href="https://sysdig.com/sign-up/"]')
    GOOGLE_BUTTON = (By.XPATH, '//a[contains(@href,"/api/oauth/google?")]')

    #Pending to move this following locator
    SIGN_IN_WITH_GOOGLE_LABEL = (By.XPATH, '//div[text()=("Sign in with Google") or ("Acceder con Google")]')