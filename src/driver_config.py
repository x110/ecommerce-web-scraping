from selenium import webdriver
from fake_useragent import UserAgent

def configure_driver():
    ua = UserAgent()
    user_agent = ua.random

    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={user_agent}")

    return webdriver.Chrome(options=options)
