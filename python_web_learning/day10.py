from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://cn.bing.com")

driver.find_element_by_css_selector('#sb_form_q').send_keys('Hello world')

driver.find_element_by_css_selector('#sb_form_q').submit()
wins1 = driver.window_handles       #显示所有窗口
print(len(wins1),'be opend')

driver.find_element_by_xpath('//ol[@id="b_results"]/li[@class="b_algo"][1]/h2/a[@target="_blank"]').click()

print('before switch window:', driver.current_url)

wins2 = driver.window_handles
print(len(wins2),'be opend')

driver.switch_to.window(wins2[1])
print('after switch window:', driver.current_url)

driver.find_element_by_id('query').clear()
driver.find_element_by_id('query').send_keys('world')



# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# import time
#
# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com/')
#
# driver.find_element_by_xpath('//*[@id="kw"]').send_keys('王力宏')
# driver.find_element_by_xpath('//input[@id="su"]').click()
# # 显示所有窗口
# wins = driver.window_handles
#
# time.sleep(3)
# # 打开新的窗口
# driver.find_element_by_xpath('//*[@id="1"]/h3/a ').click()
# # 判断新窗口是否已经打开
# WebDriverWait(driver, 5, 1).until(EC.new_window_is_opened(wins))
# # 切换窗口
# # 1.获取所有窗口
# wins1 = driver.window_handles
# # 2.切换到新窗口
# driver.switch_to.window(wins1[-1])


