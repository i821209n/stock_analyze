from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time

# Set up Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run Chrome in headless mode
# chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration (necessary in headless mode)

url = "https://goodinfo.tw/StockInfo/StockBzPerformance.asp?STOCK_ID=2330"
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)
driver.get(url)
print(driver.title)
html = driver.page_source
# print(html)

# Find the "select" tag by its name or any other attribute
# select_element = Select(driver.find_element_by_name("your_select_name"))

# Find the select element with a specific onchange attribute
select_css_selector = 'select[onchange="ChgFinDetailSheet(this.value);"]'
select_element = driver.find_element(By.CSS_SELECTOR, select_css_selector)

# Now, you can interact with the select element as needed
# For example, you can change the selected option
select = Select(select_element)
select.select_by_index(3)  # Replace with the desired option index

time.sleep(2)

soup = BeautifulSoup(driver.page_source, 'lxml')
data = soup.select_one("#txtFinDetailData")

dfs = pd.read_html((data.prettify()))

df = dfs[0]

print(df.columns)
# print(soup.prettify())

# with open('index.html', 'w', encoding='utf-8',) as file:
#     file.write(soup.prettify())

driver.quit()