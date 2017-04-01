with open ('../votes.txt','r') as f:
    votes = f.readlines()
#print(votes)
singer1 = '李健'
total = len(votes)
print('总票数：%s 票'% total)
count = {singer1:0,'迪玛希':0,'张杰':0,'林忆莲':0,'狮子合唱团':0,'林志炫':0,'彭佳慧':0}
for vo in votes:
    if singer1 in vo:
        count[singer1] +=1
    elif '迪玛希' in vo:
        count['迪玛希'] +=1
    elif '张杰' in vo:
        count['张杰'] +=1
    elif '林忆莲' in vo:
        count['林忆莲'] +=1
    elif '狮子合唱团' in vo:
        count['狮子合唱团'] +=1
    elif '林志炫' in vo:
        count['林志炫'] +=1
    elif '彭佳慧' in vo:
        count['彭佳慧'] +=1
print(singer1 + '：%s 票' % count[singer1])
print('迪玛希：%s 票' % count['迪玛希'])
print('张杰：%s 票' % count['张杰'])
print('林忆莲：%s 票' % count['林忆莲'])
print('狮子合唱团：%s 票' % count['狮子合唱团'])
print('林志炫：%s 票' % count['林志炫'])
print('彭佳慧：%s 票' % count['彭佳慧'])
#以为用序列保存取最大，然而回不去找不到是谁。。。
#result = [count['李健'],count['迪玛希'],count['张杰'],count['林忆莲'],count['狮子合唱团'],count['林志炫'],count['彭佳慧']]
#print (result)
#maxr =  max(result)
#print ('得票最多的是：%d' % maxr)
result = 0
for singer in count:
    if count[singer] > result:
        champian = singer
        result = count [singer]
print('我喜欢的狮子合唱团得票 %d，得票率 %.2f%%'%(count['狮子合唱团'],(count['狮子合唱团']/total)*100))
print('冠军是：%s,%d 票' %(champian,result))

# 问题：
# 1、字典有没有最大值方法？
# 2、整篇下来好像好多个名字，用变量好像好一点，以后加上输入好像更好-如李健
# 3、print(singer1 + '：%s 票' % count[singer1])，这一句里面的前面 + 组合起来跟用%s有什么优略势？
