"""
A Base Class for Getting common Settings required throughout the Execution
"""

from playwright.sync_api import Browser, Page, sync_playwright


class TestBase:
    """
    BaseClass for getting Browser, Page, Configuration, TestData & Other Reusable Functions
    """
    __browser: Browser = None
    __page: Page = None

    @staticmethod
    def get_browser():
        """
        Method to get current or new instance of Browser. Will return a new instance only if the previous was
        closed or never initialized
        :return: Browser
        """
        if TestBase.__browser is None or not TestBase.__browser.is_connected():
            # the configurations can be coming from a JSON or YML file
            TestBase.__browser = sync_playwright().start().chromium.launch(headless=False, slow_mo=100)
        return TestBase.__browser

    @staticmethod
    def get_page():
        """
        Method to get current or new instance of Page. Will return a new instance only if the previous was
        closed or never initialized
        :return: Page
        """
        if TestBase.__page is None or (TestBase.__page.is_closed()):
            TestBase.__page = TestBase.get_browser().new_page()
        return TestBase.__page
