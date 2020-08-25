from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.get('https://login.51job.com/login.php?')

driver.find_element_by_xpath('//form/div[1]/div/input').send_keys('15901635376')
driver.find_element_by_xpath('//form/div[2]/div/input').send_keys('Yzz211227')
driver.find_element_by_css_selector('div>button').click()

driver.find_element_by_link_text('职位搜索').click()

searchInput = driver.find_element_by_xpath('//div[1]/div/p/input')

ActionChains(driver).move_to_element(searchInput).click().send_keys('软件测试工程师').perform()

driver.implicitly_wait(5)
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="KwdSearchResult"]/span[2]').click()



driver.find_element_by_link_text('1-1.5万').click()

# zw = driver.find_elements_by_xpath('//p/span/a')
# print(zw)
# for i in range(len(zw)):
#     j = zw[i]
#     print(i)


zw_List =driver.find_element_by_xpath('//*[@id="resultList"]/div[4]/p/span/a').click()

# time.sleep(3)


gwze = gw_text=driver.find_elements_by_xpath('/html/body/div/div[1]/div[2]/div[2]/div[4]/div[3]/div[2]/p[1]/span')
print(gwze)

# print(gw_text[0])


# gw_text = gw.text
# print(type(gw_text))
# print(gw_text)
# for i in zw_List:
#     print(i)   