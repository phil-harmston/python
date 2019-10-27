__name__=="-__main__"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.options import Options
import sqlite3
import time
from bs4 import BeautifulSoup as bs
import re
from lxml import etree


con = sqlite3.connect('./dbase/uabc.db')
c = con.cursor()

# id of the Item CSC Code
id = "ContentPlaceHolderBody_tbCscCode"

# name of the Item Name box
name = "ctl00$ContentPlaceHolderBody$tbCscCode"
#options = Options()
#options.add_argument("--headless")
driver = webdriver.Chrome('/snap/bin/chromium.chromedriver' ) #, options=options


driver.get("https://webapps2.abc.utah.gov/Production/OnlineInventoryQuery/IQ/InventoryQuery.aspx")
itemNameSearchBox = driver.find_element_by_name("ctl00$ContentPlaceHolderBody$tbItemName")

c.execute("SELECT * from LIQUOR WHERE PRODUCT_NAME LIKE 'teq%'")
data = c.fetchall()
#for d in data:
    #print(d[0])

def main():
# //////////////////////////////////////////////////////
#itemIdSearchBox = driver.find_element_by_id(id)
    for d in data:
        sku = d[0]
        #print(sku)
        itemIdSearchBox = driver.find_element_by_id(id)
        itemIdSearchBox.send_keys(sku)
        itemIdSearchBox.send_keys(Keys.ENTER)
        html = driver.page_source
        soup_it(html)
        time.sleep(10)
    #driver.implicitly_wait(50000)
#///////////////////////////////////////////////////////

def soup_it(html):
    soup = bs(html, 'lxml')
    status = soup.find('span', id="ContentPlaceHolderBody_lblStatus")
    try:
        print(status.text)
    except AttributeError:
        pass

    #status = re.findall('^>$<', str(status))

#searchbox.find_elements_by_name("ctl00$ContentPlaceHolderBody$hiddenItemId")

#driver.close()


if __name__ == "__main__":
    main()

