# sum_1 = [1, 3, 4, 5, 6, 6]
# for i in range(len(sum_1)):
#     sum_2 = sum_1[i]
#     print(sum_2)
#
#
# sum = 'dfdfsdfsdfds'
# sum_list = list(sum)
# print(sum_list)


from selenium import webdriver
from selenium.webdriver.common.alert import  Alert
import time


driver = webdriver.Chrome()

driver.get('https://mail.qq.com/cgi-bin/loginpage')


driver.implicitly_wait(20)
driver.switch_to.frame('login_frame')
login_qq = driver.find_element_by_id('switcher_plogin')
login_qq.click()

username_input = driver.find_element_by_xpath('//input[@id="u"]').send_keys('389172793')
password_input = driver.find_element_by_id('p').send_keys('yzz211227')



zd_login = driver.find_element_by_id('p_low_login_enable').click()



login_buton = driver.find_element_by_id('login_button').click()

time.sleep(10)
# driver.switch_to.alert

# driver.find_element_by_id('folder_1').click()
caogao = driver.find_element_by_id('folder_4').click()


driver.find_element_by_xpath('//div[@class="toarea"]/table[@class="i M"][1]'
                             '/tbody/tr/td[@class="l"]/table[@class="i "]/tbody/tr/td[@class="gt"]/div[@class="tf no"]'





'''3个面补漆
1 次小保养
2 次代驾
浦东机场停车2次

救援无线
700元百联卡
'''













