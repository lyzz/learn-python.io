#xpatch

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

import time

driver = webdriver.Chrome()

driver.get('http://mall4j-admin.gz-yami.com')

driver.implicitly_wait(30)   #隐性延迟30s

username = driver.find_element_by_xpath('//div[@class="info el-input"]/input[@type="text"]')

username.send_keys('admin')

password = driver.find_element_by_xpath('//div[@class="info el-input"]/input[@type="password"]')

password.send_keys('123456')

time.sleep(30)

login_button = driver.find_element_by_css_selector(' form > div:nth-child(4) > div > div >input')
login_button.click()


# chanpingguanli = driver.find_element_by_xpath('//ul[@role="menubar"]/li[@role="menuitem"][2]'
#                                               '/div[@class="el-submenu__title"]')
# chanpingguanli.click()
#
#
# cpgl_child = driver.find_element_by_xpath('//ul[@role="menubar"]/li[@role="menuitem"][2]/ul[@role="menu"][1]'
#                                           '/li[@role="menuitem"][1]')
# cpgl_child.click()

#订单管理

dingdan_gl = driver.find_element_by_xpath('//ul[@role="menubar"]/li[@role="menuitem"][5]'
                                          '/div[@class="el-submenu__title"][1]')

dingdan_gl.click()

ddgl_child = driver.find_element_by_xpath('//ul[@role="menubar"]/li[@role="menuitem"][5]'
                                          '/ul[@role="menu"]/li[@role="menuitem"]')
ddgl_child.click()

#打印第一个订单

# order = driver.find_element_by_xpath('//div[@class="content"]/div[@class="prod"][2]/div[@class="prod-tit"][1]/span[1]')
# order_text = order.text
# print(type(order_text))
# print('订单编号：',order_text)
# print(order_text)

# driver.quit()
#打印所有的订单编号


orders =  driver.find_elements_by_xpath('//div[@class="content"]/div[@class="prod"]/div[@class="prod-tit"]/span[1]')
# print(type(orders))

orders_lis = list(orders)
# print(type(orders_lis))
# print(orders_lis)

# print(orders_text)

# for x in range(len(orders_lis)):
#     order = orders_lis[x]
#     print(order.text)

# driver.quit()
# for x in range(len(orders)):
#     order = orders[x]
#     print(order.text)

# for x in range(orders_text):
#     order = orders_text[x]
#     print(order)

# print("----------------------------------------------")

# page_link = driver.find_element_by_xpath('//li[@class="number"]')

# ActionChains(driver).move_to_element(page_link).click().perform()