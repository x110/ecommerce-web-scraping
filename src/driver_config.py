from selenium import webdriver
from fake_useragent import UserAgent

def configure_driver() -> webdriver.Chrome:
    """
    Configure and return a Chrome WebDriver instance.

    Returns:
        webdriver.Chrome: The configured Chrome WebDriver instance.
    """
    options = webdriver.ChromeOptions()
    user_agent = UserAgent().random
    options.add_argument(f"user-agent={user_agent}")
    return webdriver.Chrome(options=options)
