#!/usr/bin/python
# -*- coding: UTF-8 -*-
import csv
with open ('../applicants.csv',newline = '') as csvFile:
    applicants = csv.reader(csvFile,delimiter = ',',quotechar = ',')
    lst = list (applicants)
#另外一个方法
#    lst = [x for x in applicants]
    employeelist = lst[1:]
#    for row in applicants:
#用逗号作为分隔符各个值
#        print(','.join(row))
#打印的每行都是一个序列
#        print(row)
flow = []
with open('../template.txt','r',encoding = 'UTF-8') as temFile:
    tem_lst = temFile.read()
    for employee in employeelist:
        tem = tem_lst
        tem = tem.replace('${name}',employee[0]).replace('${time}',employee[1]).replace('${room}',employee[2])
#在序列后面添加一个新的对象
        flow.append(tem)
#在序列后面增加一个序列：导致文字序列+文字序列，就是一个字一个值，不可取
#        flow.extend(tem)
# 'NoneType' object has no attribute 'extend'-append方法会给list追加一个元素，但是这个函数的返回值是None
#        flow = flow.extend(tem)
with open ('output1.txt','w',encoding = 'gbk') as result:
    for one in flow:
#TypeError: must be str, not list
        result.write(one)
        result.write('\n\n')