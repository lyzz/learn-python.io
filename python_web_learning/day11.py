from selenium import webdriver
from selenium.webdriver.common.alert import Alert
#
import time
#
# driver = webdriver.Chrome()
#
# driver.get('http://mall4j-admin.gz-yami.com')
#
# driver.implicitly_wait(30)   #隐性延迟30s
#
# username = driver.find_element_by_css_selector('form>div:nth-child(1)>div.el-form-item__content>div.info '
#                                                '>input.el-input__inner')
# username.send_keys('admin')
#
# password = driver.find_element_by_css_selector('form>div:nth-child(2)>div.el-form-item__content>div.info >'
#                                                'input.el-input__inner')
#
# password.send_keys('123456')
#
# # ##  等待10秒，手动输入验证码 并手动点击登陆
# time.sleep(10)
#
# login_button = driver.find_element_by_xpath('//input[@type="button"]').click()
#
# time.sleep(5)
# chanpinguanli = driver.find_element_by_css_selector('ul.site-sidebar__menu.el-menu>li:nth-child(2)')
#
# chanpinguanli.click()
#
# time.sleep(5)
# chanpinguanli_child = driver.find_element_by_css_selector('//ul[@role="menubar"]/li[@role="menuitem"][2]'
#                                                           '/ul[@role="menu"]/li[@role="menuitem"][1]')
#
# chanpinguanli_child.click()
#
driver = webdriver.Chrome()

driver.get('C:\\Users\\Administrator\\Desktop\\python_web_learning\\aler弹窗.html')

driver.find_element_by_id('alert').click()

driver.switch_to.alert
# text = driver.switch_to.alert().text
# print(text)
print('text==', Alert(driver).text)
time.sleep(5)
Alert(driver).accept()      #确定


driver.find_element_by_id('confirm').click()
print('text1==', Alert(driver).text)
time.sleep(5)
Alert(driver).dismiss()

driver.find_element_by_id('prompt').click()
print('text2==',Alert(driver).text)
time.sleep(3)
Alert(driver).accept()