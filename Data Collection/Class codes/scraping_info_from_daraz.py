from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the product page
driver.get('https://www.daraz.com.bd/products/4g-wifi-i468701703-s2256167219.html')
driver.maximize_window()

# Allow time for the page to load
time.sleep(5)

# Extract the product title
try:
    title = driver.find_element(By.CLASS_NAME, "pdp-mod-product-badge-title").text
except:
    title = "Title not found"

# Extract the product rating
try:
    rating = driver.find_element(By.CLASS_NAME, "pdp-review-summary__link").text
except:
    rating = "Rating not found"

# Extract the product price
try:
    price = driver.find_element(By.CLASS_NAME, "pdp-price").text
except:
    price = "Price not found"

# Extract the product details headline
try:
    details_headline = driver.find_element(By.CLASS_NAME, "pdp-mod-section-title").text
except:
    details_headline = "Details headline not found"

# Extract the short product details
try:
    short_details_elements = driver.find_elements(By.XPATH, '//li[@data-spm-anchor-id]')
    short_details = "\n".join([detail.text for detail in short_details_elements])
except:
    short_details = "Short details not found"

# Extract the full product details
try:
    full_details_elements = driver.find_elements(By.XPATH, '//div[@class="html-content detail-content"]//p')
    full_details = "\n".join([detail.text for detail in full_details_elements])
except:
    full_details = "Full details not found"

# Extract image URLs
try:
    image_elements = driver.find_elements(By.XPATH, '//div[@class="html-content detail-content"]//img')
    image_urls = [img.get_attribute('src') for img in image_elements]
except:
    image_urls = []

# Print extracted information
print("Product Title:", title)
print("Rating:", rating)
print("Price:", price)
print("Details Headline:", details_headline)
print("Short Product Details:\n", short_details)
print("Full Product Details:\n", full_details)
print("Product Images:", image_urls)

# Close the browser
driver.quit()
