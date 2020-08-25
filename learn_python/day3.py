# 列表
# 特征：[],有序，什么都可以存
# a = [1, 2, 3, 4, "1", ["123"]]
# print(a)
# print(a[0])
# print(a[-1])
# print(a[5])
# # #
name = ['John', 'Amy', 'Tony', 'Stack','John']
# print(name.count('John'))      #统计'john'出现的次数
# print(name.index('John'))     #返回'Jhon'第一次出现的下标
# name.append('Tom')    #添加'Tom'元素 ，需重新print(name)
# print(name)
# name.insert(2,"Jerry")   #指定位置，插入元素
# print(name)
# name.clear()      #清除列表，返回 []
# print(name)




name2 = ["张三", "李四", "王二麻子"]
# name.extend(name2)                      #将name2的每一个元素拆分出来添加到name里
# print(name)


# name[0] = 'Jimry'         #修改第一个元素
# print(name)
# # # #
# name.remove('Jimry')        #移除指定元素
# print(name)

# name.pop() #不指定位置则删除末尾元素,默认删除末尾元素
# # #
# # #
# print(name)
#
# name.pop(1)   #,指定位置则删除指定位置的元素
# print(name)
# #
# name.clear()
# print(name)         #清除列表结果是[]



# del name
# print(name)         #del是python的方法，不仅仅适用于列表，返回结果为报错

# 拷贝，深拷贝不会随着改变而改变，浅拷贝会随着改变而改变

# s = ['1,3,4']
# a = [1, 3, 4, 5, s]
# print('执行浅拷贝')
# b = a.copy()
# print('a =', a)
# print('b=', b)

# print("-----------------------------")
# print('当s进行变化时：')
# s.append("666")
# print('a=',a)
# print('b=',b)

# 深拷贝
# from copy import deepcopy
# #
# s1 = ['1,3,4']
# a1 = [1, 3, 4, 5, s1]
# print('执行深拷贝')
# b1 = deepcopy(a1)


# print('a1=', a1)
# print('b1=', b1)
# print("-----------------------------")
# print('当s1进行变化时：')
# s1.append("666")
# print('a1=',a1)
# print('b1=',b1)
#字符串list互相转换

# st = "apple, bannar, pear, orange, lenmon"
# sst = st.split('e')  #以，作为切割符号
# print(st)
# print(sst, type(st))

# ss = 'aab, baa'
# print(ss.split('aa'))
# print(ss,type(ss))
# c = str(sst)
# print(c[0])      #用str把list转换为字符串会有问题，取第一个字符是结果为[，不推荐使用这种方法，应该用join的方法
#

# d = ','.join(sst)
# print(d,type(d))
# print(d[0])



# 元组（tuple)
# 特点： ( )、 用,分隔，不能修改，可以添加任何类型
# t1 = ('Google', 'Runoob', 1997, 2000)
# t2 = (1, 2, 3, 4, 5 )
# t3 = "a", "b", "c", "d"   #  不需要括号也可以
# print(type(t3))
#
#
# tup1 = (1)
# print(type(tup1))    #int类型
# tup = (1,)  #元组只有一个元素是，要加上一个，
# print(type(tup))   #元组类型

#访问元组
# tup1 = ('Google', 'Runoob', 1997, 2000)
# tup2 = (1, 2, 3, 4, 5, 6, 7)

# print("tup1[0]: ", tup1[0])
# print("tup2[1:5]: ", tup2[1:5])

# 修改元组
#元组不支持修改，可以用 + 拼接

# tup1 = (12, 34.56)
# tup2 = ('abc', 'xyz')
#
# # 以下修改元组元素操作是非法的。
# # tup1[0] = 100
#
# # 创建一个新的元组
# tup3 = tup1 + tup2
# print(tup3)

# 删除元组
# 元组中的元素值是不允许删除的,用del语句来删除整个元组
# tup = ('Google', 'Runoob', 1997, 2000)
#
# print(tup)
# del tup
# print("删除后的元组 tup : ")
# print(tup)

# 元组运算符
# tup = (1, 2, 4, 6)
# print(len(tup))     #计算元素个数
#
# tup1 = (1 ,)
# print(tup + tup1)   #连接元组

# print(2 in tup)   #判断元素是否存在

# for x in(1, 2, 3):    #元组迭代
#     print(x)

# 元组索引，截取

# L = ('Google', 'Taobao', 'Runoob')
# print(L[2])
# print(L[-2])
# print(L[1:])
# print(L[::-1])


#元组内置函数

