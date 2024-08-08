import requests
import pandas as pd

# 取得資料
# url = 'https://openapi.twse.com.tw/v1/opendata/t187ap05_P'
# response = requests.get(url)
# data = response.json()

# 將資料轉為 DataFrame 方便處理
# df = pd.DataFrame(data)

# 篩選出台積電的資料
# tsmc_data = df[df['公司代號'] == '2330']

# 顯示結果
# for i in range len(tsmc_data):
    # print(tsmc_data[i])

# 打印第一行的所有值
# print(tsmc_data.iloc[0, :])

# keys_list = list(df.columns)
# print(keys_list)

# 設定請求的URL和參數
url = 'https://mops.twse.com.tw/mops/web/ajax_t05st10_ifrs'
payload = {
    'encodeURIComponent': 1,
    'step': 1,
    'firstin': 1,
    'off': 1,
    'keyword4': '',
    'code1': '',
    'TYPEK2': '',
    'checkbtn': '',
    'queryName': 'co_id',
    'inpuType': 'co_id',
    'TYPEK': 'all',
    'isnew': 'false',
    'co_id': '2330',
    'year': '113',
    'month': '01'
}

# 發送POST請求
response = requests.post(url, data=payload)

# 確認請求成功
if response.status_code == 200:
    # 使用pandas從HTML表格中提取數據
    tables = pd.read_html(response.text)

    # 如果有多個表格，根據實際需求選擇需要的表格
    if tables:
        # 檢查提取的表格數量
        print(f"提取的表格數量: {len(tables)}")

        # 顯示提取的表格
        print("----------------------------")
        for i, table in enumerate(tables):
            print(f"表格 {i+1}:\n{table}\n")
            print("----------------------------")

        df = tables[1]  # 假設我們需要第一個表格

        result = df[df["項目"] == "本月"]["營業收入淨額"].values[0]
        print(f"本月營收 : {result} (單位：新台幣仟元)")

    else:
        print("未找到任何表格數據。")
else:
    print(f"請求失敗，狀態碼: {response.status_code}")

