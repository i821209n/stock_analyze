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

webdriver_path = "/path/to/your/webdriver"

# url = "https://goodinfo.tw/StockInfo/StockBzPerformance.asp?STOCK_ID=2330"
url = "https://goodinfo.tw/tw/StockFinDetail.asp?RPT_CAT=XX_M_QUAR_ACC&STOCK_ID=2330"
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)
driver.get(url)
print(driver.title)
# html = driver.page_source
# print(html)

# Find the "select" tag by its name or any other attribute
# select_element = Select(driver.find_element_by_name("your_select_name"))

# Find the select element with a specific onchange attribute
select_css_selector = 'select[id="RPT_CAT"]'
select_element = driver.find_element(By.CSS_SELECTOR, select_css_selector)
# Now, you can interact with the select element as needed
# For example, you can change the selected option
select = Select(select_element)
# all_options = select.options
# for option in all_options:
#     print(option.text)
select.select_by_visible_text("合併報表 – 年度")
time.sleep(1)
select_css_selector = 'select[id="QRY_TIME"]'
select_element = driver.find_element(By.CSS_SELECTOR, select_css_selector)
select = Select(select_element)
select.select_by_index(0)  # Replace with the desired option index
time.sleep(1)
# button = driver.find_element(By.CSS_SELECTOR, 'input[value="匯出XLS"]')
# button.click()

# time.sleep(10)

soup = BeautifulSoup(driver.page_source, 'lxml')
data = soup.select_one("#tblFinDetail")

dfs = pd.read_html((data.prettify()))

df1 = dfs[0]

select.select_by_index(12)  # Replace with the desired option index
time.sleep(1)
soup = BeautifulSoup(driver.page_source, 'lxml')
data = soup.select_one("#tblFinDetail")
dfs = pd.read_html((data.prettify()))
df2 = dfs[0]

print(df1.columns)
print(df1)
print(df2.columns)
print(df2)
# del df[df.columns[0]]
combined_df = pd.merge(df1, df2, on='獲利能力')  # Change 'common_column' to the actual common column
print(combined_df.columns)
print(combined_df)
# print(soup.prettify())
combined_df.to_csv('csv_file.csv', index=False)

# with open('index.html', 'w', encoding='utf-8',) as file:
#     file.write(soup.prettify())

driver.quit()