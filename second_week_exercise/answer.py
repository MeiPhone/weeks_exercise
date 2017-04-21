from datetime import timedelta
from datetime import date as d


def first_question():
    # 获取用户输入的字符串
    colour = input(
        "\n假设有三种颜色的外星人" +
        "分别是红色，蓝色，绿色，请输入你遇到的颜色英文：")
    # 如果用户输入为红色
    if colour == '红色':
        print('我今天遇到红色的外星人')
    elif colour == '蓝色':
        print('我今天遇到蓝色的外星人')
    elif colour == '绿色':
        print('我今天遇到绿色的外星人')
    else:
        print('抱歉，没有这种颜色的外星人')


def second_question():
    # 初始用户名列表
    lst = ['apple', 'google', 'root', 'amazon', 'github']
    while True:
        # 获取用户输入字符串
        name = input("\n请输入您的帐号：")
        # 如果字符串在用户名列表中
        if name in lst:
            # 如果字符串为root
            if name == 'root':
                print('Welcome, master, What can I do for you?')
            else:
                print("Welcome ", name)
        else:
            print('Wrong username.')


def third_question():
    # 获取今天的日期
    today = d.today()
    print("\n您好！今天的日期是：", today)
    while True:
        num = input("您想要知道多少天后的日期（1-1024天内）：")
        # 如果输入的字符串是整数
        if num.isdigit():
            count = int(num)
            # 如果输入的字符串是整数并且在1到1024的范围中
            if count > 0 and count <= 1024:
                # 计算结果日期
                date = timedelta(days=count)
                result = today + date
                print("%s天后的日期是：" % count, result)
                continue
        print("请输入大于0小于1024的整数。")
