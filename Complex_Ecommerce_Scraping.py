import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# Remaining Product separation & addition to the df
browser = webdriver.Chrome(
    'C:\Drivers\chromedrive.exe')  # Address of the chrome driver & can vary from system to system
browser.get("https://exhibitoremanual.com/packplusdelhi20/elist/exhibitorlist.aspx")
c = 0
list_raw_stores = []
list_stores_link = browser.find_elements(By.CLASS_NAME, "viewdetails")
for ele in browser.find_elements(By.TAG_NAME, "h3"):
    list_raw_stores.append(ele.text)
n = len(list_stores_link)
list_sno = list()
list_store_name = list()
list_address = []
list_pin = []
list_state=[]
list_city=[]
list_website=[]
list_product = []
list_sub_product=[]
list_tele=[]
list_mobile=[]
list_email = []
list_ceo= []
list_contact_person = []
list_product1 = []
list_product2 = []
list_product3 = []
list_product4 = []
list_product5 = []
list_product6 = []
list_product7 = []
list_product8 = []
list_product9 = []
list_product10 = []
list_product11 = []
while c < 10:
    list_stores_link[c].click()
    time.sleep(4)
    a = 1
    list_possible_content = browser.find_elements(By.CLASS_NAME, "col-md-9.col-sm-9")
    while a < len(list_possible_content):
        if len(list_possible_content[a].text) > 0:
            con = list_possible_content[a].text
            pro = con.split("\n")[3].split(",")  # Product List
            for ele in pro:
                list_sub_product.append(ele)
            list_product.append(list_sub_product)
            list_sub_product=list()
        a = a + 1
    browser.get("https://exhibitoremanual.com/packplusdelhi20/elist/exhibitorlist.aspx")
    list_stores_link = browser.find_elements(By.CLASS_NAME, "viewdetails")
    c = c + 1
    #list_website.append(con.split("\n")[8])
#           list_store_name.append(list_raw_stores[a - 1])#STore Name
      #      q.append(con.split("\n")[0])#DEscriptin
         #   r.append(con.split("\n")[3])#Product List
"""           list_address.append(con.split("\n")[6])#Actual Address
            add = con.split("\n")[6]
            list_add = add.split(" ")
            if len(list_add[-2])==6:
                list_pin.append(list_add[-2])
                list_state.append(list_add[-3])
                list_city.append(list_add[-4])
            else:
                list_state.append(list_add[-2])
                list_city.append(list_add[-3])
                list_pin.append("Missing")"""


         #   q.append(con.split("\n")[8])#ACtual Website
for x in list_product:
    z = 1
    try:
        list_product1.append(x[-z])
    except:
        list_product1.append("Missing")
    z = z+1
    try:
        list_product2.append(x[-z])
    except:
        list_product2.append("Missing")
    z = z+1
    try:
        list_product3.append(x[-z])
    except:
        list_product3.append("Missing")
    z = z+1
    try:
        list_product4.append(x[-z])
    except:
        list_product4.append("Missing")
    z = z+1
    try:
        list_product5.append(x[-z])
    except:
        list_product5.append("Missing")
    z = z+1
    try:
        list_product6.append(x[-z])
    except:
        list_product6.append("Missing")
    z = z+1
    try:
        list_product7.append(x[-z])
    except:
        list_product7.append("Missing")
    z = z+1
    try:
        list_product8.append(x[-z])
    except:
        list_product8.append("Missing")
    z = z+1
    try:
        list_product9.append(x[-z])
    except:
        list_product9.append("Missing")
    z = z+1
    try:
        list_product10.append(x[-z])
    except:
        list_product10.append("Missing")
    z = z+1
    try:
        list_product11.append(x[-z])
    except:
        list_product11.append("Missing")

for ele in list_product:
    print(ele)
print(list_product1)
print(list_product2)
print(list_product3)
print(list_product4)
print(list_product5)
print(list_product6)
print(list_product7)
print(list_product8)
print(list_product9)
print(list_product10)
print(list_product11)

