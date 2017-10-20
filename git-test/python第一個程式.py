#-*- coding:utf-8 -*-
#1. -*- coding:utf-8 -*- 讓python明白使用此編碼 python建議寫法
#2. coding=utf-8 讓python 明白使用此編碼
#3. #號後代表註釋

#3. 定義變量
iphone8 = 30000
iphone7 = 25000
money = iphone8 + iphone7
name = "顥仁"

#4. print表示文字輸出
print("money%d"%money)
print("hello world!")#表示文字輸出

#5. ''' '''表示註釋整段文字
#6. """ """表示註釋整段文字

#7. input表示文字輸入
姓名 = input ("請輸入名字")
print("姓名:%s"%姓名)
print("名字:%s"%name)

#8. if用來完成判斷
#9. fi條件:條件成立的時候,做的事情

age = input("請輸入年齡:")#input獲取的所有數據,都當做字符串類型

age_num = int(age)#去除雙引號的值20 

#10. 條件如果年齡大於:18
if age_num>18:
	print("已成年,可以去網吧....")
else:
	print("未成年,回家寫作業")
