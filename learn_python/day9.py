#函数
#
# def vote_stu():
#     score = 99
#     if score > 60:
#         if score >= 90:
#             print("可以参加评定三好学生")
#         else:
#             print("可以参加拼比优秀学生")
#     else:
#         print("不及格，什么都不能参加")
# vote_stu()

# def add_main(a,b, *c):
#     a = int(input("输入一个数字"))
#     b = int(input("输入一个数字"))
#     c = int(input("输入一个数字"))
#     return a + b + c
# print(add_main(1, 2, 3, 4))

# def judge_tran(a=1, b=2, c=1):
#     if a > 0 and b > 0 and 0 < c < a + b and \
#             a + c > b and b + c > a:
#         print("能组成三角形")
#     else:
#         print("不能组成三角形")
# judge_tran(a=1, b=2, c=1)
#
# def judge_tran(a, b, c):
#     if a > 0 and b > 0 and 0 < c < a + b and \
#             a + c > b and b + c > a:
#         print("能组成三角形")
#     else:
#         print("不能组成三角形")
# judge_tran(a=1, b=2, c=1)
# judge_tran(1, 2, 3)
#
# def plus(a,b,c):
#     d = a + b
#     e = c + a
#     return a,b,d,e
# #
# _,e,_,_ = plus(2,3,2)
# print(e)





#写一个读取csv文件的函数
# def csv_read(path):
#     with open("path",'r') as file:
#         import csv
#         reader = csv.reader(file)
#         data = [i for i in reader ]
#         print((data))
#
# print(csv_read('aaa.csv'))
#
# def calculate(a, b, c):
#     return a+b, a-c, a+b-c
#
# # 计算5+8-2的值
# a, b, c = calculate(5, 8, 2)
# print(a, b, c)
# _,_,c = calculate(3, 4, 5)
# print(c)
# def sqr(a, c,d):
#     return a**2+c**2, d**3+c**2
#
# # 计算3的平方＋5的平方
# f = sqr(3, 5, 7)
# print(f[0])


# def get_randow(n):
#     import random
#     return random.randint(1, n)
#
# import qrcode
#
# ima = qrcode.make('http://www.baidu.com')
# ima.save(r'test.png')




