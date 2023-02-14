"""
Script for functional testing
"""
import pytest
from playwright.sync_api import sync_playwright, expect
from support.test_base import TestBase
from support.test_data import Website
from support.helper import Helpers
from support.page_data import PageData

class TestFunctional:
    """
    Test scenarios for verification of page elements
    """
    def setup(self):
        """
        Invoked before every test function in the module
        """
        page = PageData()
        TestBase.get_page().goto(Website.url)
        TestBase.get_page().wait_for_load_state("domcontentloaded")
        expect(TestBase.get_page()).to_have_title("Uniblox")
        expect(page.header_logo).to_be_visible()

    def teardown(self):
        """
        Invoked after every test function in the module
        """
        TestBase.get_page().screenshot("screenshot.png", full_page=True)
        TestBase.get_browser().close()

    def test_GUI(self):
        """
        Verify GUI elements
        """
        page = PageData()
        Helpers.verify_label(page.header_need_help_link, "Need help?")
        Helpers.verify_button(page.get_started_button, "Get Started")
        Helpers.verify_label(page.welcome_text, "👋Welcome")
        Helpers.verify_label(page.welcome_message, page.welcome_str)
        expect(page.footer_text).to_be_visible()
        page.header_need_help_link.click()
        expect(page.need_help_panel).to_be_visible()
        assert page.need_help_panel.all_inner_texts()[0] == page.help_panel
        page.get_started_button.click()

        Helpers.verify_label(page.applicant_type, "Applicant type")
        Helpers.verify_label(page.employee_label, "Employee")
        Helpers.verify_label(page.spouse_label, "Spouse")
        Helpers.verify_button(page.back_button, "Back")
        Helpers.verify_button(page.next_button, "Next")
        page.spouse_label.click()

        Helpers.verify_label(page.your_name_label, "Your name")
        Helpers.verify_label(page.first_label, "First")
        Helpers.verify_label(page.last_label, "Last")
        page.first_name_input.fill(Website.first_name)
        page.last_name_input.fill(Website.last_name)
        page.next_button.click()
