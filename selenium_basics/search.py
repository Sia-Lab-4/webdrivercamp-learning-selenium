import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

url = "https://www.ebay.com/"

# Task 1
# driver.get(url)
# print(url)
# driver.quit()

# Task 2
# driver.get(url)
# wait = WebDriverWait(driver, 10)
# wait.until(expected_conditions.visibility_of_element_located((By.ID, "gh-logo")))
# print(url)
# driver.quit()

# Task 3
# driver.get(url)
# wait = WebDriverWait(driver, 10)
# wait.until(expected_conditions.visibility_of_element_located((By.ID, "gh-logo")))
# print(url)
# search_field = driver.find_element(By.ID, "gh-ac")
# search_field.send_keys("women watch")
# search_button = driver.find_element(By.ID, "gh-btn")
# search_button.click()
# driver.quit()


# Task 4
# driver.get(url)
# wait = WebDriverWait(driver, 10)
# wait.until(expected_conditions.visibility_of_element_located((By.ID, "gh-logo")))
# print(url)
# search_field = driver.find_element(By.ID, "gh-ac")
# search_field.send_keys("women watch")
# search_button = driver.find_element(By.ID, "gh-btn")
# search_button.click()
# wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//h1")))
# verified_header = driver.find_element(By.XPATH, '//h1')
# element_text = verified_header.text
# expected_text = "results for women watch"
# assert expected_text in element_text
# driver.quit()








