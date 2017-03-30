# -*- coding: utf-8 -*-
import csv


def applicants(file_name):
    # 打开文件
    with open(file_name, newline='') as csvfile:
        # 读取csv文件
        applicants = csv.reader(csvfile, delimiter=',', quotechar='|')
        # 生成由csv文件内容组成的列表
        # [['name', 'time', 'room'], ['Alice', '09:00', 'A302'],
        # ['Bob', '09:00', 'A403'], ['Alicia', '10:00', 'A101'],
        # ['Cary', '10:30', 'A101'], ['Lucca', '10:00', 'A102'],
        # ['Maia', '10:30', 'A102']]
        lst = [x for x in applicants]
        # 获取除了第一个标题的内容
        return lst[1:]


def template(file_name, lst):
    # 这个函数把template.txt里面的内容按照不同的名称替换成相应的名字内容
    def replace_string(tem, content):
        result = tem.replace(
                    '${name}', content[0]).replace(
                    '${time}', content[1]).replace(
                    '${room}', content[2]) + '\n\n'
        return result
    # 打开文件
    with open(file_name, 'r', encoding='utf-8') as file:
        # 读取文件内容
        template = file.read()
        # 把最后面试的内容都替换到template.txt模版中
        s_list = [replace_string(template, x) for x in lst]
        return s_list


def write_txt(file_name, s_list):
    with open(file_name, 'w', encoding='utf-8') as file:
        for s in s_list:
            file.write(s)


if __name__ == '__main__':
    app = applicants('../applicants.csv')
    tem = template('../template.txt', app)
    write_txt('output.txt', tem)
