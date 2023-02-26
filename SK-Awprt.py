from selenium import webdriver
import time

url = httpswww.example.com  # 替换为你要刷新的网页地址

# 创建Chrome浏览器实例
driver = webdriver.Chrome()

while True
    driver.get(url)  # 打开网页
    time.sleep(10)   # 等待10秒后刷新
