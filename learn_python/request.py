import requests
# #
# url = "http://www.polayoutu.com/collections"
# response = requests.get(url)
# print(response)
# print(response.status_code)  #网页的状态码
# if response.status_code == 200:
#     print(response.text)


# ur2 = "https://www.polayoutu.com/palette/get_img_by_user_id/10100?{}"        #接口地址
# #
# response = requests.get(ur2)
# print(response)
# print(response.status_code)  #网页的状态一般是200
# if response.status_code == 200:
#     print(type(response.json()))     #得到一个字典类型的数据
#     res = response.json()
#     print(res)
    # print(res.get('message'))    #字典取值
    # print(res['message'])
    # print(res.get("data")[0].get('id'))             取data里的id值
    # a = res.get("data")
    # print(a)
    # print(a[0].get("id"))
    # for i in res['data']:
    #     print(i['full_res'])              #取所有的.jpg的图片

    # for i in range(len(res['data'])):
    #     data = requests.get(res['data'][i]["full_res"])
    #     with open("{}.jpg".format(i),'ab') as f:
    #         f.write(data.content)

    # 找出北京的.jpg
# ur1 = "https://www.polayoutu.com/collections/get_entries_by_tags/%E5%8C%97%E4%BA%AC?{}"
# response = requests.get(ur1)
# print(response.status_code)
#
# if response.status_code == 200:
#     res = response.json()
#     print(res.get('data')[0])
#     for i in res['data']:
#         print(i['full_res'])
#
#     for i in range(len(res['data'])):
#         data = requests.get(res['data'][i]["full_res"])
#         with open("{}.jpg".format(i),'ab') as f:                    #图片是byte格式的，要加ab
#             f.write(data.content)
#
#
# def visit_interface(url, params, method="get"):
#     if method == "get":
#         response = requests.get(url, params)
#         return response.json()
#     if method == "post":
#         response = requests.post(url, params)
#         return response.json()



import requests
ur1 = "https://www.polayoutu.com/palette/get_img_by_user_id/8293?{}"

response = requests.get(ur1)

if response.status_code == 200:
	res = response.json()
	print(res)
