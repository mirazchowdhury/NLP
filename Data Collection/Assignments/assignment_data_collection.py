from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import re
import time

# Specify the path to your ChromeDriver
from selenium.webdriver.chrome.options import Options

# Chrome options to handle SSL issues
options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

service = Service(r"G:\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

# Open the first page to find the total number of pages
driver.get('https://www.daraz.com.bd/routers/?page=1')
time.sleep(5)  # Allow time for the page to load
driver.maximize_window()

# Debug: Save page source
with open("page_source.html", "w", encoding="utf-8") as file:
    file.write(driver.page_source)

# Find the total number of items element safely
try:
    total_number_page_element = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[1]/div/div[1]/div/div/span[1]'))
    )
    total_number_page = total_number_page_element.text  # Use the .text property directly
except Exception as e:
    print(f"Error finding total number of pages: {e}")
    driver.quit()
    exit()

# Extract the total number of items using regex and calculate total pages
numbers = int(re.findall(r"\d+", total_number_page)[0])
total_page = (numbers // 40) + (1 if numbers % 40 != 0 else 0)  # Adjust for partial pages
print(f'Total pages: {total_page}')

# Dictionary to store links for each page
pages_links = {}

# Loop through each page dynamically
try:
    for page_no in range(1, total_page + 1):
        print(f"Scraping page {page_no}...")
        driver.get(f'https://www.daraz.com.bd/routers/?page={page_no}')
        time.sleep(5)  # Allow time for the page to load

        # Wait for products to load on the page
        WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#root > div > div.ant-row.FrEdP.css-1bkhbmc.app > div:nth-child(1) > div > div.ant-col.ant-col-20.ant-col-push-4.Jv5R8.css-1bkhbmc.app > div._17mcb > div:nth-child(1) > div > div > div.buTCk > div.RfADt > a')))

        # Collect product links using the provided CSS selector
        products = driver.find_elements(By.CSS_SELECTOR, '#root > div > div.ant-row.FrEdP.css-1bkhbmc.app > div:nth-child(1) > div > div.ant-col.ant-col-20.ant-col-push-4.Jv5R8.css-1bkhbmc.app > div._17mcb > div > div > div > div.buTCk > div.RfADt > a')
        page_links = [prod.get_attribute('href') for prod in products]

        # Store links for the current page
        pages_links[f'page_{page_no}'] = page_links
        print(f"Page {page_no} scraped. Found {len(page_links)} links.")
finally:
    driver.quit()

# Save the results to a JSON file
with open('daraz_links.json', 'w') as file:
    json.dump(pages_links, file, indent=4)

print("Scraping completed. Links saved to 'daraz_links.json'.")
