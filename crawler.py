import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os
import re

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
def isYear(string):
    # Define the regex pattern
    pattern = r'(\d+)Q(\d+)'
    try:
        # Match the pattern in the string
        match = re.match(pattern, string)
        if match:
            # Extract the numbers before and after "Q"
            before_q = int(match.group(1)) + 2000
            return before_q
        else:
            return int(string)
    except ValueError:
        return -1

def get_data(stock_num):
    start_time = time.time()
    if not os.path.exists('csv_file.csv'):
        # Set up Chrome options for headless mode
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # Run Chrome in headless mode
        # chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration (necessary in headless mode)

        url = f"https://goodinfo.tw/StockInfo/StockBzPerformance.asp?STOCK_ID={stock_num}"
        # headers = {
        #     "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        # }

        driver = webdriver.Chrome(options=chrome_options)
        driver.implicitly_wait(10)
        try:
            driver.get(url)
            # res = requests.get(url, headers=headers)
        except:
            print(f"wrong url : {url}")
            return
        # res.encoding = "utf-8"
        print(driver.title)

        # Find the select element with a specific onchange attribute
        select_css_selector = 'select[onchange="ChgFinDetailSheet(this.value);"]'
        select_element = driver.find_element(By.CSS_SELECTOR, select_css_selector)

        # Now, you can interact with the select element as needed
        # For example, you can change the selected option
        select = Select(select_element)
        select.select_by_index(0)  # Replace with the desired option index
        time.sleep(1)

        soup = BeautifulSoup(driver.page_source, "lxml")
        # print(f"Title : {soup.title.text}")
        # link_tag = soup.find_all('a', class_='link_blue')
        # print(link_tag)

        data = soup.select_one("#txtFinDetailData")

        dfs = pd.read_html((data.prettify()))

        df = dfs[0]
        # print(df)
        print(df.columns)

        list_close = [float(x) for x in (df['年度股價(元)']['收盤']) if isfloat(x)]
        print(list_close)
        # print(df['年度']['年度'])
        list_year = [isYear(x) for x in (df['年度']['年度']) if isYear(x) > 0]
        print(list_year)

        data_input = pd.DataFrame({'year':list_year, 'close_price':list_close})
        data_input = data_input.sort_values(by='year').reset_index(drop=True)
        data_input.index = data_input.year

        print(data_input)

        data_input.to_csv('csv_file.csv')
        # df.to_excel('excel_file.xlsx')

    # Read the CSV file into a DataFrame
    df = pd.read_csv('csv_file.csv')
    print(df)
    # print(df.columns)

    driver.quit()

    print(f"running time : {time.time() - start_time}")

