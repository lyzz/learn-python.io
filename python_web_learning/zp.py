from selenium import webdriver
import time

driver = webdriver.Chrome()


url = "https://sou.zhaopin.com/?jl=538&sf=10001&st=15000&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3"

driver.get(url)

jsButton = driver.find_element_by_css_selector(' div.risk-warning__content>button')
jsButton.click()

driver.implicitly_wait(30)
# driver.maximize_window()

# driver.implicitly_wait(30)