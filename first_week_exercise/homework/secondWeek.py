from datetime import date
from datetime import timedelta

def questionOne():
    colour = input("\n假设有三种颜色的外星人，分别是红色，蓝色，绿色，请输入你遇到的颜色英文：")
    if colour == 'red':
        print ('我今天遇到红色的外星人')
    elif colour  == 'blue':
        print ('我今天遇到蓝色的外星人')
    elif colour =='grean':
        print ('我今天遇到绿色的外星人')
    else:
        print ('很抱歉，没有这种颜色的外星人')

def questionTwo(lst,root):
    name  = input("\n请输入您的帐号：")
    if name in lst:
        if name  == root:
            print('Welcome, master, What can I do for you?')
        # 不是root用户
        else:
            print("Welcome",name)
    # 不在列表里
    else:
        print('Wrong username.')

def questionThree(today):
    print ("\n您好！今天的日期是：",today,'\n')
    while True:
        num = input("请输入您想要计算的天数：")
        # print(type(num))
        # 输入的内容需要是整数
        if num.isdigit():
            # 把输入的str类型转为数值类型
            countNum = int(num)
            # print(type(countNum))
            # 输入数字的范围需要在2的10平方
            if countNum >= 0 and countNum <=1024:
                break
            # 如果超出范围
            else:
                print ("请输入大于0小于1024的整数。")
        # 如果不是整数
        else:
            print ("请输入大于0小于1024的整数！")
    # 转换需要添加的日期为日期计算可用
    date = timedelta(days = countNum)
    #计算日期
    result = today + date
    print ("结果日期：",result)

if __name__ == '__main__':
    # 问题二的账户列表
    lst = ['rose','kate','mike','winson','sue','root']
    root = 'root'
    # 获取今天的日期
    today = date.today()
    while True:
        choice = input("\n请输入想要看的题目(1~3),输入4则退出：")
        if choice == '1':
            questionOne()
        elif choice == '2':
            questionTwo(lst,root)
        elif choice == '3':
            questionThree(today)
        elif choice == '4':
            break
        else:
            print("输入有误，请重新输入。")