# tuple1 = ('Google', 'Runoob', 'Taobao')
# print(len(tuple1))                          #计算元组个数
#
# tuple2 = ('5', '4', '8')
# print(max(tuple2))                  #返回元组中最大值
# print(min(tuple2))                  #返回元组最小值
# #
# list1= ['Google', 'Taobao', 'Runoob', 'Baidu']
# tuple3 = tuple(list1)           #转元组
# print(tuple3)

#字典

# 特点：可变，  用{} 表示， "":""  键必须是唯一，值不必,值可以取任何数据类型，
# 但键必须是不可变的，如字符串，数字或元组

# d = {key1: value1, key2: value2}
# dict1 = {'adb':456}
# dict2 = {'abc': 123, 98.6: 37}
# #
# # 访问字典里的值,访问字典不存在的值
# dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# print ("dict['Name']: ", dict['Name'])
# print ("dict['Age']: ", dict['Age'])
# print("dict['Alice']: ", dict['Alice')   #报错

#修改字典

# dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# #
# dict['Age'] = 8  # 更新 Age
# dict['School'] = "菜鸟教程"  # 添加信息
# print(dict
#       )
# print("dict['Age']: ", dict['Age'])
# print("dict['School']: ", dict['School'])

# 删除字典元素
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
#
# del dict['Name']  # 删除键 'Name'
# print(dict)
# dict.clear()  # 清空字典
# print(dict)
# del dict  # 删除字典
#
# print("dict['Age']: ", dict['Age'])
# print("dict['School']: ", dict['School'])

# 字典特性：1.不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
# dict = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}
# print("dict['Name']: ", dict['Name'])

# 2.键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行
# dict = {['Name']: 'Runoob', 'Age': 7}
#
# print("dict['Name']: ", dict['Name'])  #报错

# 字典内置函数
# dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# print(len(dict))  #计算字典元素个数，即键的总数。
# print(str(dict))   #输出字典，以可打印的字符串表示。
# print(type(dict))   #返回输入的变量类型

#字典内置方法

# dict.clear()删除字典所有元素

# l = {'name': "TIM", "age": 12}
# print(l)
# print(l.clear())  #返回None         #
# print(l)            #返回｛｝

#dict.copy()  ython 字典 copy() 函数返回一个字典的浅复制。

# dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
#
# dict2 = dict1.copy()
# print("新复制的字典为 : ", dict2)

# 直接赋值和 copy 的区别

# dict1 = {'user': 'runoob', 'num': [1, 2, 3]}
#
# dict2 = dict1  # 浅拷贝: 引用对象
# dict3 = dict1.copy()  # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用
#
# # 修改 data 数据
# dict1['user'] = 'root'
# dict1['num'].remove(1)
#
# # 输出结果
# print(dict1)
# print(dict2)
# print(dict3)

# 字典 fromkeys() 方法
# dict.fromkeys(seq[, value])
seq = ('name', 'age', 'sex')
# # #
#
# dict = dict.fromkeys(seq)
# print("新的字典为 : %s" % str(dict))
# # #
#
# dict = dict.fromkeys(seq, 10)
# print("新的字典为 : %s" % str(dict))

# # 字典 in 操作符

# key in dict

# dict = {'Name': 'Runoob', 'Age': 7}

# 检测键 Age 是否存在
# if 'Age' in dict:
#     print("键 Age 存在")
# else:
#     print("键 Age 不存在")

# not in

# 检测键 Age 是否存在
# if 'Age' not in dict:
#     print("键 Age 不存在")
# else:
#     print("键 Age 存在")

# 字典 items() 方法以列表返回可遍历的(键, 值) 元组数组

# dict = {'Name': 'Runoob', 'Age': 7}
#
# print("Value : %s" % dict.items())

# 字典 keys() 方法
# Python3 字典 keys() 方法返回一个可迭代对象，可以使用 list() 来转换为列表

# dict = {'Name': 'Runoob', 'Age': 7}
# print(dict.keys())
# print(list(dict.keys()))  ## 转换为列表

# 字典 setdefault() 方法 和 get()方法 类似, 如果键不已经存在于字典中，将会添加键并将值设为默认值

# dict.setdefault(key, default=None)   #key -- 查找的键值。default -- 键不存在时，设置的默认键值。

# dict = {'Name': 'Runoob', 'Age': 7}
#
# print("Age 键的值为 : %s" % dict.setdefault('Age', None))
# print("Sex 键的值为 : %s" % dict.setdefault('Sex', None))
# print("新字典为：", dict)

