import xlwt


def set_style(name, height, bold=False):
    style = xlwt.XFStyle()  # 初始化样式
    font = xlwt.Font()  # 为样式创建字体
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height

    style.font = font
    return style


def write_excel(path):
    # 创建工作簿
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建sheet
    data_sheet = workbook.add_sheet('demo')

    lines = ["name", "age", "class_id"]
    john = ["john", 12, "class1"]
    tom = ["tom", 22, 'class2']
    alice = ['alice', 17, 'class2']
    jim = ['jim', 19, 'class4']

    # 生成第一行和第二行
    for i in range(len(lines)):
        data_sheet.write(0, i, lines[i],
                         set_style('Times New Roman', 220, True))

        data_sheet.write(1, i, john[i],
                         set_style('Times New Roman', 220, True))

        data_sheet.write(2, i, tom[i],
                         set_style('Times New Roman', 220, True))

        data_sheet.write(3, i, alice[i],
                         set_style('Times New Roman', 220, True))

        data_sheet.write(4, i, jim[i],
                         set_style('Times New Roman', 220, True))

        workbook.save(path)


if __name__ == '__main__':
    path = 'F:\learn_python\demo.xls'
    write_excel(path)
    print(u'创建demo.xls文件成功')

# import xlrd
#
# # 设置路径
# path = 'excelwrite.xls'
# # 打开execl
# workbook = xlrd.open_workbook(path)
#
# # 输出Excel文件中所有sheet的名字
# print(workbook.sheet_names())
