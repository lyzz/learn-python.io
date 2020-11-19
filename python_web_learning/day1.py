#selenium 文档：https://selenium-python.readthedocs.io/#

#step1:下载chrome 浏览器，查看版本号
#step2:下载chrome插件：https://npm.taobao.org/,选择对应chrome浏览器的版本,选择win32.zip下载
#step3:将下载完的.exe文件拖到python的根目录

from selenium import webdriver

import time 

#打开浏览器

driver = webdriver.Chrome()

driver.get("https://www.baidu.com")

# driver.quit()
