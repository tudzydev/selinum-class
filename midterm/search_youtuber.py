from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://www.youtube.com")

search = driver.find_element(
    By.NAME,
    "search_query"
)

search.send_keys(
    "Bie The Ska",
    Keys.ENTER
)

input("กด Enter เพื่อปิด...")
driver.quit()