import re
'''虽然在 Python 中使用正则表达式有几个步骤，但每一步都相当简单。
1．用 import re 导入正则表达式模块。
2．用 re.compile()函数创建一个 Regex 对象（记得使用原始字符串）。
3．向 Regex 对象的 search()方法传入想查找的字符串。它返回一个 Mat
'''


# def isPhoneNumber(text):
#     if len(text) != 12:
#         return False
#     for i in range(0,3):
#         if not text[i].isdecimal():
#             return False
#     if text[3] != '-':
#         return False
#     for i in range(4,7):
#         if not text[i].isdecimal():
#             return False
#     if text[7] != '-':
#         return False
#     for i in range(8,12):
#         if not text[i].isdecimal():
#             return False
#     return True

# # print(isPhoneNumber('455-555-2222'))
# message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office'
# isPhoneNumber= re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# mo = isPhoneNumber.search(message)
# print('Phone number fount:' + mo.group())
# print('打印区号' + mo.group(1))
# print(mo.groups())

# areaCode,mainNumber = mo.groups()
# print(areaCode)

# isPhoneNumber = re.compile(r'(\(\d\d\d)) (\d\d\d-\d\d\d\d)')
# mo = isPhoneNumber.search('My phone is (415) 555-4242')
# print(mo.group(1))

# message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office'
# for i in range(len(message)):
#     chunk = message[i:i+12]
#     if isPhoneNumber(chunk):
#         print('Phone number found:' + chunk)
# print('Done')


#列用括号分组
# phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
# mo = phoneNumRegex.search('My phone number is (415) 555-4242')
# print(mo.group(1))

#用|管道匹配多个分组#
# heroRegex = re.compile(r'Batman|Tina Fey')
# mo1 = heroRegex.search('Batman and Tina Fey')
# print(mo1.group())



# batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
# mo = batRegex.search('Batmobile lost a wheel')
# print(mo.group())
# print(mo.group(1))



# ?表示可选
# batRegex = re.compile(r'Bat(wo)?man')
# mo1 = batRegex.search('The Adventures of Batman')
# print(mo1.group())

# mo2 = batRegex.search('The Adventures of Batwoman')
# print(mo2.group())


#用* 匹配零次或多次

# batRegx = re.compile(r'Bat(wo)*man')
# mo1 = batRegx.search('The Adventures of Batman')
# print(mo1.group())

# mo2 = batRegx.search('The Adventures of Batwoman')
# print(mo2.group())

# mo3 = batRegx.search('The Adventures of Batwowowowoman')
# print(mo3.group())


#用+号匹配一次或多次

# batRegex = re.compile(r'Bat(wo)+man')
# mo1 = batRegex.search("The Adventures of Batwoman")
# print(mo1.group())

# mo2 = batRegex.search("The Adventures of Batwowowowoman")
# print(mo2.group())

# mo3 = batRegex.search("The Adventures of Batman")
# mo3 = None
# # print(mo3.group())
# print(mo3)


#用花括号匹配特定次数

# haRegex = re.compile(r'(Ha){3,5}')
# mo1 = haRegex.search("HaHaHa").group()
# mo2 = haRegex.search("HaHaHaHa").group()
# mo3 = haRegex.search("HaHaHaHaHa").group()
# mo4 = input('输入str:')
# if mo4 == None:
#     mo4 = group()
#     print("它是空值")

# print(mo1,mo2,mo3,mo4)
