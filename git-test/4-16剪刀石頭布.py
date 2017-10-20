#-*-coding:utf-8 -*-
#導入import random 工具
import random

#用input定義player輸入文字為(請輸入剪刀石頭布)
player = int(input("請輸入 0剪刀 1石頭 2布:"))

#import random工具 讓computer = 隨機生成0-2數字
computer = random.randint(0,2)

#
if (player==0 and computer==2) or (player==1 and computer==0) or (player==2 and computer==1):
	print("你贏了")

#
elif player==computer:
	print("平手")

#
else:
	print("你輸了")