# 字典 update() 方法update() 函数把字典参数 dict2 的 key/value(键/值) 对更新到字典 dict 里

# dict.update(dict2)

# dict = {'1':2, '2':4}
# dict1 = {'3':None}
# dict.update(dict1)
# print(dict)

# values() 方法
# dict.values()
#values() 方法返回一个迭代器，可以使用 list() 来转换为列表，列表为字典中的所有值

# dict = {'Sex': 'female', 'Age': 7, 'Name': 'Zara'}
# print(dict.values())
#
# print ("字典所有值为 : ",  list(dict.values()))

#字典 pop() 方法

#字典 pop() 方法删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值

# pop(key[,default])

# dict = {'Name': 'Tim', 'Age': 12, 'Class': 'num_05', 'Gender': 'Male', 'Hobby': 'Basketball'}
# print(dict.pop('Name'))
#
# print(dict)
# 字典 popitem() 方法
#Python 字典 popitem() 方法随机返回并删除字典中的最后一对键和值。
# 如果字典已经为空，却调用了此方法，就报出KeyError异常
# popitem()
# print(dict.popitem())
# print(dict)

# 集合
# 集合（set）是一个无序的不重复元素序列。可以使用大括号 { } 或者 set() 函数创建集合，
# 注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
# # parame = {value01,value02,...}
# 或者
# set(value)

# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(basket)                 #自动去重 ，排列是无序的
#
# print('apple' in basket)    #判断元素是否在集合里


#两个集合间的运算

# a = set('abracadabra')
# b = set('alacazam')
# print(a)    #{'a', 'r', 'b', 'c', 'd'}
# print(b)    #{'a', 'z', 'c', 'l', 'm'}
# print(a - b)  ## 集合a中包含而集合b中不包含的元素
# print(a | b)   # 集合a或b中包含的所有元素
# print(a & b)   # 集合a和b中都包含了的元素
# print(a ^ b )   # 不同时包含于a和b的元素

#类似列表推导式，同样集合支持集合推导式
# print({x for x in 'abracadabra' if x not in 'abc'})

#添加元素
# s.add()

# s = set(('a', 'b', 'c'))
# s.add('d')
# print(s)
# s.update()
# s.update('e', 'f', 'g')
# print(s)

#移除元素,不存在的元素会报错s.remove(x)
# s.remove('e')
# print(s)
#
# s.discard('g')
# print(s)
# #
# s.discard('h')    #移除不存在的元素不会报错
# print(s)

#s.pop()  多次执行测试结果都不一样。set 集合的 pop 方法会对集合进行无序的排列，
# 然后将这个无序排列集合的左面第一个元素进行删除
# s.pop()
# print(s)

# 计算集合元素个数
# print(len(s))  #计算s元素个数

# 清空集合
# s.clear()
# print(s)


#拷贝Set copy()
# x = s.copy()    #x的值不会随着s的改变给改变
# s.add('u')
# print(x)            #{'c', 'a', 'b', 'd'}
# print(s)            #{'c', 'a', 'u', 'd', 'b'}
#
# # Set difference()  返回集合的差集
# z = s.difference(x)     #返回一个集合，元素在集合s里，但不在集合x里
# print(z)

#Set difference_update()
#difference_update() 方法用于移除两个集合中都存在的元素。
# difference_update() 方法与 difference() 方法的区别在于 difference() 方法返回一个移除相同元素的新集合
# ，而 difference_update() 方法是直接在原来的集合中移除元素，没有返回值。
# t = s.difference_update(x)
# print(t)   #返回None
# print(x)

#Set intersection() 返回两个或更多集合中都包含的元素，即交集
# x = {"apple", "banana", "cherry"}
# y = {"google", "runoob", "apple"}
#
# z = x.intersection(y)   #返回x,y里都包含的元素
#
# print(z)

#Set intersection_update()
#intersection_update() 方法用于获取两个或更多集合中都重叠的元素，即计算交集。
# intersection_update() 方法不同于 intersection() 方法，因为 intersection() 方法是返回一个新的集合，
# 而 intersection_update() 方法是在原始的集合上移除不重叠的元素。
# x = {"apple", "banana", "cherry"}
# y = {"google", "runoob", "apple"}
#
# z = x.intersection_update(y)
# print(z)   #无返回值，返回None
# print(x)

# Set isdisjoint()判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False

# x = {"apple", "banana", "cherry"}
# y = {"google", "runoob", "facebook"}
#
# z = x.isdisjoint(y)   #判断集合 y 中是否有包含 集合 x 的元素
#
# print(z)

