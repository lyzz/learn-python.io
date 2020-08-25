import csv

with open("软件测试工程师.cvs","r") as file:
    reader = csv.reader(file)
    data = [i for i in reader]
    print(data)
    