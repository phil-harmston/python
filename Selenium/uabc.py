from selenium import webdriver
from selenium.webdriver.common.keys import Keys


from selenium import webdriver
# id of the Item CSC Code
id = "ContentPlaceHolderBody_tbCscCode"

# name of the Item Name box
name = "ctl00$ContentPlaceHolderBody$tbCscCode"
driver = webdriver.Chrome('/snap/bin/chromium.chromedriver')

driver.get("https://webapps2.abc.utah.gov/Production/OnlineInventoryQuery/IQ/InventoryQuery.aspx")
#searchbox = driver.find_element_by_name(name)
itemNameSearchBox = driver.find_element_by_name("ctl00$ContentPlaceHolderBody$tbItemName")

#itemNameSearchBox.send_keys("rose")
#driver.implicitly_wait(10000)


itemIdSearchBox = driver.find_element_by_id(id)
itemIdSearchBox.send_keys("000133")
driver.implicitly_wait(5000)
itemIdSearchBox.send_keys(Keys.ENTER)
driver.implicitly_wait(5000)
#searchbox.find_elements_by_name("ctl00$ContentPlaceHolderBody$hiddenItemId")

#driver.close()



