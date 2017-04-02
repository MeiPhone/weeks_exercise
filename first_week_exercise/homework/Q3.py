import os
import csv
import operator
def renameFiles(filePath):
    #获取路径下所有文件序列
    pathDir =  os.listdir(filePath)
    for fileName in pathDir:
        # 判断是否文件只会根据绝对路径，不然会返回false，所以需要拼接路径才能判断
        fullName = os.path.join(filePath,fileName)
        if os.path.isfile(fullName):
            originName = os.path.join(fileName)
            name = os.path.splitext(originName)[0]
            #os的方法都要用绝对路径，新文件名的绝对路径
        newName = os.path.join(filePath,name + '.csv')
        #重命名
        os.rename(fullName,newName)

def compileFiles(filePath,compilecsv,header):
    #文件数据数据插入到表里
    def insertFiles(compilecsv,departmentList,header):
        with open(compilecsv,'a') as csvfile:
            fieldnames = header
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            # 表头
            # writer.writeheader()
            for detail in departmentList['achievement']:
                month = detail[0]
                achievement = detail[1]
                writer.writerow ({'department':departmentList['department'],'month':month,'achievement':achievement})

    departmentList = {}
    pathDir = os.listdir(filePath)
    # 遍历每一个文件
    for fileName in pathDir:
        # 文件名就是部门名称
        departmentList['department'] = os.path.splitext(fileName)[0]
        #打开该部门的文件，读取文件内容。
        fullName = os.path.join(filePath,fileName)
        with open (fullName,'r',newline = '') as csvFile:
            lst = csv.reader(csvFile,delimiter = ',',quotechar = ',')
            # achieve = [x for x in lst]
            achieve = list(lst)
            departmentList['achievement'] = achieve
        #把这个文件的数据插入到汇总表
        insertFiles(compilecsv,departmentList,header)

#创建一个新文件，并写好表头
def newcsv(compilecsv,header):
    with open (compilecsv,'w') as csvfile:
        fieldnames = header
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(fieldnames)

def calculate(compilecsv):
    lst_depart = []
    lst_month =[]
    detailDict = {}
    month_achieve = {}
    # 获取文件总部门列表、月份列表
    with open (compilecsv,'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            lst_depart.append(row['department'])
            lst_month.append(row['month'])
        #把部门的名字去重，set()
        lst_depart = list(set(lst_depart))
        lst_month = list(set(lst_month))
        #把列表变成字典，方便计算记录
        achieveDict = {x:0 for x in lst_depart}
        monthDict = {x:0 for x in lst_month}
    # 读取文件、计算部门总业绩、月份总业绩
    with open (compilecsv,'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # 把每个部门的每月业绩字典映射到部门字典-需要再学习不知道有重复的时候会怎么样
            detailDict.setdefault(row['department'],{})[row['month']]=row['achievement']
            # 计算每个部门的总业绩
            achieveDict[row['department']] +=int(row['achievement'])
            monthDict[row['month']] += int(row['achievement'])
    # 获取业绩最好的部门--参考老师的,sorted函数还需要继续学习
    sorted_achieve = sorted(achieveDict.items(), key=operator.itemgetter(1))
    # print('业绩最好的部门是：%s，业绩总额：%s'，%(sorted_achieve[-1][0],sorted_achieve[-1][1]))
    best_depart = sorted_achieve[-1][0]
    print('业绩最好的部门是：',best_depart,'业绩总额：',sorted_achieve[-1][1])
    # 获取业绩最好部门的业绩
    achieve_Bdepart = detailDict[best_depart]
    # 获取业绩最好部门的最好月份
    sorted_best_depart = sorted(achieve_Bdepart.items(), key=operator.itemgetter(1))
    print('部门',best_depart,'最好的业绩月份是',sorted_best_depart[-1][0])
    # 获取全公司业绩最好的月份
    sorted_best_month = sorted(monthDict.items(), key=operator.itemgetter(1))
    print('公司最好的业绩月份是',sorted_best_month[-1][0],'业绩：',sorted_best_month[-1][1])


if __name__ == '__main__':
    filePath = '../performance'
    compilecsv = 'total.csv'
    header = ['department','month','achievement']
    renameFiles(filePath)
    newcsv(compilecsv,header)
    compileFiles(filePath,compilecsv,header)
    calculate(compilecsv)
