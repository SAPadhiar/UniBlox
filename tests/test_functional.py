"""
Script for functional testing
"""
from playwright.sync_api import expect
from support.test_base import TestBase
from support.test_data import User
from support.helper import Helpers
from support.page_data import PageData

class TestFunctional:
    """
    Test scenarios for verification of page elements
    """
    alnum = Helpers.generate_random_alphanumeric(10)

    def setup(self):
        """
        Invoked before every test function in the module
        """
        page = PageData()
        TestBase.get_page().goto(User.url)
        TestBase.get_page().wait_for_load_state("domcontentloaded")
        expect(TestBase.get_page()).to_have_title("Uniblox")
        expect(page.header_logo).to_be_visible()

    def teardown(self):
        """
        Invoked after every test function in the module
        """
        TestBase.get_browser().close()

    def test_add_insurance(self):
        """
        Verification for successful addition of Insurance
        """
        page = PageData()
        print("\nVerification for the Welcome Page")
        Helpers.verify_label(page.header_need_help_link, "Need help?")
        Helpers.verify_button(page.get_started_button, "Get Started")
        Helpers.verify_label(page.welcome_text, "👋Welcome")
        Helpers.verify_label(page.welcome_message, page.welcome_str)
        expect(page.footer_text).to_be_visible()
        page.header_need_help_link.click()
        expect(page.need_help_panel).to_be_visible()
        assert page.need_help_panel.all_inner_texts()[0] == page.help_panel, "Help Panel text mismatch"
        page.get_started_button.click()

        print("Verification for Applicant Page")
        Helpers.verify_label(page.applicant_type, "Applicant type")
        Helpers.verify_label(page.employee_label, "Employee")
        Helpers.verify_label(page.spouse_label, "Spouse")
        Helpers.verify_button(page.back_button, "Back")
        Helpers.verify_button(page.next_button, "Next")
        page.spouse_label.click()

        print("Verification for Spouse Name Page")
        Helpers.verify_label(page.your_name_label, "Your name")
        Helpers.verify_label(page.first_label, "First")
        Helpers.verify_label(page.last_label, "Last")
        Helpers.verify_textbox(page.first_name_input, None, self.alnum)
        Helpers.verify_textbox(page.last_name_input, None, self.alnum)
        page.first_name_input.fill(User.first_name)
        page.last_name_input.fill(User.last_name)
        page.next_button.click()

        print("Verification for Spouse Email Page")
        Helpers.verify_label(page.email_label, "Email")
        Helpers.verify_textbox(page.email_textbox, None, self.alnum+"@-.")
        page.email_textbox.fill(self.alnum)
        page.next_button.click()
        Helpers.verify_label(page.validation_error, "Please enter a valid email")
        page.email_textbox.fill(User.email)
        page.next_button.click()

        print("Verification for Employee Name Page")
        Helpers.verify_label(page.employee_name_label, "Employee Name")
        Helpers.verify_label(page.first_label, "First")
        Helpers.verify_label(page.last_label, "Last")
        Helpers.verify_textbox(page.first_name_input, None, self.alnum)
        Helpers.verify_textbox(page.last_name_input, None, self.alnum)
        page.first_name_input.fill("Employee" + User.first_name)
        page.last_name_input.fill("Employee" + User.last_name)
        page.next_button.click()

        print("Verification for Coverage Page")
        Helpers.verify_label(page.coverage_label, "Select a coverage amount")
        Helpers.verify_label(page.coverage_amount_label, "$0")
        expect(page.coverage_slider).to_be_visible()
        Helpers.move_slider(page.coverage_slider)
        Helpers.verify_label(page.coverage_amount_label, "$130,000")
        page.next_button.click()

        print("Verification for Date of Birth Page")
        Helpers.verify_label(page.date_of_birth_label, "Date of Birth")
        Helpers.verify_textbox(page.date_of_birth_textbox)
        page.date_of_birth_textbox.fill(self.alnum)     # Should not allow alphabetical chars
        assert page.phone_input.all_inner_texts() == [], "DOB not enter correctly"
        page.date_of_birth_textbox.fill(User.birth_date)
        Helpers.verify_label(page.date_format_label, "mm-dd-yyyy")
        page.next_button.click()

        print("Verification for Gender Page")
        Helpers.verify_label(page.gender_label, "Gender")
        Helpers.verify_label(page.male_label, "Male")
        Helpers.verify_label(page.female_label, "Female")
        page.male_label.click()

        print("Verification for Phone Page")
        Helpers.verify_label(page.phone_label, "Phone Number")
        Helpers.verify_textbox(page.phone_input)
        page.phone_input.fill(self.alnum)     # Should not allow alphabetical chars
        assert page.phone_input.all_inner_texts()[0] == '', "Phone number not entered correctly"
        page.phone_input.fill(User.phone)  # Should not allow to enter more than 10 digits
        Helpers.wait_for_element_to_have_text(page.phone_input, "(928) 745-9832")
        page.next_button.click()

        print("Verification for Address Page")
        Helpers.verify_label(page.address_label, "Address")
        Helpers.verify_textbox(page.location_input, None, self.alnum, "Enter a location")
        Helpers.verify_label(page.find_address_link, "I can't find my address")
        Helpers.verify_textbox(page.apt_unit_input, None, self.alnum)
        Helpers.verify_label(page.apt_unit_label, "Apt/Unit #")
        Helpers.verify_label(page.concent_message, page.concent)
        Helpers.verify_label(page.hipaa_message, page.hippa)
        page.location_input.fill(User.address)
        page.select_city.click()
        page.concent_checkbox.click()
        page.hipaa_notice_checkbox.click()
        page.next_button.click()

        print("Verification for Height & Weight Page")
        Helpers.verify_label(page.height_weight_label, "What is your height and weight?")
        Helpers.verify_label(page.height_label, "Height")
        page.height_dropdown.select_option("4'10\"")
        Helpers.verify_label(page.weight_label, "Weight (lbs)")
        Helpers.verify_textbox(page.weight_input)
        page.weight_input.fill(self.alnum)     # Should not allow alphabetical chars
        assert page.weight_input.all_inner_texts()[0] == '', "Weight not entered correctly"
        page.weight_input.fill("1234")  # Should not allow to enter more than 3 digits
        assert page.weight_input.input_value() == "123", "Weight not entered correctly"
