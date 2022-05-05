# Sysdig Job Opportunity - Alejandro Zuniga

This repository contains code for some automated tests 

## Exercise Purpose

The exercise consists in writing automated tests against app.sysdigcloud.com, with the goal of testing the log-in webpage (do not log in/no need to log in)

## Project Structure
* locators folder: Here you can find the files that contain the locators for each page.
* pages folder: Here you can find the methods for each page.
* reports folder: Here you can find the latest results of the execution of the tests.
* tests folder: Here you can find the tests files.

## WebDriver Setup
For Web UI testing, you will need to install the latest versions of [Google Chrome](https://www.google.com/chrome/)
You will also need to install the latest versions of the WebDriver executables for these browsers: [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) for Chrome
Each test case will launch the WebDriver executable for this target browser.
The WebDriver executable will act as a proxy between the test automation and the browser instance.
Please use the latest versions of both the browsers and the WebDriver executables.

### WebDriver Setup for Windows
To install ChromeDriver on Windows:
1. Create a folder named `C:\Selenium`.
2. Move the executables into this folder.

## Test Cases Cover
All Tests are parametrized to run for all the clusters defined in ./test/conftest.py
* test_api_clusters
* test_login_with_invalid_credentials
* test_validate_forgot_password
* test_validate_sign_up
* test_login_with_google (ToDos are pending)

## Run the Tests
* To Run the API basic tests you need to run: 'py -m pytest -m api_tests --html=./reports/report-api-tests.html'
* To Run the UI tests you need to run: 'py -m pytest -m ui_tests --html=./reports/report-ui-tests.html'
* To Run all tests you need to run: 'py -m pytest --html=./reports/report-all-tests.html'

## Test Cases Pending to Implement
* test_login_with_empty_fields
* test_validate_cluster_selection
* test_sign_up
* test_validate_changed_your_mind (In Forgot your password page)
* test_login_with_saml
* test_go_back_from_saml
* test_login_with_openid
* test_go_back_from_openid

## Improvements for the page
* Validate the correct email structure (.com part is not required)
