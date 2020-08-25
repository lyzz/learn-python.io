from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()

driver.implicitly_wait(20)  #全局隐式等待20s

driver.maximize_window()    #窗口最大化

driver.get('http://wufazhuce.com/')

One_text = driver.find_element_by_css_selector('div.fp-one-cita').text
print(One_text)

driver.get('https://qzone.qq.com/')

driver.switch_to.frame('login_frame')

driver.find_element_by_xpath('//div[@class="qlogin_list"]/a[@hidefocus="true"]/span[@class="img_out_focus"]').click()

time.sleep(10)
driver.find_element_by_xpath('//div[@class="nav-list-inner"]').click()

QQZone_input = driver.find_element_by_xpath('//div[@id="QM_Mood_Poster_Container"]')

ActionChains(driver).move_to_element(QQZone_input).click().pause(4).perform()

ActionChains(driver).send_keys(One_text).perform()

tijiao_botton = driver.find_element_by_xpath('//div[@class="op"]')

ActionChains(driver).move_to_element(tijiao_botton).click().perform()

time.sleep(10)
driver.find_element_by_xpath('//a[@class="arrow-down"]').click()


# driver.switch_to.alert
# # text = driver.switch_to.alert().text
# # print(text)
# print('text==', Alert(driver).text)
# # time.sleep(5)
# # Alert(driver).dismiss()      #确定
