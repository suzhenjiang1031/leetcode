import requests
from bs4 import BeautifulSoup

# 目标 URL
url = 'https://www.163.com'

# 定义请求头，伪装成浏览器
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

# 发送 HTTP GET 请求，带上 headers
response = requests.get(url, headers=headers)

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

# 获取所有的新闻链接（网易新闻的新闻链接一般都在 <a> 标签中）
links = soup.find_all('a', href=True)

# 输出前 5 个新闻标题及其链接
count = 0
for link in links:
    title = link.get_text(strip=True)  # 获取文本并去除空格
    href = link['href']  # 获取链接
    if title and href.startswith('http'):  # 如果链接以 http 开头，且有标题
        print(f"新闻标题：{title}")
        print(f"链接：{href}")
        print("-" * 50)

        count += 1
        if count == 5:  # 只爬取前 5 条新闻
            break
