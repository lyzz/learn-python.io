from selenium import webdriver
from selenium.webdriver.common.by import By
#打开浏览器

driver = webdriver.Chrome()

driver.get("https://www.baidu.com")

# link = driver.find_element_by_link_text('新闻')  #链接
# link = driver.find_element_by_partial_link_text('新')   #模糊查询
# link.click()


# baidu_input = driver.find_element_by_name('kw')

# baidu_input = driver.find_element_by_class_name('s_ipt')
# baidu_input.clear()
#
# baidu_input.send_keys('hellow  world')
#
# baidu_button = driver.find_element_by_id('su')
#
# baidu_button.click()