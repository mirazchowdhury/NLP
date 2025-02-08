# from selenium import webdriver
# from selenium.webdriver.common.by import By 
# import time 
# import math


# driver = webdriver.Chrome()

# driver.get("https://www.daraz.com.bd/products/polashi-a-social-deduction-board-game-5-to-10-players-age-12-i294822893-s1304280008.html?c=&channelLpJumpArgs=&clickTrackInfo=query%253Apolashi%253Bnid%253A294822893%253Bsrc%253ALazadaMainSrp%253Brn%253Accdb9fc1bd883b618affd93348ba58de%253Bregion%253Abd%253Bsku%253A294822893_BD%253Bprice%253A599%253Bclient%253Adesktop%253Bsupplier_id%253A700533537674%253Bbiz_source%253Ahttps%253A%252F%252Fwww.daraz.com.bd%252F%253Bslot%253A0%253Butlog_bucket_id%253A470687%253Basc_category_id%253A9369%253Bitem_id%253A294822893%253Bsku_id%253A1304280008%253Bshop_id%253A340729%253BtemplateInfo%253A&freeshipping=0&fs_ab=1&fuse_fs=&lang=en&location=Dhaka&price=599&priceCompare=skuId%3A1304280008%3Bsource%3Alazada-search-voucher%3Bsn%3Accdb9fc1bd883b618affd93348ba58de%3BoriginPrice%3A59900%3BdisplayPrice%3A59900%3BsinglePromotionId%3A-1%3BsingleToolCode%3A-1%3BvoucherPricePlugin%3A0%3Btimestamp%3A1738870105138&ratingscore=4.689655172413793&request_id=ccdb9fc1bd883b618affd93348ba58de&review=232&sale=1170&search=1&source=search&spm=a2a0e.searchlist.list.0&stock=1")

# driver.maximize_window()


# height = driver.execute_script('return document.body.scrollHeight')
# print(height)

# for i in range(0,height+2000,30):
#     time.sleep(0.5)
#     driver.execute_script(f'window.scrollTo(0,{i});')

# comments = driver.find_elements(By.CLASS_NAME,'content')

# for i in comments:
#     print(i.text)


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def get_total_pages(driver):
    """Get the total number of comment pages."""
    try:
        total_pages_element = driver.find_element(By.XPATH, '//button[@class="next-pagination-item"][last()]')
        total_pages = int(total_pages_element.text)
        print(f"Total pages: {total_pages}")
        return total_pages
    except Exception as e:
        print(f"Error getting total pages: {e}")
        return 1

def scrape_comments(driver):
    """Scrape comments from all pages."""
    comments_dict = {}
    total_pages = get_total_pages(driver)

    for page in range(1, total_pages + 1):
        time.sleep(2)  # Allow time for the page to load
        print(f"\nScraping page {page}...")

        comments = driver.find_elements(By.CLASS_NAME, 'content')
        comments_list = [comment.text for comment in comments]
        comments_dict[f"Page {page}"] = comments_list

        # Print comments from the current page
        for comment in comments_list:
            print(f"- {comment}")

        # Go to the next page if not the last page
        if page < total_pages:
            try:
                next_button = driver.find_element(By.XPATH, '//button[@aria-label="Next page"]')
                next_button.click()
                time.sleep(3)  # Wait for the next page to load
            except Exception as e:
                print(f"Error clicking next button: {e}")
                break

    return comments_dict

def main():
    driver = webdriver.Chrome()
    driver.get("https://www.daraz.com.bd/products/polashi-a-social-deduction-board-game-5-to-10-players-age-12-i294822893-s1304280008.html")
    driver.maximize_window()

    # Scroll to the bottom to load the comments section
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Scrape comments from all pages
    comments = scrape_comments(driver)
    
    driver.quit()

    # Save or process comments as needed
    print("\nAll comments scraped successfully!")
    for page, comment_list in comments.items():
        print(f"\n{page} Comments:")
        for comment in comment_list:
            print(f"- {comment}")

if __name__ == "__main__":
    main()
