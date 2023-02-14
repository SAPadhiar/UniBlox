"""
This module holds information about instances of locators
"""
from support.locators import Locators
from support.test_base import TestBase


class PageData:
    """
    Class that contains instances of locators
    """
    welcome_str = "It’s easy to apply, tell us about yourself and see if you’re instantly approved for coverage! It’ll only take about 5-10 mins to complete your application."
    help_panel = "Email us\nyoursupport@insure.com\nIf you have questions specific to your coverages, please reach out to your HR Representative."
    concent = "I have read and agree to sign the Consent to do business electronically"
    hippa = "I have read and agree to sign the HIPAA notice which authorizes any physician, hospital, pharmacy, pharmacy benefit manager, health insurance plan or any other entity that possesses any diagnosis, treatment, prescription or other medical information about me to furnish such health information to Symetra Life Insurance Company for the purpose of evaluating my eligibility for insurance. This medical or health information may include information on the diagnosis and treatment of mental illness, alcohol, and drug use. This also includes information on the diagnosis, treatment, and testing results related to HIV, AIDS, and sexually transmitted diseases, unless otherwise restricted by state law. Health information obtained will not be re-disclosed without my authorization unless permitted by law, in which case it may not be protected under federal privacy rules. This authorization shall be valid for two years from this date and may be revoked by sending written notice to Symetra Life Insurance Company. I further understand that if I refuse to sign this authorization to release your complete medical record, Symetra Life Insurance Company may not be able to process my application."

    def __init__(self):
        self.header_logo = TestBase.get_page().locator(Locators.header_logo)
        self.header_need_help_link = TestBase.get_page().locator(Locators.header_need_help_link)
        self.get_started_button = TestBase.get_page().locator(Locators.get_started_button)
        self.footer_text = TestBase.get_page().locator(Locators.footer_text)
        self.welcome_text = TestBase.get_page().locator(Locators.welcome_text)
        self.welcome_message = TestBase.get_page().locator(Locators.welcome_message)
        self.need_help_panel = TestBase.get_page().locator(Locators.need_help_panel)
        self.loading_icon = TestBase.get_page().locator(Locators.loading_icon)
        self.applicant_type = TestBase.get_page().locator(Locators.applicant_type)
        self.next_button = TestBase.get_page().locator(Locators.next_button)
        self.back_button = TestBase.get_page().locator(Locators.back_button)
        self.employee_label = TestBase.get_page().locator(Locators.employee_label)
        self.spouse_label = TestBase.get_page().locator(Locators.spouse_label)
        self.your_name_label = TestBase.get_page().locator(Locators.your_name_label)
        self.first_label = TestBase.get_page().locator(Locators.first_label)
        self.last_label = TestBase.get_page().locator(Locators.last_label)
        self.first_name_input = TestBase.get_page().locator(Locators.first_name_input)
        self.last_name_input = TestBase.get_page().locator(Locators.last_name_input)
        self.email_label = TestBase.get_page().locator(Locators.email_label)
        self.email_textbox = TestBase.get_page().locator(Locators.email_textbox)
        self.validation_error = TestBase.get_page().locator(Locators.validation_error)
        self.employee_name_label = TestBase.get_page().locator(Locators.employee_name_label)
        self.coverage_label = TestBase.get_page().locator(Locators.coverage_label)
        self.coverage_slider = TestBase.get_page().locator(Locators.coverage_slider)
        self.slider_handle = TestBase.get_page().locator(Locators.slider_handle)
        self.coverage_amount_label = TestBase.get_page().locator(Locators.coverage_amount_label)
        self.date_of_birth_label = TestBase.get_page().locator(Locators.date_of_birth_label)
        self.date_of_birth_textbox = TestBase.get_page().locator(Locators.date_of_birth_textbox)
        self.date_format_label = TestBase.get_page().locator(Locators.date_format_label)
        self.gender_label = TestBase.get_page().locator(Locators.gender_label)
        self.male_label = TestBase.get_page().locator(Locators.male_label)
        self.female_label = TestBase.get_page().locator(Locators.female_label)
        self.phone_label = TestBase.get_page().locator(Locators.phone_label)
        self.phone_input = TestBase.get_page().locator(Locators.phone_input)
        self.address_label = TestBase.get_page().locator(Locators.address_label)
        self.location_input = TestBase.get_page().locator(Locators.location_input)
        self.find_address_link = TestBase.get_page().locator(Locators.find_address_link)
        self.concent_message = TestBase.get_page().locator(Locators.concent_message)
        self.concent_checkbox = TestBase.get_page().locator(Locators.concent_checkbox)
        self.hipaa_message = TestBase.get_page().locator(Locators.hipaa_message)
        self.hipaa_notice_checkbox = TestBase.get_page().locator(Locators.hipaa_notice_checkbox)
        self.apt_unit_input = TestBase.get_page().locator(Locators.apt_unit_input)
        self.apt_unit_label = TestBase.get_page().locator(Locators.apt_unit_label)
        self.select_city = TestBase.get_page().locator(Locators.select_city)
        self.height_weight_label = TestBase.get_page().locator(Locators.height_weight_label)
        self.height_label = TestBase.get_page().locator(Locators.height_label)
        self.weight_label = TestBase.get_page().locator(Locators.weight_label)
        self.height_dropdown = TestBase.get_page().locator(Locators.height_dropdown)
        self.weight_input = TestBase.get_page().locator(Locators.weight_input)
