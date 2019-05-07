# _*_ coding:utf-8 _*_
import os
import sys
import xlrd

result_zhongkong = {}
result_computer = {}
data = xlrd.open_workbook("IP地址.xlsx")
table = data.sheets()[0]
nrows = table.nrows
for i in range(2,nrows):
    print(table.row_values(i)[0], table.row_values(i)[1], table.row_values(i)[2] )
    ip_computer = table.row_values(i)[1]
    backinfo_computer = os.system('ping -w 1 %s' %ip_computer)
    print(backinfo_computer)
    if backinfo_computer:
        result_computer[table.row_values(i)[0]] = ip_computer
    # for r in result_computer:
    #     print(r)
    ip_zhongong = table.row_values(i)[2]
    backinfo_zhongkong = os.system("ping -w 1 %s" %ip_zhongong)
    if backinfo_zhongkong:
        result_zhongkong[table.row_values(i)[0]] = ip_zhongong
print("--------------The computer result---------------")
for r1 in result_computer:
    print(r1)
print("--------------The zhongkong result--------------")
for r2 in result_zhongkong:
    print(r2)