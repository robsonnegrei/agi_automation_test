from selenium import webdriver
from selenium.webdriver.chrome.options import Options
def before_all(context):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    context.driver = webdriver.Chrome()
    context.driver.get('https://blogdoagi.com.br/')


def after_all(context):
    context.driver.quit()
