import time
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# 使用 webdriver-manager 自动安装并配置 ChromeDriver
driver = webdriver.Chrome(ChromeDriverManager().install())

# 打开目标页面
url = "https://gwykl.fujian.gov.cn/kl2024/signupcount"
driver.get(url)

# 等待页面加载（可以根据实际情况调整等待时间）
time.sleep(5)

# 提取岗位数据
# 假设数据在某个表格中，您需要根据实际页面结构定位该表格
# 这里用的 XPath 是假设的，您需要根据实际页面结构调整
table = driver.find_element(By.XPATH, '//*[@id="signUpTable"]')  # 修改为实际表格的XPath
rows = table.find_elements(By.TAG_NAME, 'tr')

# 解析每一行的数据
data = []
for row in rows[1:]:  # 跳过表头
    columns = row.find_elements(By.TAG_NAME, 'td')
    if len(columns) > 0:
        position = columns[0].text  # 假设岗位名称在第一列
        signups = int(columns[1].text)  # 假设报名人数在第二列
        if signups <= 5:  # 如果报名人数小于5
            data.append({"Position": position, "Signups": signups})

# 关闭浏览器
driver.quit()

# 创建 DataFrame 并保存为 Excel 文件
df = pd.DataFrame(data)
df.to_excel('positions_with_less_than_5_signups.xlsx', index=False)

print("Excel 文件已生成")
