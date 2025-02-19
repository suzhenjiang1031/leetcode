import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

# 设置 Selenium 配置
chrome_options = Options()
chrome_options.add_argument('--headless')  # 设置无头模式，不弹出浏览器
chrome_options.add_argument('--disable-gpu')  # 禁用 GPU 加速
chrome_options.add_argument('--no-sandbox')  # 无沙盒模式

# 创建 WebDriver 实例
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# 目标网址（假设的新闻网站）
url = 'https://www.example-news-website.com/'

# 打开网页
driver.get(url)

# 等待页面加载
time.sleep(3)

# 模拟滚动页面，加载更多内容（如果网站有动态加载的内容）
for _ in range(3):  # 滚动三次
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

# 获取网页内容
html = driver.page_source

# 解析网页
soup = BeautifulSoup(html, 'html.parser')

# 创建一个空列表，用来存储抓取的数据
news_data = []

# 提取新闻条目
articles = soup.find_all('article', class_='news-item')  # 假设新闻的每个条目在 <article class="news-item"> 中

for article in articles:
    title = article.find('h2').get_text(strip=True)  # 新闻标题
    link = article.find('a')['href']  # 新闻链接
    pub_date = article.find('time').get_text(strip=True)  # 发布时间
    summary = article.find('p').get_text(strip=True)  # 新闻简介
    
    # 将数据添加到列表
    news_data.append({
        'Title': title,
        'Link': link,
        'Publish Date': pub_date,
        'Summary': summary
    })

# 将抓取的数据保存到 CSV 文件
df = pd.DataFrame(news_data)
df.to_csv('news_data.csv', index=False, encoding='utf-8')

# 关闭 WebDriver
driver.quit()

print("爬取完成，数据已保存到 'news_data.csv' 文件中")
