import requests
from bs4 import BeautifulSoup
import pandas as pd

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
def isint(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

def get_data(stock_num):
    url = f"https://goodinfo.tw/StockInfo/StockBzPerformance.asp?STOCK_ID={stock_num}"
    headers = {
        "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }
    try:
        res = requests.get(url, headers=headers)
    except:
        print(f"wrong url : {url}")
        return
    res.encoding = "utf-8"

    soup = BeautifulSoup(res.text, "lxml")
    print(f"Title : {soup.title.text}")
    # link_tag = soup.find_all('a', class_='link_blue')
    # print(link_tag)

    data = soup.select_one("#txtFinDetailData")

    dfs = pd.read_html((data.prettify()))

    df = dfs[0]

    # print(df)

