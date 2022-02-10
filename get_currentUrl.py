from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")

driver.get("http://www.amazon.com")

print(driver.title)     # Get the Title Of the Page
print(driver.current_url)   # Get the Current URL of the Page

# driver.close()  # It Close a Current Tab of the Browser

driver.quit()   # It Close the Browser Application.