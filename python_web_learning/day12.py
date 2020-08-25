from selenium import webdriver

mobile_emulation = { "deviceName": 'iPad Pro'}

chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

driver = webdriver.Chrome(desired_capabilities = chrome_options.to_capabilities())
driver.get('https://www.baidu.com')


