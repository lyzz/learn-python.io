from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys




driver=webdriver.Chrome()
driver.get("http://www.baidu.com")

ss_input = driver.find_element_by_xpath('//input[@id="kw"]')
ss_input.click()

ActionChains(driver).move_to_element(ss_input).send_keys('abcdef').perform()
ActionChains(driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
# ActionChains(driver).
# #输入关键词内容
# driver.find_element_by_id("kw").send_keys("selenium")
# #删除键
# driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
#空格键
# driver.find_element_by_id("kw").send_keys(Keys.SPACE)
# #输入内容
# driver.find_element_by_id("kw").send_keys("教程")
# #全选(Ctrl+A)
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
# #剪切(Ctrl+X)
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
# #粘贴(Ctrl+V)
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'v')
# #回车键
# driver.find_element_by_id("kw").send_keys(Keys.ENTER)