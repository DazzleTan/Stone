from stone import stone
from scissors import scissors
from palm import palm
import random

def judgment(a):
    if a == "石头":
        stone()
    elif a == "剪刀":
        scissors()
    else:
        palm()

number = 0
while True:
    if number > 0:
        c = input("要继续游戏吗？请输入n退出，输入其它继续游戏：")
        if c == "n":
            break
        else:
            number = 0
    else:
        while number == 0:
            a = input("请出拳（石头，剪刀，布）：")
            if a== "石头" or a== "剪刀" or a== "布":
                number += 1
            else:
                print("输入有误，请重新输入")
        print("--------战斗过程--------")
        b = random.randint(1,3)
        if b == 1:
            print("电脑出了：石头")
            stone()
            print("你出了：")
            judgment(a)
        elif b == 2:
            print("电脑出了：剪刀")
            scissors()
            print("你出了：")
            judgment(a)
        else:
            print("电脑出了：布")
            palm()
            print("你出了：")
            judgment(a)
        print("--------结果--------")
        if a == "石头":
            if b == 1:
                print("平局")
            elif b == 2:
                print("你赢了")
            else:
                print("电脑赢了")
        elif a == "剪刀":
            if b == 1:
                print("电脑赢了")
            elif b == 2:
                print("平局")
            else:
                print("你赢了")
        else:
            if b == 1:
                print("你赢了")
            elif b == 2:
                print("电脑赢了")
            else:
                print("平局")
        number += 1