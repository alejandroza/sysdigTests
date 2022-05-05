"""
These tests cover the Login page and its features.
"""
import pytest
from conftest import clusters
from pages.login_page import SysdigLoginPage
from pages.forgot_password_page import SysdigFotgotPasswordPage


@pytest.mark.parametrize('cluster', clusters)
@pytest.mark.ui_tests
def test_login_with_invalid_credentials(browser, cluster):
  login_page = SysdigLoginPage(browser)

  login_page.load(cluster)
  login_page.enter_email('test@sysdig.com')
  login_page.enter_password('12345')
  login_page.click_login()
  assert login_page.error_message_displayed() == True

@pytest.mark.parametrize('cluster', clusters)
@pytest.mark.ui_tests
def test_validate_forgot_password(browser, cluster):
  login_page = SysdigLoginPage(browser)

  login_page.load(cluster)
  login_page.click_forgot_password()

  forgot_password_page = SysdigFotgotPasswordPage(browser)
  assert forgot_password_page.enter_email_displayed() == True
  forgot_password_page.enter_email('test@sysdig.com')
  forgot_password_page.click_request_password_reset()
  assert forgot_password_page.feedback_message_displayed() == True

@pytest.mark.parametrize('cluster', clusters)
@pytest.mark.ui_tests
def test_validate_sign_up(browser, cluster):
  login_page = SysdigLoginPage(browser)

  login_page.load(cluster)
  login_page.click_sign_up()

  assert browser.current_url == 'https://sysdig.com/company/start-free/'

@pytest.mark.parametrize('cluster', clusters)
@pytest.mark.ui_tests
def test_login_with_google(browser, cluster):
  login_page = SysdigLoginPage(browser)

  login_page.load(cluster)
  login_page.click_google()
  assert login_page.title() in 'Access: Google Accounts / Acceso: Cuentas de Google'
  assert login_page.signin_with_google_displayed() == True
  # ToDos
  ## Steps to Sign in with the Google account