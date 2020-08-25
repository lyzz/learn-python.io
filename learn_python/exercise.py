# 字符串练习
#简述位、字节的关系
#:位：计算机的计算单位，代表0或者1 字节：一字节相当于8位

# 简述ascii、unicode、uft-8、gbk的关系
#
# ascii 英文编码，8个二进制位代表一个字母，总共可以有2的8次方减去1个等于255个
#
# gbk是中文编码，是用的16个二进制代表一个汉字，有点浪费空间
#
# uft-8也是中文编码，也是用的16个二进制代表一个汉字，但是能用8位表示就用位了

# 请写出“李杰”分别用utf-8的gbk编码所占的位数
# print(len((bytes("李杰", encoding='utf-8'))))
# print(len((bytes("李杰", encoding='gbk'))))

#变量命名
# 必须由数字，字母，下划线组成，不能以数字开头，不能用关键字，还有系统内置函数

# 有以下变量n1 = 5,请使用int提供的方法，得到该变量最少可以用多少个二进制位表示
# n1 = 5
# v = n1.bit_length()
# print(v)

name = " gouguoQ "
# a.移除name变量对应值的两边的空格，并输出移除后的内容
# print(name.strip())  #移除字符串头尾指定的字符（默认为空格）或字符序列。注意：该方法只能删除开头或是结尾的字符
#                     # ，不能删除中间部分的字符。
#
# # b.判断name变量对应的值是否以"go"开头，并输出结果
# print(name.startswith('go'))
#
# #c.判断name变量对应的值是否以"Q"结尾，并输出结果
# print(name.endswith("Q"))
#
# #d.将name变量对应的值中的"o"，替换为"p"，并输出结果
# print(name.replace("o","p"))

#e.将name变量对应的值根据"o"分割，并输出结果

# print(name.split("o"))
# print(type(name.split("o")))

#g.将name变量对应的值变大写，并输出结果
# print(name.upper())

# h.将name变量对应的值变成小写，并输出结果
# print(name.lower())

#i.请输出name变量对应的值的第二个字符？
# print(name[1])

# j.请输出name变量对应的值的前三个字符
# print(name[0:3])

#h.请输出name变量对应值的后2个字符
# print(name[5:8])
# print(name[-2:])

#l.请输出name变量中的值"Q的索引的位置
# print(name.index("Q"))
# print(name.find("Q"))
# v = len(name)
# for n in range(v):
#     if(name[n]) != "Q":
#         continue
#     else:
#         print(n, name[n])

#m.获取子序列，仅不包含最后一个字符，如：woaini则获取woain  root则获取roo
# print (name[0:-1])

# 21、字符串是否可以迭代对象？如果可以请使用for循环每一个元素？
# name1 = 'life is diffcult, but i use python!'
# for i in name1:
#     print(i)
#
#22、请用代码实现
#a.利用下划线将列表的每一个元素拼接成字符串  li = "gouguoqi"
# li = ['gou', 'gou', 'qi']
# v = '_'.join(li)
# print(v)

# 23、在python2和3中range有啥区别
# python2range可以直接帮我们打印出来范围内的数字，打印多了，得一直等着，占用库存
# python3里面，range创建之后，并不会把这些数字打印出来，而是在什么时候调用的时候才去一个一个的打印
#比如我for循环调用的时候才会挨个打印，这样就省内存了

# 25.计算用户输入的内容中有几个十进制小数？几个字母？
# content = input('请输入内容：计算十进制小数个数和字母个数 ')
# num = 0
# zimu = 0
# for n in content:
#     if n.isdecimal() == True:
#         num+=1
# #        print ('数字个数 ',(num))
#     elif n.isalpha() == True:
#         zimu+=1
# #        print ('字母个数',zimu)
#     else:
#         pass
# print ('数字个数 ',(num))
# print ('字母个数',zimu)

# 27、制作趣味模板程序

