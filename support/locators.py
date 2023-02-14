"""
This module holds information about Page Locators
"""

class Locators:
    """
    Class that contains Locators
    """
    header_logo = "//img[@alt='Header Logo']"
    header_need_help_link = "//div[contains(text(),'Need help?')]"
    get_started_button = "//button[@type='submit']"
    footer_text = "//div[contains(@class,'sticky bottom')]"
    welcome_text = "//div[text()='Welcome']"
    welcome_message = "//div[contains(text(), 'easy to apply')]"
    need_help_panel = "//div[@id='headlessui-popover-panel-:r0:']"
    loading_icon = "(//*[name()='svg'][@stroke='currentColor'])[1]"

    applicant_type = "//div[contains(@class,'truncate !text-xl font-medium')]"
    next_button = "(//button[contains(@type,'submit')])[1]"
    back_button = "(//button[contains(@type,'button')])[2]"
    employee_label = "//div[contains(text(),'Employee')]"
    spouse_label = "//div[contains(text(),'Spouse')]"

    your_name_label = "//div[contains(text(),'Your name')]"
    first_label = "label[for='first_name']"
    last_label = "label[for='last_name']"
    first_name_input = "#first_name"
    last_name_input = "#last_name"
