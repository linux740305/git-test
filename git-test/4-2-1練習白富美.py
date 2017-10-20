#-*- coding:utf-8 -*-

EnglishApple = input("請輸入蘋果的英文:")
EnglishOne = int(input("請輸入one的數字是:"))
EnglishTwo = int(input("請輸入two的數字是:"))
EnglishThere = input("請輸入英文數字3的正確答案:")
if (EnglishApple=="apple") and (EnglishOne==1) and (EnglishTwo==2) and (EnglishThere=="there"):
	print("正確答案")
elif EnglishApple=="?":
	print("apple")
else:
	print("答案錯誤")

#if EnglistApple=="apple" or EnglistOne==1 or EnglistTwo==2:
#	print("or效果")
#else:
#	print("or錯誤消果")
'''color = input("你白嗎?:")
money = int(input("請輸入你的財產:"))
beautiful = input("你漂亮嗎?:")

if color=="白" or money>=1000000 and beautiful =="漂亮":
	print("你是白富美")
else:
	print("你不是白富美")
'''


