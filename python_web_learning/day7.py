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

# chanpingguanli = driver.find_element_by_xpath('//ul[@role="menubar"]/li[@role="menuitem"][2]'
#                                               '/div[@class="el-submenu__title"]')
# chanpingguanli.click()
#
#
# cpgl_child = driver.find_element_by_xpath('//ul[@role="menubar"]/li[@role="menuitem"][2]/ul[@role="menu"][1]'
#                                           '/li[@role="menuitem"][1]')
# cpgl_child.click()

# button_update_click = driver.find_element_by_xpath('//div[@class="el-table__body-wrapper is-scrolling-none"]'
#                                                    '/table[@class="el-table__body"]/tbody/tr[@class="el-table__row"][1]'
#                                                    '/td[@class="el-table_5_column_30 is-center  is-hidden"]'
#                                                    '/div[@class="cell"]/button[@type="button"][1]')
#
# ActionChains(driver).move_to_element(button_update_click).click().perform()


mdguanli = driver.find_element_by_xpath('//ul[@role="menubar"]/li[@role="menuitem"][3]'
                                        '/div[@class="el-submenu__title"][1]')
mdguanli.click()

mdgl_child = driver.find_element_by_xpath('//ul[@role="menubar"]/li[@role="menuitem"][3]/ul[@role="menu"]'
                                          '/li[@role="menuitem"][1]')

mdgl_child.click()



gongao_click = driver.find_element_by_xpath('//div[@class="el-tooltip avue-input"]'
                                            '/div[@class="el-input el-input--small el-input--suffix"]'
                                            '/input[@type="text"]')

gongao_click.send_keys('22222')

time.sleep(10)

