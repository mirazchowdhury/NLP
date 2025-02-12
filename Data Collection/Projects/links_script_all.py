import time
import streamlit as st
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Streamlit page configuration
st.set_page_config(page_title="Google Scraper", page_icon="🔍", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .big-title {
        font-size:36px !important;
        text-align: center;
        color:rgb(55, 15, 217);
        font-weight: bold;
    }
    .stTextInput > label {
        font-size:18px;
        font-weight: bold;
    }
    .stButton button {
        background-color:rgb(55, 15, 217) !important;
        color: white !important;
        font-size: 16px;
        border-radius: 10px;
        padding: 8px 24px;
    }
    .stDataFrame {
        background-color: black;
        border-radius: 10px;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and description
st.markdown('<p class="big-title">🔍 Google Search Scraper</p>', unsafe_allow_html=True)
st.write("Enter a search term to collect **all links** from the first **3 pages of Google**.")

# Input field for the search query
search_query = st.text_input("🔎 Enter Search Query:")

# Submit button to trigger scraping
if st.button("Search Google"):
    if search_query.strip():
        progress_bar = st.progress(0)
        status_text = st.empty()
        status_text.text("🚀 Searching Google...")

        # Set up Chrome options
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--incognito")
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

        # Create WebDriver instance
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get(f"https://www.google.com/search?q={search_query.replace(' ', '+')}")
        driver.maximize_window()

        all_links = set()  # Use set to avoid duplicates
        page = 1
        max_pages = 3  # Number of pages to scrape

        try:
            while page <= max_pages:
                time.sleep(2)  # Wait for the page to load

                WebDriverWait(driver, 5).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.tF2Cxc a"))
                )

                # Extract all valid links
                search_results = driver.find_elements(By.CSS_SELECTOR, "div.tF2Cxc a")
                for result in search_results:
                    link = result.get_attribute("href")
                    if link and "google.com" not in link:  # Avoid Google-related links
                        all_links.add(link)

                progress_bar.progress(page / max_pages)

                try:
                    next_button = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, "#pnnext"))
                    )
                    next_button.click()
                    page += 1
                except (NoSuchElementException, TimeoutException):
                    break

        except Exception as e:
            st.error(f"⚠️ Error: {str(e)}")

        driver.quit()

        # Display the results in a Pandas DataFrame
        if all_links:
            df = pd.DataFrame(sorted(all_links), columns=["🌍 Web Links"])
            status_text.text("✅ Scraping Completed!")
            progress_bar.empty()

            st.write("### 🔗 Extracted Links:")
            st.dataframe(df, use_container_width=True)

            # Option to copy links as text
            copy_text = "\n".join(df["🌍 Web Links"])
            st.code(copy_text, language="text")
            st.success("✅ You can copy and save these links!")
        else:
            st.warning("⚠️ No links were extracted. Google may have blocked automated access.")
    else:
        st.warning("⚠️ Please enter a search query.")
