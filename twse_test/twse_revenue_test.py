import requests
import pandas as pd

# 取得資料
url = 'https://openapi.twse.com.tw/v1/opendata/t187ap05_P'
response = requests.get(url)
data = response.json()

# 將資料轉為 DataFrame 方便處理
df = pd.DataFrame(data)

# 篩選出台積電的資料
tsmc_data = df[df['公司代號'] == '2330']

# 顯示結果
# for i in range len(tsmc_data):
    # print(tsmc_data[i])

# 打印第一行的所有值
# print(tsmc_data.iloc[0, :])

keys_list = list(df.columns)
print(keys_list)
