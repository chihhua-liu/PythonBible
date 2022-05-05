# # 1.	Function
# # Test1 -------------------------------------------------
# def SayHello():
#     print("Welcome!")
# SayHello()  # Ans:Welcome!!
# # Test2 -------------------------------------------------
# def GetArea(width,height):
#  area=width*height
#  return area
# w = float(input('Please input width:'))
# h = float(input('Please input height:'))
# a = GetArea(w,h)
# print('Area =',a)
# # Test 2-1 ---------------------------------------------
# def Circle(radius):
#     area =radius*radius*3.14
#     length = 2*radius*3.14
#     return area,length
# area, length = Circle(5)
# print("radius={} ,area ={},length ={:5.2f}".format(5,area,length))
# # --Test3 ------------------------------------------------
# def ctof(c):  #攝氏轉華氏
#    f = c * 1.8 + 32
#    return f
# inputc = float(input("請輸入攝氏溫度："))
# print("華氏溫度為：%5.1f 度" % ctof(inputc))
# # Test4 global parameter-------------------------------------------
# def scope():
#    global var1
#    var1 = 1
#    var2 = 2
#    print(var1, var2)
# var1 = 10
# var2 = 20
# scope()
# print(var1,var2)
# # 2,字串函式
# print("center() 字串擴充n字元且置中=" ,'book'.center(10))
# print("ljust(n) 字串擴充n字元且靠左=" ,'book'.ljust(10))
# print("rjust(n) 字串擴充n字元且靠右=" ,'book'.rjust(10))
# ###--------------------------------------------------------------
# print('k 在字串的第幾個位置:','book'.find('k')) # 3(從零開始算
# print('是否都是小寫','abc'.islower()) #True
# print('是否都是大寫','ABc'.isupper()) #False
###--------------------------------------------------------------
# list1=['1','2','3','4']
# list2='+'.join(list1)
# print('串列元素以+連接',list2)   #1+2+3+4
# print(type(list2))
###--------------------------------------------------------------
# print('轉換成小寫','Yes'.lower())
# print('轉換成大寫','Yes'.upper())
# ###--------------------------------------------------------------
# print('移除左邊的空白鍵','  book   '.lstrip())
# print('移除右邊的空白鍵','  book   '.rstrip())
# print('移除左右邊的空白鍵','  book   '.strip())
# ###-split 常用-------------------------------------------------------------
# print('取代字元','  book   '.replace('o','a'))    # book change baak
# print('取代字元','  book   '.replace('o','a',1))  # book change baak
# print('分隔字元分割為串列','ab#cd'.split('#')) # ['ab', 'cd']
# str1 ='This is a book'
# print('分隔字元分割為串列',str1.split(' '))
# ###--------------------------------------------------------------
# print('是否以某字母結尾','abc'.endswith('c')) #True
# print('是否以某字母開頭','abc'.startswith('a')) #True
# # ---- startswith()檢查網址格式 ---------------------------------------------
# web = input("請輸入網址：")  # web is str
# if web.startswith("http:\\") or web.startswith("https:\\"):
#    print("輸入的網址格式正確！")
# else:
#    print("輸入的網址格式錯誤！")
# # ----------------------------------------------------------------------------------------------
# listname = ["林大明", "陳阿中", "張小英"]
# listchinese = [100, 74, 82]
# listmath = [87, 88, 65]
# listenglish = [79, 100, 8]
# print("姓名     座號  國文  數學  英文")
# for i in range(0,3):    # str(i+1).rjust(3)
#   print(listname[i].ljust(5), str(i+1).rjust(3), str(listchinese[i]).rjust(5), str(listmath[i]).rjust(5), str(listenglish[i]).rjust(5))
#   # print(listname[i].ljust(5), str(listchinese[i]).rjust(5), str(listmath[i]).rjust(5), str(listenglish[i]).rjust(5))
# # -------------------------------------------------------------------------------------------------
# date1 = "2017-8-23"
# date1 = "西元 " + date1
# date1 = date1.replace("-", " 年 ", 1)
# date1 = date1.replace("-", " 月 ", 1)
# date1 += " 日"
# print(date1)

#3.random module  ------------------------------------------------------
# import random as r1 #  randint(1,10)
# for i in range(0,5) :
#      print(r1.randint(1,10), end = ',') # 1 to 10 random
# print()
# #  randrange(1,10,2) ---------------------------
# for i in range(0,5) :
#      print(r1.randrange(0,10,2), end = ',') # 0,2,4,6,8 random not-inculde 10
# #   random()--> 0~1 之間的float random ---------
# print(r1.random())  # 0.8269503786181547
# print(r1.uniform(3,10))  # uniform  產生指定範圍的float亂數
# # Smaple1 --------------------------------------
# while True:
#    inkey = input("按任意鍵再按[ENTER]鍵擲骰子，直接按[ENTER]鍵結束:")
#    if len(inkey) > 0:
#        num = r1.randint(1,6)
#        print("你擲的骰子點數為：" + str(num))
#    else:
#        print("遊戲結束！"), break
# # choice(字串or 串列) 中 隨機取一個字--------------------------------------
# for i in range(0,5) :
#   print(r1.choice('abdfrtq'), end=',') # q,a,f,r,d,
# print()
# for i in range(0,5) :
#   print(r1.sample('abdfrtq',3), end=',') # ['b', 'd', 't']
#   print()
# # Sample 2 ---------------------------------------
# import random as r
# list1 = r.sample(range(1,50), 6)
# # special = list1.pop() # pop() 取出最後一個元素，並刪除
# list1.sort()
# print("本期大樂透中獎號碼為：", end="")
# for i in range(0,6):
#    if i == 5:
#        print(str(list1[i]))
#    else:
#        print(str(list1[i]), end=", ")
# # # print("本期大樂透特別號為：" + str(special))
# # # Sample 3 威力彩 ----------------------------------
# import random
# list2 = random.sample(range(1,9),1)   # random.sample
# special = list2[0]
# print("本期威力彩特別號為：" + str(special))
# print("本期威力彩中獎號碼為：", end="")
# list3 = random.sample(range(1,39),6)
# list3.sort()
# for i in range(0,6):
#   if i == 5:
#       print(str(list3[i]))
#   else:
#       print(str(list3[i]), end=", ")

