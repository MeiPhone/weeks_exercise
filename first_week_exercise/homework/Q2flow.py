#!/usr/bin/python
# -*- coding: UTF-8 -*-
import csv
with open ('../applicants.csv',newline = '') as csvFile:
    applicants = csv.reader(csvFile,delimiter = ',',quotechar = ',')
    lst = list (applicants)
#����һ������
#    lst = [x for x in applicants]
    employeelist = lst[1:]
#    for row in applicants:
#�ö�����Ϊ�ָ�������ֵ
#        print(','.join(row))
#��ӡ��ÿ�ж���һ������
#        print(row)
flow = []
with open('../template.txt','r',encoding = 'UTF-8') as temFile:
    tem_lst = temFile.read()
    for employee in employeelist:
        tem = tem_lst
        tem = tem.replace('${name}',employee[0]).replace('${time}',employee[1]).replace('${room}',employee[2])
#�����к������һ���µĶ���
        flow.append(tem)
#�����к�������һ�����У�������������+�������У�����һ����һ��ֵ������ȡ
#        flow.extend(tem)
# 'NoneType' object has no attribute 'extend'-append�������list׷��һ��Ԫ�أ�������������ķ���ֵ��None
#        flow = flow.extend(tem)
with open ('output1.txt','w',encoding = 'gbk') as result:
    for one in flow:
#TypeError: must be str, not list
        result.write(one)
        result.write('\n\n')