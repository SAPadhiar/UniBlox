"""
Script to test Login Page
"""
import pytest
from playwright.sync_api import sync_playwright
from support.test_base import TestBase
from support.test_data import Website

class TestFunctional:
    """
    Test scenarios for Login page
    """
    def setup(self):
        """
        Invoked before every test function in the module.
        """
        TestBase.get_page().goto(Website.url)

    def teardown(self):
        """
        Invoked after every test function in the module.
        """
        TestBase.get_browser().close()

    def test_login_001(self):
        """
        Verify Login GUI
        """
