from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")

driver.get("http://www.google.com")

print(driver.title)
print(driver.current_url)

driver.close()