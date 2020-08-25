# 求边长在10以内的所有整数边长的正方形面积
# print([i*i for i in range(1,11)])

# ls1 = ['1', [2, 4], 'a', (1, 'a'), {"c":"s"}, {3, '5'}, 66]
# # 列出列表里面的字符串做成一个列表
#
# print([i for i in ls1 if isinstance(i,str)])
# print([i for i in ls1 if type(i) == type("")])



#时间
# import time

# ticks = time.time()
# print('当前时间戳为:',ticks)


#datatime.datetime

# from datetime import date

# #
# today = date.today()
# print(today, type(today))
# #
from datetime import datetime
# # # 获取当前的时间
now = datetime.now()

print(datetime.today())
print(now)
# print(str(now),type(str(now)))

# now_str = "2020-02-04 21:00:04"
# #
# a = datetime.strptime(now_str,"%Y-%m-%d %H:%M:%S")
# a1 = datetime.strptime("2020-02-04", "%Y-%m-%d")
# print(a,a1)
#
# import os
# # print(os.path.exists("love_python1"))  #判断文件夹是否存在
# # #
# # os.makedirs("love_python1")
# # os.system("python day1.py")    #运行一个python文件