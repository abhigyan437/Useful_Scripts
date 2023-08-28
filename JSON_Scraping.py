import json
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedrive.exe")  # Loading the Webdriver
driver.get('https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1')  # Navigating to the targeted URL
title_list = []  # List for Collection of Titles of Products
price_list = []  # List for Collection of Prices of Products
status_list = []  # List for Collection of Stock Status of Products
brand_list = []  # List for Collection of Brands of Products
for elm in driver.find_elements(By.CLASS_NAME, 'catalog-item-name'):
    title_list.append(elm.text)  # Getting the Title
for elm in driver.find_elements(By.CLASS_NAME, 'price'):
    price_list.append(elm.text)  # Getting the Price
for elm in driver.find_elements(By.CLASS_NAME, 'status'):
    status_list.append(elm.text)  # Getting the Stock Status
for elm in driver.find_elements(By.CLASS_NAME, 'catalog-item-brand'):
    brand_list.append(elm.text)  # Getting the Brand
num = len(brand_list)  # Finding total number of Products
dict_collection = {}  # Declaring Dictionary for collection of all info related to an individual brand
list_collection = []  # Declaring the list for collecting all dictionaries
for i in range(0, num):  # Collecting all info related to a particular product
    dict_collection['Price'] = price_list[i]
    dict_collection['Title'] = title_list[i]
    dict_collection['Stock'] = status_list[i]
    dict_collection['Maftr'] = brand_list[i]
    list_collection.append(dict_collection)  # Appending formed dictionary to the Overall List
data = json.dumps(list_collection)  # Converting the List to JSON format
print(data)  # Printing the final output in the form of JSON