# 4. Built in Function
# # abs()--------------------------------------------------
# a=-5
# b=abs(a)  #絕對值
# print(b)
# # chr()--------------------------------------------------
# a=65
# b=chr(a)  # 取得整數a 的字元
# print('b 的type =%s , b=chr(a)=%s'% (type(b),b))
# #Ans: b 的type =<class 'str'> , b=chr(a)=A
# # divmod()-商與餘數----------------------------------------------
# a,b =divmod(44,6) # 44/6 的商與餘數
# print("商=",type(a),a)          #商= <class 'int'> 7
# print("餘數=",type(b),b)        #餘數= <class 'int'> 2
# ret = divmod(44,6)      # ret = tuple  # (7, 2) <class 'tuple'>
# print("商=",type(ret[0]),ret[0])  #商= <class 'int'> 7
# print("餘數=",type(ret[1]),ret[1]) #餘數= <class 'int'> 2
# print(ret,type(ret))  # tuple 不可變更的list  #(7, 2) <class 'tuple'>
# # float() & int() & str()--------------------------------
# x=20
# a = float(x)  # 轉換成float 的資料型態 #<class 'float'> 20.0
# print(type(a),a)#
# b = str(a)    # 轉換成str 的資料型態   #<class 'str'> 20.0
# print(type(b),b)#
# c = int(a)    # 轉換成int 的資料型態   #<class 'int'> 20
# print(type(c),c)#
# # hex()-16 進位-------------------------------------------------
# x = 2000
# a = hex(x)  #16 進位
# print(type(a),a)
# # Ans: <class 'str'> 0x7d0
# # oct()-#8 進位-------------------------------------------------
# x = 200
# a = oct(x)  #8 進位
# print(type(a),a)
# # Ans: <class 'str'> 0o310
# max() & min() for list --------------------------------
list1=[1,2,3,4,5]
a=max(list1)    # max() for list
print(type(a),a)     #  <class 'int'> 5
a = min(list1)  #min()  for list
print(type(a),a)     #  <class 'int'> 1
# # pow() & id()--------------------------------------------------
# x = 3
# y = 4
# z = pow(x,y)  #x 的 y 次方
# print(type(z),'記憶體位置=',id(z),z) #id():記憶體位置
# x = 3
# y = 4
# z = pow(x,y,7)  #x 的 y 次方 /7 的餘數
# print(type(z),'記憶體位置='id(z),z) #id():記憶體位置
#
# # ord()--------------------------------------------------
# a = 'A'
# b = "Z"
# c = ord(a)  # unicode 編碼值
# d = ord(b)
# print('c 的type =',type(c),c)
# print('d 的type =',type(d),d)
# e = 'a'
# f = "z"
# g= ord(e)  # unicode 編碼值
# h = ord(f)
# print('c 的type =',type(g),g)
# print('d 的type =',type(h),h)
# # round () ----------------------------------------------
# a = 45.8234
# b = round (a,2)  #四捨五入取值到小數點幾位
# print('b 的type =',type(b),b)
# # sorted for list ---------------------------------------
# list1=[1,2,3,4,5]
# a = sorted(list1,reverse=True) #預設是升冪，reverse=True是降冪
# print(a)
# # sum() for list-----------------------------------------
# list1=[1,2,3,4,5]
# a = sum(list1)
# print(type(a),a)
# # Test6 : divmod ----------------------------------------
# person = int(input("請輸入學生人數: "))
# apple = int(input("請輸入蘋果總數: "))
# ret = divmod(apple, person)
# print("每個學生可分得蘋果 " + str(ret[0]) + " 個")
# print("蘋果剩餘 " + str(ret[1]) + " 個")
# # Test7 ------------------------------------------------
# innum = 0
# list1 = []
# while(innum != -1):
#    innum = int(input("請輸入電費 (-1：結束)："))
#    list1.append(innum)
# list1.pop()   # delete 最後輸出的 -1
# print("共輸入 %d 個數" % len(list1))
# print("最多電費為：%d" % max(list1))
# print("最少電費為：%d" % min(list1))
# print("電費總和為：%d" % sum(list1))
# print("電費：{}".format(list1))
# print("電費由大到小排序為：{}".format(sorted(list1, reverse=True)))

