
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=watch&_sacat=0"
driver.get(url)

brand_rolex_check = wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Rolex')]")))
brand_rolex_check.click()

items_headers = wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH, "//span[@role='heading']")))

visible_items_headers = []
for header in items_headers:
    if header.is_displayed():
        visible_items_headers.append(header)

first_two_visible_headers = visible_items_headers[0:2]

mismatches = []
title_and_price = []
elems_on_item_page = []
for header in first_two_visible_headers:
    header_text = header.text.lower()
    if "rolex" not in header_text:
        mismatches.append(f"Header does not contain rolex: {header_text}")
    parent_element = header.find_element(By.XPATH, "./ancestor::li[contains(@class, 's-item')]")
    price = parent_element.find_element(By.XPATH, ".//span[@class='s-item__price']")
    title_and_price.append({
        "title": header.text,
        "price": price.text
    })
    header.click()
    current_tabs = driver.window_handles
    driver.switch_to.window(current_tabs[-1])

    header_inside = wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//h1[@class='x-item-title__mainTitle']")))
    price_inside = driver.find_element(By.XPATH, "//div[@class='x-price-primary']")
    # print(f"NEW {header_inside.text}, {price_inside.text}")
    elems_on_item_page.append({
        "title": header_inside.text,
        "price": price_inside.text[3:]
    })
    driver.close()
    driver.switch_to.window(current_tabs[0])

for i in range(len(title_and_price)):
    if title_and_price[i]["title"] != elems_on_item_page[i]["title"]:
        mismatches.append(f"Mismatch in title at index {i}. Expected title: {title_and_price[i]['title']}, Actual title: {elems_on_item_page[i]['title']}")
    if title_and_price[i]["price"] != elems_on_item_page[i]["price"]:
        mismatches.append(f"Mismatch in price at index {i}. Expected price: {title_and_price[i]['price']}, Actual price: {elems_on_item_page[i]['price']}")


brand_rolex_uncheck = wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Rolex')]")))
brand_rolex_uncheck.click()
brand_casio_check = driver.find_element(By.XPATH, "//span[contains(text(), 'Casio')]")
brand_casio_check.click()

new_items_headers = wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH, "//span[@role='heading']")))
new_visible_items_headers = []
for new_header in new_items_headers:
    if new_header.is_displayed():
        new_visible_items_headers.append(new_header)
new_first_two_visible_headers = new_visible_items_headers[-2:]

for new_header in new_first_two_visible_headers:
    new_header_text = new_header.text.lower()
    if "casio" not in new_header_text:
        mismatches.append("Header does not contain casio: {new_header_text}")

if mismatches:
    print("Found next mismatches:")
    for mismatch in mismatches:
        print(mismatch)
else:
    print("No mismatches found.")



driver.quit()













