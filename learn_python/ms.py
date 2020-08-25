#1.一行代码实现1--100之和
print(sum(range(101)))

print((1+100)*100//2)       #等差数列求和公式

print(sum([i for i in range(1,101)]))    #列表推导式生成1到100


#2、如何在一个函数内部修改全局变量

a=1
def test():
    global a   #利用global 修改全局变量
    a=2
    print(a)
    return
test()

#3、列出5个python标准库
# os datetime sys re math

