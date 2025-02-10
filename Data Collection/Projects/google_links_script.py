# import time
# import streamlit as st
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# import pandas as pd

# # Set up Streamlit
# st.title("Google Search Automation with Selenium")

# # Input field for the search query
# search_query = st.text_input("Enter your search query:")

# # Submit button to trigger search and fetch results
# if st.button("Submit") and search_query:
#     # Set up Chrome options for Selenium
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--disable-gpu")
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument("--disable-dev-shm-usage")
    
#     # Create a WebDriver instance
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
#     # Perform Google search automation
#     driver.get("https://www.google.com/")
#     search_box = driver.find_element(By.NAME, "q")
#     search_box.send_keys(search_query)
#     search_box.send_keys(Keys.RETURN)
    
#     # Wait for results to load
#     time.sleep(2)
    
#     # Collect links from the first three pages
#     links = []
#     for page in range(1, 4):  # Iterate for 3 pages
#         for i in range(1, 12, 2):  # Loop to cover div[1], div[3], div[5], ..., div[11]
#             try:
#                 link_element = driver.find_elements(By.XPATH, f'/html/body/div[3]/div/div[12]/div/div/div[2]/div[2]/div/div/div[{i}]/div/div/div/div[1]/div/div/span/a')
#                 link = link_element.get_attribute('href')
#                 if link:
#                     links.append(link)
#             except Exception as e:
#                 # Ignore if no link is found at the specific index
#                 continue
        
#         # Navigate to the next page
#         try:
#             next_button = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[12]/div/div/div[4]/div/div[3]/table/tbody/tr/td[12]/a')
#             next_button.click()
#             time.sleep(2)
#         except Exception as e:
#             print(f"Error navigating to next page: {e}")
#             break

#     # Close the browser
#     driver.quit()

#     # Show the results in a table
#     if links:
#         df = pd.DataFrame(links, columns=["Web Links"])
#         st.table(df)
#     else:
#         st.write("No results found.")





import time
import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains

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
    
    # Find the search box and enter the search query
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)
    
    # Wait for results to load
    time.sleep(2)
    
    # To scroll down and load more results dynamically
    links = set()  # Use set to avoid duplicate links
    scroll_pause_time = 2  # Time to pause after scrolling
    
    # Scroll to load more results (scrolling multiple times for more results)
    for _ in range(5):  # Adjust the number of scrolls based on your needs
        # Collect links from the page
        results = driver.find_elements(By.XPATH, '//*[@class="UWckNb"]')
        for result in results:
            link = result.get_attribute('href')
            if link:
                links.add(link)
        
        # Scroll down to the bottom of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)

    # Close the browser
    driver.quit()

    # Show the results in a table using Pandas DataFrame
    if links:
        df = pd.DataFrame(list(links), columns=["Web Links"])
        st.write(df)
    else:
        st.write("No results found.")
