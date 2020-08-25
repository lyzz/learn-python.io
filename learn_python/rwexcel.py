
import xlwt

workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('test')
# worksheet.write(0, 0, 'john')
# worksheet.write(0, 1, 'dolphin')
# worksheet.write(0, 2, 'tony')
# workbook.save('excelwrite.xls')
lines = ["name", "age", "class_id"]
names = ["john", "any", "alice", "tom"]
ages = ["12", "23", "16", "32"]
class_ids = ["1", "2", "3", "4"]

for line in range(len(lines)):
    worksheet.write(0, 0, line)


# workbook.save('excelwrite.xls')
#     for name in range(len(names)):
#         worksheet.write(1, name, names[name])
# workbook.save('excelwrite.xls')

# for line in range(len(lines)):
#     worksheet.write(0, line, lines[line])
# workbook.save('excelwrite.xls')
#
# for line in range(len(lines)):
#     worksheet.write(0, line, lines[line])
# workbook.save('excelwrite.xls')
# import xlrd
# book = xlrd.open_workbook('excelwrite.xls')
# sheet1 = book.sheets()[]
# nrows = sheet1.nrows
# print('表格总行数',nrows)