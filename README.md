## SauceDemo Automation Test Suite - Miranda Cipollone

This project is a Selenium + pytest automation framework for testing the Sauce Demo site

## Overview
The test suite covers these core scenarios:

-Login (valid & invalid credentials)

-Cart Actions (adding/removing products)

-Checkout Flows (successful, missing details)

-Product Sorting (low-to-high)

-Logout

## Requirements

-Python 3.7+

-pip

-Google Chrome

-ChromeDriver

Ensure it’s placed in your PATH

## Installation

**-Clone the Repository**

_git clone https://github.com/mirandacipollone/mirandacipollone.github.io.git_
-Create & Activate a Virtual Environment

_python -m venv .venv_

_source .venv/bin/activate   # macOS/Linux_

_.venv\Scripts\activate      # Windows_


**Install Dependencies**

_pip install selenium pytest Faker pytest-html_

**Add ChromeDriver to PATH**

macOS: Move or symlink the chromedriver binary into /usr/local/bin/ or update your ~/.zshrc or ~/.bash_profile.

Windows: Place chromedriver.exe in a folder on your PATH (like C:\Windows\System32) or set an environment variable.

## Project Structure

**pages/**: Each page object encapsulates locators and actions for a specific page.

**tests/**: Contains test files for different features.

**utils/**: Utility modules (e.g., config, data loading, etc.).

**conftest.py**: pytest configuration and fixtures 


## Running the Tests

Here are some common commands you can use to run the test suite. Make sure you’re in the project’s root directory, and you have installed all dependencies

**Basic Run (with verbose output):**

_python -m pytest -v_

**Run with Custom Window Size:**

_python -m pytest -v --width=800 --height=800_

**Run in a Different Browser (e.g., Firefox):**

_python -m pytest -v --browser=firefox_


**Generate an HTML Report:**

_python -m pytest -v --html=report.html --self-contained-html_

You can combine these options as needed. For example, to run in Firefox with an 800×800 window and generate an HTML report:

_python -m pytest -v --browser=firefox --width=800 --height=800 --html=report.html --self-contained-html_