# name = input("请输入你的名字: ")
# place = input("请输入你经常去的地方: ")
# like = input("请输入你平时的爱好: ")
# print('猥琐的', name, ',', '最喜欢在', place, '地方', like)
#
# test = "猥琐的{0},最喜欢在{1}地方干{2}"
# name = input("请输入你的名字: ")
# place = input("请输入你经常去的地方: ")
# like = input("请输入你平时的爱好: ")
# v = test.format(name, place, like)
# print(v)

# 28、制作随机验证码，不区分大小写
#
# 流程：
#
#    - 用户执行程序
#
#    - 给用户显示需要输入验证码
#
#    - 用户输入的值
#
#           用户输入的值和显示的值相同时显示正确的信息:否则继续生成验证码等待用户输入



# def check_code():
#     import random
#     check_code = ''
#     for i in range(4):
#         current = random.randrange(0,4)
#         if current != i:
#             temp = chr(random.randint(65,90))
#         else:
#             temp = random.randint(0,9)
#         check_code += str(temp)
#     return check_code
# code = check_code()
# while True:
#     code = check_code()
#     print (code)
#     v = input('请输入验证码>>>>')
#     v1 = v.upper()
#     if v1 == code:
#         print ('验证码正确')
#         break
#     else:
#         pass

# while True:
#     name = input('请输入内容：')
#     if "苍井空" in name or "东京热" in name:
#         v = name.replace('苍井空', '*****')
#         v1 = v.replace('东京热', '*****')
#         print(v1)
#         exit()
#     else:
#         print(name)

# 例1：题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？

# sum=0
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if i!=j and j!=k and i!=k:
#                 print(i,j,k)
#                 sum+=1
# print("共",sum,"种")

#例2：题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，
# 低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提成7.5%；20万到40万之间时，
# 高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，
# 高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I
# ，求应发放奖金总数？

# i = int(input("输入你的净利润："))
# a = [0, 10, 20, 40, 60, 100]
# b = [0.1, 0.075, 0.05, 0.03, 0.15, 0.01]
# r = 0
#
# for c in range(0,6):
#     if i>a[c]:
#         r+=(i-a[c])*b[c]
#         print('区间提成:',(i-a[c])*b[c])
#         i=a[c]
# print("您的总提成为",r,"万元")

#
# # 例4:输入某月某日，判断这一天是一年的第几天？
# dic = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}#用字典的方式来对应月份和天数最合适不过了，
# # 不用考虑位置的问题。
# x = int(input('请输入月份：',))
# y = int(input('请输入日期：',))
# r=0
# if  x in range(1,13) and y in range(1,dic[x]):
#     for i in range(1, 13):
#         if i<x:
#             r+=dic[i]
#     print("这是年度第",r+y,"天")
# else:
#     print("error")

# 意输入三个整数x,y,z，请把这三个数由小到大输出。

# a=[]
# for i in range(3):
#     x=int(input("请输入数字:"))
#     a.append(x)
# a.sort()
# print(a[0],a[1],a[-1])

# 倒序排序
# r=[ ]
# for i  in range(3):
#     x=int(input('请输入整数：\n'),)
#     r.append(x)
#     r.sort(reverse=1)
# print ('\n',r[0],'\n',r[1],'\n',r[2])

# 斐波那契数列指的是从0，1开始，第三项为前两项之和。即：F0=0，F1=1，Fn=F[n-1]+F[n-2] (n>=2)

# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     elif n==0:
#         return 0
#     return fib(n - 1) + fib(n - 2)
# print (fib(10))


# def fib(n):
#     a, b = 0, 1
#     for i in range(n):
#         a, b = b, a + b
#     return a
# print(fib(10))
#
# def fib(n):
#     if n<1:
#         return None
#     if n==1:
#         return [1]
#     if n==2:
#         return [1,1]
#     else:
#         fibs=[1,1]
#         for i in range(2,n):
#             fibs.append(fibs[-1]+fibs[-2])
#     return fibs
# print(fib(0))

