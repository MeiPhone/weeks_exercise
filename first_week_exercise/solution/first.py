# -*- coding: utf-8 -*-
import operator


# 第一个问题第一问
def calculate_votes(file_name, singer):
    # 打开文件
    with open(file_name, 'r', encoding='utf-8') as votes_files:
        # 获取文件的每一行内容，并组成列表，赋予votes
        # votes的内容为['李健', '林忆莲', '彭佳慧'.....]
        votes = votes_files.readlines()
    # 一开始歌手得票为0
    count = 0
    # 循环获取votes的每一个元素
    for vote in votes:
        # 如果歌手的名字出现在列表的元素中
        if singer in vote:
            # 增加一票
            count = count + 1
    # 最终获得的票数以及得票率（题目提到一共1500票）
    return count, str(round(count/(3 * 500) * 100, 2)) + '%'


# 同时解决第一问和第二问
# 如果要计算最高得票率的歌手，可以构造字典类型如:
# {'李健': 0, '林忆莲': 0, ...}
# 每获取到一张票，是哪个歌手就加到哪个的上面
def second_calculate_votes(file_name, singer):
    # 这两句代码等同于 {'李健': 0，'迪玛希': 0，'张杰': 0，'林忆莲': 0，'狮子合唱团': 0，'林志炫': 0，'彭佳慧': 0}
    lst = ['李健', '迪玛希', '张杰', '林忆莲', '狮子合唱团', '林志炫', '彭佳慧']
    singer_dict = {x: 0 for x in lst}
    # 打开文件
    with open(file_name, 'r', encoding='utf-8') as votes_files:
        # 获取文件的每一行内容，并组成列表，赋予votes
        # votes的内容为['李健', '林忆莲', '彭佳慧'.....]
        votes = votes_files.readlines()
    # 循环获取votes的每一个元素
    for vote in votes:
        # 这里非常重要，数据处理很多时候会遇到一些特别的数据。
        # 我们获取到的每行其实是 '李健\n' 或者 '林忆莲<tab>'。
        # 虽然在文本中不容易发现，但是其实每一行结束都有换行符
        # 所以当遇到<tab>或者\n的时候，我们需要先为数据作处理
        if '<tab>' in vote:
            # '林忆莲<tab>'经过split函数被转换为['林忆莲', '<tab>']这个列表，我们获取列表的第一项
            vote = vote.split('<tab>')[0]
        elif '\n' in vote:
            # '李健\n'经过split函数被转换为['李健', '\n']这个列表，我们获取列表的第一项
            vote = vote.split('\n')[0]
        # 当这个票是对应的歌手名的时候，对应的票数加一
        singer_dict[vote] = singer_dict[vote] + 1
    # 这里获取自己喜欢的歌手的票数
    set_singer_votes = singer_dict[singer]
    # 这里计算得票率，str函数把数字转变为字符串，round函数把浮点数保留两位小数
    set_singer_percetage = str(round((set_singer_votes/1500 * 100), 2)) + '%'
    # 这句有点复杂，我们获取到每一个歌手的得票数之后，需要获取得票最多的歌手
    # 所以根据歌手的票数，也就是字典的值从小到大排序，并排获取最后的元素
    sorted_singer = sorted(singer_dict.items(), key=operator.itemgetter(1))
    return set_singer_votes, set_singer_percetage, sorted_singer[-1]

if __name__ == '__main__':
    print(calculate_votes('../votes.txt', '李健'))
    print(second_calculate_votes('../votes.txt', '李健'))