#Set issubset() 判断集合的所有元素是否都包含在指定集合中，如果是则返回 True，否则返回 False

# x = {"a", "b", "c"}
# y = {"f", "e", "d", "c", "b", "a"}
#
# z = x.issubset(y)  #断集合 x 的所有元素是否都包含在集合 y 中
#
# print(z)

#Set issuperset() 判断指定集合的所有元素是否都包含在原始的集合中，如果是则返回 True，否则返回 False

# x = {"f", "e", "d", "c", "b", "a"}
# y = {"a", "b", "c"}
#
# z = x.issuperset(y)   #判断集合 y 的所有元素是否都包含在集合 x 中
#
# print(z)

#Set symmetric_difference()返回两个集合中不重复的元素集合，即会移除两个集合中都存在的元素

# x = {"apple", "banana", "cherry"}
# y = {"google", "runoob", "apple"}
#
# z = x.symmetric_difference(y)
#
# print(z)

#Set symmetric_difference_update() 移除当前集合中在另外一个指定集合相同的元素
# ，并将另外一个指定集合中不同的元素插入到当前集合中

# x = {"apple", "banana", "cherry"}
# y = {"google", "runoob", "apple"}
#
# x.symmetric_difference_update(y)  #在原始集合 x 中移除与 y 集合中的重复元素，并将不重复的
# # 元素插入到集合 x 中
#
# print(x)

#Set union() 返回两个集合的并集，即包含了所有集合的元素，重复的元素只会出现一次
#
# x = {"a", "b", "c"}
# y = {"f", "d", "a"}
# z = {"c", "d", "e"}
#
# result = x.union(y, z)
#
# print(result)



#文件路径的合法性

# "F:\learn_python\day1.py"
# "F:\\learn_python\\day1.py"         #第一种方法路径前再加一个\
# "F:/earn_python/day1.py"            #第二种方法将\变成/
# r"F:\learn_python\day1.py"          #第三种方法路径前加r

#文件的读

# file = open(r"day1.py", "r", encoding="utf-8")      #如果再同一个目录下用r"day1.py"也可以
# print(file.read())
# file.close()

# file = open(r"day01.txt", "r", encoding="utf-8")
# print(file.read())
# file.close()
#文件的写

# file = open(r"F:\learn_python\day1.txt", "w",encoding="utf-8")          #读写不能同时操作
#
# file.write("hellow,world")
#
# file.close()
# file = open(r"day01.txt", 'w', encoding="utf-8")
# file.write("Life is difficult, but i use python!")
# file.close()


#以二进制方式读文件
#
# file = open(r"day1.py", "rb")
# print(file.read(),type(file.read()))
# file.close()

# python3读取文件方法

# with open(r"day1.txt", "r") as file1:
    # a = file1.read()
    # a1 = file1.readline()           #读取多行
    # print('a=',a)
    # print('a1=',a1)
#
# with open("text.txt", "a", encoding="UTF-8") as f1:               #a表示追加，执行一次就追加一次
#     f1.write("你好，我是哈哈哈\n")


# 作业


# with open(r"fruit.txt", "w", encoding="UTF-8") as fruit:
#     fruit.write("苹果，橙子，\n香蕉，\n梨子")

# with open(r"fruit.txt", "r", encoding="UTF-8") as fruit:
#     data = fruit.readlines()
#     print(data)                         #['苹果，橙子，\n', '香蕉，\n', '梨子']
# #
#
    # data[1] = data[1].replace("，\n","")     #['苹果，橙子，\n', '香蕉', '梨子']
    # print(data)                             #['苹果，橙子，\n', '香蕉', '梨子']
    # a = data[0].split('，')             #['苹果，橙子，\n']
    # print(a)
    # c = a[:-1]              #['苹果', '橙子']
    # print(c)
    # c.extend(data[1:])
    # print(c)

# with open(r"fruit.txt", "r", encoding="UTF-8") as fruit:
#     data = fruit.read()
#     print(data)
#     a = data.replace('\n', "").split("，")
#     print(a)

# 排序
# num = [2, 3, 6, 4, 1, 7, 8, 5]
# num.sort()            #从小到大排序
# print(num)
# num.reverse()           #倒序排序
# print(num)

# num1 = ['0', '322', '56', 'a00', '34', '7', '1322']
# num1.sort()   #['0', '1322', '322', '34', '56', '7', 'a00']字符串比大小，从第一位开始比，有字母的字符串默认最大
# # num1.reverse()
# print(num1)

