# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get('https://mail.qq.com/')
#
# driver.switch_to.frame('login_frame')
#
# driver.find_element_by_xpath('//input[@class="inputstyle"]').send_keys('389172793@qq.com')


from selenium import webdriver
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
