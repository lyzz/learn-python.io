# def add(a,b):
#     return a+b
# print(add(1,1))

# 求1+2+3+....
# def f(n):
#     if n == 1:
#         return 1
#     return f(n-1)+n
#
# print(f(100))
'''
f(1) = 1
f(2) = f(1) +2
f(3) = f(2) + 3
f(4) = f(3) + 4

'''

"""
s(1) = 1
s(3) = s(1)+3
s(5) = s(1)+3+5
s(7) = s(1)+3+5+7
s(9) = s(1)+3+5+7+9
"""
#求1+3+5...99

# def s(i):
#     if i == 1:
#         return 1
#     return s(i-2)+i
# print(s(9))

# '闭包函数'
def shopping():
    print("登录成功")
    def order(id):
        print("下订单",id)
    return order
# shop = shopping()
# shop("11111")
# shop

'匿名函数'
# def add(x,y):
#     return x+y
# # print(add(1,2))
#
# a = lambda x,y:x+y
# print(a(1,2))


# def add2(x,y,z):
#     return x+2*y+3*z
#
# a = lambda x,y,z:x+2*y+3*z
# print(a(1,1,1))