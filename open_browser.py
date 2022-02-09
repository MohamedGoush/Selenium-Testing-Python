from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")

driver.get("http://www.google.com")

print(driver.title)

driver.close()