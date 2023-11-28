from selenium import webdriver
from bs4 import BeautifulSoup
import requests

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://rate.bot.com.tw/xrt?Lang=zh-TW')
print(driver.title)
html = driver.page_source
print(html)

soup = BeautifulSoup(driver.page_source, 'lxml')
print(soup.prettify())

with open('index.html', 'w', encoding='utf-8',) as file:
    file.write(soup.prettify())

driver.quit()