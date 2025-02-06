from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


# Specify the path to your ChromeDriver
service = Service(r"G:\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open the website
#driver.get('https://www.daraz.com.bd/routers/')



link_list=[]
driver.get('https://www.daraz.com.bd/routers/?page=1')
driver.maximize_window()
total_number_page = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[1]/div/div[1]/div/div/span[1]').text()       
#print(f'total = {total_number_page}')
#total_number_page = int(total_number_page.split()[0])

# using regex
import re
numbers = int(re.findall(r"\d+", total_number_page)[0])
total_page = round(numbers/40)
print(total_page)
#print(numbers)


#find numbers in the list


#Multiple Xpath _____ class 3
for page_no in range(1,3):
    driver.get(f'https://www.daraz.com.bd/routers/?page={page_no}')
    #maximize the window
    driver.maximize_window()
    for prod in range(1,13):
        type_i = str(prod)
        #XPATH Utilization
        link = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div['+type_i+']/div/div/div[2]/div[2]/a').get_attribute('href')

#link_list.append(link)

print(link_list)
print(len(link_list))

#if we want to open the link, then

#driver.get(link.get_attribute('href'))

# Keep the browser open for 1000 seconds
time.sleep(1000)

# Close the browser
driver.quit()


