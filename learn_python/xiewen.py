import requests
import datetime
url = "http://vqzone.gtimg.com/1006_76728885644c4f369a55c33fc60896fc.f20.mp4" \
      "?ptype=http&vkey=AA93547CE44D30A35F082F4A3C869D60FD5C98476D10733CC1B2" \
      "215BE3C77A56DA48520A36E665F2AC8D6434B1DC91B3A952EFE8A257F10F&sdtfrom=v1000&owner=0"
# 视频的url地址
html = requests.get(url)
# content返回的的数据（注意，是二进制类型哦！）
html = html.content
start_down_time = datetime.datetime.now()
print('开始下载叶问,时间：{}'.format(start_down_time))
# 因为是二进制数据，所以必须要要采用wb的形式来写入
with open(r'C:\Users\38917\Desktop\yw\叶问4.mp4', 'wb') as f:
    f.write(html)
end_time = datetime.datetime.now()
print('电影下载结束,时间：{}'.format(end_time))