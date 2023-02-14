"""
This module has functions to verify different form controls
"""
import random
import string
import time
from playwright.sync_api import Locator, expect
from support.test_base import TestBase


class Helpers:
    """
    Contains support methods for verification of form elements
    """
    @staticmethod
    def verify_button(locator:Locator, button_text:str=None, is_enabled:bool=True):
        """
        Method to add basic verifications for a given button element
        """
        locator.wait_for(state="visible")
        expect(locator).to_be_visible()
        if button_text:
            try:
                expect(locator).to_have_value(button_text)
            except:
                expect(locator).to_have_text(button_text)
        if is_enabled:
            expect(locator).to_be_enabled()
        else:
            expect(locator).to_be_disabled()

    @staticmethod
    def verify_label(locator:Locator, expected_text:str, href:str=None):
        """
        Method to verify element text
        """
        locator.wait_for(state="visible")
        expect(locator).to_be_visible()
        expect(locator).to_have_text(expected_text)
        if href:
            expect(locator).to_have_attribute("href", href)

    @staticmethod
    def verify_textbox(locator:Locator, is_required:bool=None, input_value:str=None, placeholder:str=None):
        """
        Method to add basic verifications for a given textbox element
        """
        locator.wait_for(state="visible")
        expect(locator).to_be_visible()
        if is_required:
            assert locator.get_attribute("required"), "The field is not required"
        if placeholder:
            assert locator.get_attribute("placeholder").strip() == placeholder, "Mismatch in placeholder"
        if input_value:
            locator.fill(input_value)
            text = locator.input_value()
            assert input_value in text
            locator.fill("")

    @staticmethod
    def generate_random_alphanumeric(size: int):
        """
        Returns randomly generated alphanumeric string
        """
        return ''.join(random.choices(string.ascii_letters + string.digits, k=size))

    @staticmethod
    def move_slider(locator:Locator):
        """
        Method to move the slider element
        """
        locator.hover()
        TestBase.get_page().mouse.down()
        locator.hover()
        TestBase.get_page().mouse.up()

    @staticmethod
    def wait_for_element_to_have_text(element: Locator, expected_text: str, timeout_seconds: int = 15) -> None:
        """
        Waits till an element to have expected text
        """
        count = 1
        while expected_text not in element.input_value() and count <= timeout_seconds:
            time.sleep(1)
            count += 1
