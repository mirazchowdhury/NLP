# from selenium import webdriver
# import time
# import selenium.webdriver.common.by import By
# import re

# driver = webdriver.Chrome()
# driver.get('https://www.daraz.com.bd/routers/?page=1')
# driver.maximize_window()
# time.sleep(30)
# driver.quit()


from selenium import webdriver
import time
from selenium.webdriver.common.by import By  # Corrected import statement
import re

driver = webdriver.Chrome()
driver.get('https://www.daraz.com.bd/products/4g-wifi-i468701703-s2256167219.html')
driver.maximize_window()

# to execute javascript code on python, we need to use driver.execute_script()
height = driver.execute_script('return document.body.scrollHeight') 
print(height)

for i in range(0,height+1000,30):
    driver.execute_script(f'window.scrollTo(0,{i});')
    time.sleep(0.5)

# we have to check which css class is common in the review, then we take that class, run a loop for that class
all_comments = driver.find_elements(By.CLASS_NAME,'content')
for i in all_comments:
    print(i.text)

time.sleep(30)
driver.quit()