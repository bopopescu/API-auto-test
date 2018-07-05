import xlrd
import os

filename = "/Users/chongwang/Documents/Jing/9-a-m/testimport.xlsx"
filePath = os.path.join(os.getcwd(), filename)

print filePath

xl = xlrd.open_workbook(filePath)

sheet1 = xl.sheet_by_name("user")

print 'sheet_names:', sheet1.name
print 'sheet_numbers:', sheet1.nrows