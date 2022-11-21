# 1 Python 資料型態
# (1) bool  :    True,False               # 不可變
# (2) int   :    47,25000                 # 不可變
# (3) float :    3.14, 2.7e5              # 2.7*100000   不可變
# (4) complex :  5+9j, 3j                 # 不可變
# (5) str   :   'alas','alack'            # string       不可變
# (6) list  :   ['Winken' ,'Blinken']     # 可變
# (7) tuple :   (2,4,8)                   # 不可變
# (8) bytes :   b'ab\xff                  # 不可變
# (9) set   :   set([3,5,7])  # {3,5,7}   # 可變
# (10) dict :   {'game':'bingo' , 'dog':'dingo' , 'drummer':'Ringo'}   # 可變

# 2 Python 變數的命名規則
# (1)
# 小寫字母
# 大寫字母
# 數字(0~9)
# 底線(_)
# (2) 有區分大小寫
# (3) 開頭不可使用數字
# (4) 底線開頭的名稱會被特殊對待
# (5)不可使用保留字(關鍵字) :# https://docs.python.org/3/reference/index.html
# The following identifiers are used as reserved words, or keywords of the language, and cannot be used as ordinary identifiers. They must be spelled exactly as written here:
# False await else import pass
# None break except in raise
# True class finally is return
# and continue for lambda try
# as def from nonlocal while
# assert del global not with
# async elif if or yield

## test1 ------------------------------------------------
# num1 =34
# num2 = 67.83
# flag = True
# str1 = 'This is string'
# print(num1,'\n',num2,'\n',flag'\n',str1)
#
# d = set([3,5,7])  # {3,5,7}
# # 2.print() & pprint()
# print (d) # {3,5,7}

## test2 Print
# print("first way---------------------------------")
# print(100, 60, sep="&", end="\n")

# # second method :%s,%d,%8.2f(int=5 + .=1 + decimal=2)
# print("second way---------------------------------")
# name = "mika"
# score = 80
# price = 23.3
# print("%s grades is %d and price is %6.2f" % (name, score, price))
# print("姓名   座號  國文  數學  英文")
# print("%3s  %2d   %3d   %3d  %3d" % ("林大明", 1, 100, 87, 79))
# print("%3s  %2d   %3d   %3d  %3d" % ("陳阿中", 2, 74, 88, 100))
# print("%3s  %2d   %3d   %3d  %3d" % ("張小英", 11, 82, 65, 8))

# print("Third way---------------------------------")
# print("{} grates is {} and price is {}".format(name,score,price))

# print("Fourth way--------------------------------")
# print(f"{name} grates is {score} and price is {price}")
# print("www","runoob","com",sep=".")  # 设置间隔符
###-------------------------------------------
# import time
# print("---RUNOOB EXAMPLE ： Loading 效果---")
# print("Loading",end = "")
# for i in range(5):
#     print(".",end = '',flush = True)
#     time.sleep(0.5)
# print('\n')
##-------------------------------------------
# from pprint import pprint as pp
# data = {'powers': [0,
#                    1,
#                    1024,
#                    59049,
#                    1048576,
#                    9765625,
#                    60466176,
#                    282475249,
#                    1073741824,
#                    3486784401]}
# pp(data)
# print(data)
## 簡單python 運算
# x = 5
# y = x+6
# print(y)
# type(y)     # type is get 資料的型別 :  ex: y 的資料型別是 int

## Test3  Automatic conversion of data types ------------
# num1 = 5 +7.8
# print(f'num1(float) = {num1}')
# num2 = 5 + True   # True = 1
# print(num2)
# num3 = 5 + False  # False = 0
# print(num3)
# num4 = bool(False+1)
# print(num4)
# num5 = int(num1)
# print(num5)
# num6 = float(num2)
# print(num6)
# str1 = str(num1)
# print(f'str1(string) ={str1}')

## Test4 input --------------------------
# nat = input("請輸入國文成績：")
# math = input("請輸入數學成績：")
# eng = input("請輸入英文成績：")
# sum = int(nat) + int(math) + int(eng)  #輸入值需轉換為整數
# average = sum / 3
# print("成績總分：%d，平均成績：%5.2f" % (sum, average))

## Test5 if …elif….else ---------------------------
# pw = input("請輸入密碼：")
# if(pw=="1234"):
#     print("歡迎光臨！")
# else:
#     print("密碼錯誤！")
## -------------------------------------
# score = int(input("請輸入成績："))
# if(score) >= 90:
#     print("優等")
# elif(score) >= 80:
#     print("甲等")
# elif(score) >= 70:
#     print("乙等")
# elif(score) >= 60:
#     print("丙等")
# else:
#     print("丁等")
##------------------------------------------
# money = int(input("請輸入購物金額："))
# if(money >= 10000):
#     if(money >= 100000):
#         print(money * 0.8, end=" 元\n")  #八折
#     elif(money >= 50000):
#         print(money * 0.85, end=" 元\n")  #八五折
#     elif(money >= 30000):
#         print(money * 0.9, end=" 元\n")  #九折
#     else:
#         print(money * 0.95, end=" 元\n")  #九五折
# else:
#     print(money, end=" 元\n")  #未打折
# t4 lab4-3  os module can call exe :os.popen(exeName)------------------
# import os
# while True:
#      cmd1 = input('''
#                    press 1 - calc
#                    press 2 - notepad
#                    press 0 - quit
#                    Hello Master, what can I do for you ?   ''')
#      if cmd1 == '0':
#            break
#      elif cmd1 == '1':
#            os.popen('calc')
#      elif cmd1 == '2':
#            os.popen('notepad')
#      else :
#            print("Sorry Master,I can't understand what you say.")
# print("ok, I will quit. See you again my master ~~")
# t5 -----------------------------------------------
# print('*'*15)
# for x in range(6):
#    print('*',end='')
#    print(' '*13,end='')
#    print('*')
# print('*    Hello    *')
# for x in range(6):
#    print('*',end='')
#    print(' '*13,end='')
#    print('*')
# print('*'*15)
# # t6 Lab4-7.py-------------------------------------------------
# import random
# ans = random.randint(1,100)
# for i in range(1,11):
#    youans = int(input(str(i)+' You guess: '))
#    if youans > ans:
#        print('guess less')
#    elif youans < ans:
#        print('guess more')
#    else:
#        print('Correct !!')
#        break
# print('End')

# Bases 底數 ------------------------
a = 0x10
print('0x10 (16 進位)=',a)
b = 0b10
print('0b10 (2進位)=',b)
c = 0o10
print('0o10 (8進位)=',c)

# 轉換進位 -------------------
value =65
print('2進位 65 =', bin(65))
print('8進位 65 =', oct(65))
print('16進位 65 =', hex(65))

# ASCII code 轉換------------------
a = 65
b = chr(65)
print('chr(65) =', chr(65))

print("ord('A')= ", ord('A'))


