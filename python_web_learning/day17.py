import requests
from lxml import etree
import csv
# csv后缀的格式就是excel文件打开的格式，我们等于是直接存入了excel中
import time

headers = {
    "User-Agent": "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14"
}

f = open("软件测试工程师20200813.cvs","w",newline="")
writer = csv.writer(f)
writer.writerow(['编号','职位名', '公司名', '工作地点', '薪资',  '发布时间'])

i = 1
for page in range(1,42):
    requests_get = requests.get(
        f"https://search.51job.com/list/020000,000000,0000,00,9,99,%25E8%25BD%25AF%25E4%25BB%25B6%25E6%25B5%258B%25E8%25AF%2595%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=",headers=headers
        )
    requests_get.encoding="GBK"
    if requests_get.status_code == 200:
        html = etree.HTML(requests_get.text)
        els = html.xpath("//div[@class='el']")[4:]
        for el in els:
            jobname = str(el.xpath("p[contains(@class,'t1')]/span/a/@title")).strip("[']")
            jobcom = str(el.xpath("span[@class='t2']/a/@title")).strip("[']")
            jobaddress = str(el.xpath("span[@class='t3']/text()")).strip("[']")
            jobsalary = str(el.xpath("span[@class='t4']/text()")).strip("[']")
            jobdate = str(el.xpath("span[@class='t5']/text()")).strip("[']")
            writer.writerow([i, jobname, jobcom, jobaddress, jobsalary, jobdate])
            i += 1
        print(f"第{page}页获取完毕")







