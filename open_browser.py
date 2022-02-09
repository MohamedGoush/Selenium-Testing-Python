from lib2to3.pgen2 import driver
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")

driver.get("http://www.google.com")

print(driver.title)

driver.close()