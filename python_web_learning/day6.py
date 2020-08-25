from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains  #倒入鼠标操作模块

driver = webdriver.Chrome()

driver.get('https://www.baidu.com')

more_link = driver.find_element_by_xpath('//a[@name="tj_briicon"]')

ActionChains(driver).move_to_element(more_link).pause(10).perform()    #鼠标停放在菜单上10s

mp3_link = driver.find_element_by_xpath('//a[@name="tj_mp3"]')

ActionChains(driver).move_to_element(mp3_link).click().perform()