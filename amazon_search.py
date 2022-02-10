import imp
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")

driver.get("http://www.amazon.com")

search = driver.find_element_by_id("twotabsearchtextbox")
search.send_keys("iphone 13")
search.send_keys(Keys.RETURN)

# print(driver.title)     # Get the Title Of the Page
# print(driver.current_url)   # Get the Current URL of the Page
# print(driver.page_source)   # Get The Source Code of the Page

# driver.close()  # It Close a Current Tab of the Browser

# driver.quit()   # It Close the Browser Application.

