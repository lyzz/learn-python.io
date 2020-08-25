from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.baidu.com/')

driver.save_screenshot('./baidu.png')

form = driver.find_element_by_css_selector('form[id="form"]')

form.screenshot('./search.png')