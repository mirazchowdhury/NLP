from selenium import webdriver
import time
from selenium.webdriver.common.by import By  # Corrected import statement

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the product page
driver.get('https://www.daraz.com.bd/products/4g-wifi-i468701703-s2256167219.html')
driver.maximize_window()

# Pause to ensure the page loads fully
time.sleep(3)

# Get the total height of the webpage
height = driver.execute_script('return document.body.scrollHeight')
print(f"Total page height: {height}")

# Scroll down using the `scrollBy` method
scroll_amount = 500  # Scroll by 500px each time
current_position = 0

while current_position < height:
    driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
    current_position += scroll_amount
    time.sleep(0.5)  # Pause to let content load

# Extract all comments using the CSS class name 'content'
try:
    all_comments = driver.find_elements(By.CLASS_NAME, 'content')
    print("Extracted Comments:")
    for comment in all_comments:
        print(comment.text)
except Exception as e:
    print(f"Error extracting comments: {e}")

# Pause before quitting the browser
time.sleep(5)
driver.quit()
