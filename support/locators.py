"""
This module holds information about Page Locators
"""

class Locators:
    """
    Class that contains Locators
    """
    # Welcome page locators
    header_logo = "//img[@alt='Header Logo']"
    header_need_help_link = "//div[contains(text(),'Need help?')]"
    get_started_button = "//button[@type='submit']"
    footer_text = "//div[contains(@class,'sticky bottom')]"
    welcome_text = "//div[text()='Welcome']"
    welcome_message = "//div[contains(text(), 'easy to apply')]"
    need_help_panel = "//div[@id='headlessui-popover-panel-:r0:']"
    loading_icon = "(//*[name()='svg'][@stroke='currentColor'])[1]"

    # Applicant detials page locators
    applicant_type = "//div[contains(@class,'truncate !text-xl font-medium')]"
    next_button = "(//button[contains(@type,'submit')])[1]"
    back_button = "(//button[contains(@type,'button')])[2]"
    employee_label = "//div[contains(text(),'Employee')]"
    spouse_label = "//div[contains(text(),'Spouse')]"

    # Spouse Name page locators
    your_name_label = "//div[contains(text(),'Your name')]"
    employee_name_label = "//div[contains(text(),'Employee')]"
    first_label = "label[for='first_name']"
    last_label = "label[for='last_name']"
    first_name_input = "#first_name"
    last_name_input = "#last_name"

    # Spouse Email page locators
    email_label = "//div[contains(text(),'Email')]"
    email_textbox = "input[name='answer']"
    validation_error = "//span[contains(text(),'enter a valid email')]"

    # Coverage selection page locators
    coverage_label = "//div[contains(text(),'coverage')]"
    coverage_slider = ".rc-slider.rc-slider-horizontal"
    slider_handle = "div[role='slider']"
    coverage_amount_label = ".text-xl.text-neutral-100.text-left.font-medium.mb-4"

    # Date of birth page locators
    date_of_birth_label = "//div[contains(text(),'Date')]"
    date_of_birth_textbox = "#date"
    date_format_label = ".text-sm.text-neutral-100.font-normal"

    # Gender select page locators
    gender_label = "//div[contains(text(),'Gender')]"
    male_label = "//div[contains(text(),'Male')]"
    female_label = "//div[contains(text(),'Female')]"

    # Phone number page locators
    phone_label = "//div[contains(text(),'Phone')]"
    phone_input = "input[name='answer']"
