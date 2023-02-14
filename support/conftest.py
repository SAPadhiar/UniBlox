import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="module", autouse=True)
def setup_test_module():
    """
    Sets up the Test Case Pre-conditions that is about to run.
    :param request:
    :param base_url:
    :return:
    """
