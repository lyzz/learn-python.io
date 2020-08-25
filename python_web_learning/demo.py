# sum_1 = [1, 3, 4, 5, 6, 6]
# for i in range(len(sum_1)):
#     sum_2 = sum_1[i]
#     print(sum_2)
# # #
# #
# # sum = 'dfdfsdfsdfds'
# # sum_list = list(sum)
# # print(sum_list)


# from selenium import webdriver
# from selenium.webdriver.common.alert import  Alert
# import time


# driver = webdriver.Chrome()

# driver.get('https://mail.qq.com/cgi-bin/loginpage')


# driver.implicitly_wait(20)
# driver.switch_to.frame('login_frame')
# login_qq = driver.find_element_by_id('switcher_plogin')
# login_qq.click()

# username_input = driver.find_element_by_xpath('//input[@id="u"]').send_keys('389172793')
# password_input = driver.find_element_by_id('p').send_keys('yzz211227')



# zd_login = driver.find_element_by_id('p_low_login_enable').click()



# login_buton = driver.find_element_by_id('login_button').click()

# time.sleep(10)
# # driver.switch_to.alert

# # driver.find_element_by_id('folder_1').click()
# caogao = driver.find_element_by_id('folder_4').click()


# driver.find_element_by_xpath('//div[@class="toarea"]/table[@class="i M"][1]'
#                              '/tbody/tr/td[@class="l"]/table[@class="i "]/tbody/tr/td[@class="gt"]/div[@class="tf no"]'





'''3个面补漆
1 次小保养
2 次代驾
浦东机场停车2次

救援无线
700元百联卡
'''













import requests
from lxml import etree
import csv
# csv后缀的格式就是excel文件打开的格式，我们等于是直接存入了excel中
import time

headers = {
    "User-Agent": "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14"
}

f = open("软件测试工程师.cvs","w",newline="")
writer = csv.writer(f)
writer.writerow(['编号','职位名', '公司名', '工作地点', '薪资',  '发布时间'])

i = 1
for page in range(1,42):
    requests_get = requests.get(
        f"https://search.51job.com/list/020000,000000,0000,00,9,99,%25E8%25BD%25AF%25E4%25BB%25B6%25E6%25B5%258B%25E8%25AF%2595%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=",headers=headers
        )
    requests_get.encoding="GBK"
    if requests_get.status_code == 200:
        html = etree.HTML(requests_get.text)
        els = html.xpath("//div[@class='el']")[4:]
        for el in els:
            jobname = str(el.xpath("p[contains(@class,'t1')]/span/a/@title")).strip("[']")
            jobcom = str(el.xpath("span[@class='t2']/a/@titlr")).strip("[']")
            jobaddress = str(el.xpath("span[@class='t3']/text()")).strip("[']")
            jobsalary = str(el.xpath("span[@class='t4']/text()")).strip("[']")
            jobdate = str(el.xpath("span[@class='t5']/text()")).strip("[']")
            writer.writerow([i, jobname, jobcom, jobaddress, jobsalary, jobdate])
            i += 1
        print(f"第{page}页获取完毕")
