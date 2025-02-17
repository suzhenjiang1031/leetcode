import requests
from bs4 import BeautifulSoup

# 目标 URL
url = 'http://quotes.toscrape.com'

# 发送 HTTP GET 请求
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    print("成功获取网页内容")
else:
    print(f"请求失败，状态码：{response.status_code}")
    exit()

# 解析网页内容
soup = BeautifulSoup(response.text, 'html.parser')

# 获取网页标题
title = soup.title.string
print(f"网页标题：{title}")

# 获取所有名言及其作者
quotes = soup.find_all('div', class_='quote')
for quote in quotes:
    text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    print(f"名言：{text}\n作者：{author}\n")
