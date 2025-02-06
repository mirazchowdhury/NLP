import time
import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Set up Streamlit
st.title("Google Search Automation with Selenium")

# Input field for the search query
search_query = st.text_input("Enter your search query:")

# Submit button to trigger search and fetch results
if st.button("Submit") and search_query:
    # Set up Chrome options for Selenium
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run browser in background
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Create a WebDriver instance
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    # Perform Google search automation
    driver.get("https://www.google.com/")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)
    
    # Wait for results to load
    time.sleep(2)
    
    # Collect links from first three pages of results
    links = []
    for i in range(3):
        # Update XPath for search result links
        results = driver.find_elements(By.XPATH, '//div[@class="g"]//a')
        for result in results:
            link = result.get_attribute('href')
            if link:
                links.append(link)
        
        # Navigate to the next page if not on the last page
        try:
            next_button = driver.find_element(By.XPATH, '//*[@id="pnnext"]')
            next_button.click()
            time.sleep(2)
        except Exception as e:
            print(f"Error navigating to next page: {e}")
            break

    # Close the browser
    driver.quit()

    # Show the results in a table
    if links:
        df = pd.DataFrame(links, columns=["Web Links"])
        st.table(df)
    else:
        st.write("No results found.")

