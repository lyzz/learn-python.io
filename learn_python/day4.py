# with open(r"test.txt","r",encoding="UTF-8") as f:
#     data = f.read()
#     print(data)
#     ls = data.split("\n")
#     print(ls)                           #['苹果：apple', '橘子：orange', '梨子：pear', '桃子：peach', '香蕉：banana']
#     fruit = {}
# # #
#     apple = ls[0].split("：")
#     # print(apple)
#     fruit[apple[0]] = apple[1]
#     print(fruit)                    #{'苹果': 'apple'}
# #
#     orange = ls[1].split("：")
#     # print(orange)
#     fruit[orange[0]] = orange[1]
# #
#     pear = ls[2].split("：")
#     fruit[pear[0]] = pear[1]

#     peach = ls[3].split("：")
#     fruit[peach[0]] = peach[1]

#     banana = ls[4].split("：")
#     fruit[banana[0]] = banana[1]
# #
#     print(fruit)
# # #
#     key =input("输入你喜欢的水果：")
# print(fruit.get(key))