from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import re

# Specify the path to your ChromeDriver
service = Service(r"G:\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open the first page to find the total number of pages
driver.get('https://www.daraz.com.bd/routers/?page=1')
driver.maximize_window()

# Find the total number of items element safely
try:
    total_number_page_element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[1]/div/div[1]/div/div/span[1]')
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
for page_no in range(1, total_page + 1):
    driver.get(f'https://www.daraz.com.bd/routers/?page={page_no}')
    driver.maximize_window()

    page_links = []
    for prod in range(1, 41):  # Assuming up to 40 products per page
        try:
            # Dynamically generate XPath for each product
            link = driver.find_element(By.XPATH, f'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[{prod}]/div/div/div[2]/div[2]/a').get_attribute('href')
            page_links.append(link)
        except Exception as e:
            # Break out if fewer products are on the last page
            break

    # Add the links of the current page to the dictionary
    pages_links[f'page_{page_no}'] = page_links

# Print the dictionary containing links for all pages
for page, links in pages_links.items():
    print(f"{page}: {len(links)} links")

# Uncomment the following line to see all links if needed
# print(pages_links)

# Close the browser after collecting all data
time.sleep(2)
driver.quit()

# Output the dictionary (optional)
print(pages_links)
