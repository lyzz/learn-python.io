from selenium import webdriver
driver = webdriver.Chrome()


url = "https://wenku.baidu.com/view/de9287f726284b73f242336c1eb91a37f0113217.html"
driver.get(url)



one_text = driver.find_element_by_xpath('//div[@class="mod reader-page complex reader-page-3"]/div[@class="inner"]/div[@class="bd"]')

one_text = one_text.text

print(one_text)






