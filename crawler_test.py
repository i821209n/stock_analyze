import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

url = "https://goodinfo.tw/StockInfo/StockBzPerformance.asp?STOCK_ID=2330"
headers = {
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}
res = requests.get(url, headers=headers)
res.encoding = "utf-8"

soup = BeautifulSoup(res.text, "lxml")
data = soup.select_one("#txtFinDetailData")

dfs = pd.read_html((data.prettify()))

df = dfs[0]

print(df.columns)

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
    
list_close = [float(df['年度股價(元)']['收盤'][i]) for i in range(len(df['年度股價(元)']['收盤'])) if isfloat(df['年度股價(元)']['收盤'][i])]
list_int = [int(df['年度']['年度'][i]) for i in range(len(df['年度']['年度'])) if isint(df['年度']['年度'][i])and isfloat(df['年度股價(元)']['收盤'][i])]
list_year = [list_int[0]+1]+list_int
print(list_close, " ", len(list_close))
print(list_int, " ", len(list_int))
print(list_year, " ", len(list_year))

data_input = pd.DataFrame({'year':list_year, 'close_price':list_close})
data_input = data_input.sort_values(by='year').reset_index(drop=True)
data_input.index = data_input.year

print(data_input)

# Plotting the line chart
plt.figure(figsize=(8, 6))
plt.plot(data_input['year'], data_input['close_price'], marker='o', linestyle='-')

# Adding labels and title
plt.xlabel('year')
plt.ylabel('close_price')
plt.title('close_price of years')

# Display the plot
plt.grid(True)
plt.show()