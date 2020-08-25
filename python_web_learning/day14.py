from selenium import webdriver
import time

driver = webdriver.Chrome()

# 最大化浏览器窗口

driver.maximize_window()

driver.get('https://www.baidu.com')

driver.find_element_by_id('kw').send_keys('hello world')
driver.find_element_by_css_selector('#su').click()

time.sleep(3)

driver.refresh()     #刷新

driver.back()   #返回上一页

driver.minimize_window()    #最小化窗口

# driver.close()
driver.quit()   #关闭窗口