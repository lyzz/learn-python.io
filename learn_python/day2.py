# 行与缩进

# #不顶行写会报错，需要顶格写
    # print('ll')   #   IndentationError: unexpected indent

# # 遇:下一行必缩进一个tab
# if True:
#     print('正确的书写')
# else:
#     print('true')
#     print("111")      #缩进不一致也会报错

# # 多行语句

# #语句过长用\
# item_one = 'one'
# item_two = 'two'
# item_three = 'three'

# total = item_one + \
#         item_two + \
#             item_three
        
# print(total)

# total1 = item_one + \
#     total

# print(total)

# #在[],{}或（）中多行语句，无需使用\,直接用enter键
# total1 = ['item_one', 'item_two', 'item_three',
#             'item_four', 'item_five']
# print(total1)


#报错

# print(111 1)

# File "cnJc01.py", line 59     #错误信息在第39行
#     print(111 1)                #错误的具体地方
#               ^
# SyntaxError: invalid syntax     #SyntaxError 错误类型
                                    #invalid syntax 错误的具体解释




# import keyword
# # # 导入一个模块
# i = keyword.kwlist
# print(i)        #打印python3的关键字
# '''['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue',
#  'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in',
#  'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# '''
# s = 0
# for n in i:
#     print('{}'.format(n))
#     s += 1
#     print(s)

# str = "人生苦短，我用python!"      #字符串用 "" 号表示
#
# print(str[0])                     #取第一个值
# # # #
# print(str[-1])                    #取最后一个值
# # #
# print(str[0:3])                   #取前三个值
# # # #
# print(str[::2])                   #2表示步长，字符串没两个取一个值
# # # #
# print(str[::])                    #取整个字符串
# # # #
# print(str[-5:-1])                   #取thon  ,-1取不到
# # #
# # #
# print(str[:11])                     #取前11个值
# # # #
# # print(str[2:])                      #从第三个开始取一直到底
# print(str[::-1])     #字符串倒序
# str1 = "My name is HanMeiMei!"
# # # # #
# print(str1.capitalize())        #首字母大写，其他小写
# print(str1.count("i"))          #统计字符出现的次数
# print(str1.find("n"))           #查找字符第一次出现的下标
# print(str1.find("you"))         #不存在的字符返回-1
# print(str1.index("i"))          #查找字符第一次出现的下标
# # # print(str1.index("you"))      #不存在的字符会报错
# print(str1.isalnum())           #检测字符串是否由字母和数字组成
# print(str1.isalpha())           #检测字符串是否只由字母组成
# print(str1.isdigit())           #检测字符串是否只由数字组成
# print(str1.lower())             #字符串变为小写
# print(str1.islower())           #判读字符串是否都是小写
# print(str1.upper())             #字符串变为大写
# print(str1.isupper())           #判读字符串是否都是大写
# print(str1.endswith("!"))       #判读是否以指定字符结尾
# print(str1.endswith("a"))
# print(str1.replace("My","You"))      #替换字符

# 字符串运算符
# "+"表拼接
# a = "哈哈3aa"
# b = '嘻嘻4bb'
# print(a + b)
# print('{}'.format(a) + '{}'.format(b))


# "*"表重复字符串
# c = "python"
# print(c * 3)

# "in" 成员运算符，字符在字符串里返回true，否则为false
# str4 = "sdjflkj"
# print("s" in str4)

# "not in" 成员运算符，字符不在字符串里返回true，否则为false

# str5 = "1213213123"
# print('3' not in str5)

# "r" "R" 表原始字符串

# print("h\ntt")
# print(r"h\ntt")
# print(R"h\ntt")

# "%"格式化字符串
# %c	格式化字符及其ASCII码
# %s	 格式化字符串
# %d	 格式化整数
# %u	 格式化无符号整型
# %o	 格式化无符号八进制数
# %x	 格式化无符号十六进制数
# %X	 格式化无符号十六进制数（大写）
# %f	 格式化浮点数字，可指定小数点后的精度
# %e	 用科学计数法格式化浮点数
# %E	 作用同%e，用科学计数法格式化浮点数
# %g	 %f和%e的简写
# %G	 %f 和 %E 的简写
# %p	 用十六进制数格式化变量的地址

# str6 = "My name %s, I'm %d years old!" %('hanmeimei',12)
# print(str6)
# #
# str7 = "My name is {}, I'm {} years old!".format('HanMeiMei',12)
# print(str7)
