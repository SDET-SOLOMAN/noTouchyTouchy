import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pytest

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get('https://suninjuly.github.io/xpath_examples')

browser = Service('/Users/mikesoloman/PycharmProjects/EveyroneQA/chromedriver')
driver = webdriver.Chrome(service=browser)


driver.get("http://suninjuly.github.io/cats.html")
a = driver.find_element(By.XPATH, ("//*[contains(text(),'Bullet cat')]"))

print(a.text)

# or //*[contains(text(), 'Bullet cat')]