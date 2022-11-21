# 補充: for PyCharm
# (1) 比較source code 不同 for debug
#     在 ***.py 按下滑鼠右鍵-> 弹出菜单再点击Compare With进入选择要比较的文件界面，选择另一個.py
# (2) 備份程式在Git Hub :
#     step 1.

# 1 .Pycharm Hot Key
# ctrl+alt+L        : 自動排列對齊程式碼
# ctrl+shift+F10    : 執行程式
# alt+enter         : 自動修正語法錯誤
# shift+F6          :
# ctrl+Q            : 快速提式文件
# ctrl+/            : open/close 註解

# python -m pip install --upgrade pip
# pip list
# pip install --upgrade setuptools
# pip install ipython pyreadline jupyter jupyterlab
# pip list

# help(print)  # 查詢指令
# test1 ---------------------
# def say_hello(name):
#        print('hi:%s'%name)
# say_hello("Tom")

# test2----------------------
# import pip
# import ipython_genutils
# import sys
#
# print("current module=", __name__)      #  __name__ : 這個檔案的模組名稱
# print("pip moudle name=", pip.__name__) #  __name__ : pip 模組的名稱
# print("ipython module name=", ipython_genutils.__name__)
# Test1 ----------------------------------
# import os
# print('hello world')
# print(os.getcwd())  # 目前工作目錄
# # Test2 ----------------------------------
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#     print('hello world')
#     print(os.getcwd())
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':   # 主程式: 程式進入點
#     print_hi('PyCharm')

# test3 費事定理 : Fn =Fn-1 +Fn-2---------------------------------
# import sys
#
# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a + b
#     print()
# fib(100)

# test4 : in CMD run : python CH01.py 50  -------------
# import sys
# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a + b
#     print()
#
# print(sys.argv) # 執行才輸入值 ['CH01.py', '50']
# fib(100)

# test5  in CMD Run : python CH01.py 50-------------------------------------------
# import pip
# import ipython_genutils
# import sys
#
# print("current module=", __name__)
# print("pip moudle name=", pip.__name__)
# print("ipython module name=", ipython_genutils.__name__)
#
#
# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a + b
#     print()
#
#
# print(sys.argv)
# fib(int(sys.argv[1]))

# demo5  demo4 is ---------------------
# import demo4
# import sys
# for p in sys.path:
#     print(p)
#
# demo4.fib(200)

# ps : demo4 =============================================
# import pip
# import ipython_genutils
# import sys
#
# print("current module=", __name__)
# print("pip moudle name=", pip.__name__)
# print("ipython module name=", ipython_genutils.__name__)
#
#
# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a + b
#     print()
#
#
# if __name__ == '__main__':
#     print(sys.argv)
#     fib(int(sys.argv[1]))

# ps :  https://pypi.org/  -> you can Find, install and publish Python packages with the Python Package Index
# ps :  https://www.lfd.uci.edu/~gohlke/pythonlibs/ -> unofficial windows binaries for python Extension  packages
# in terminal(CMD) key
#     pip list
#     pip list --format=columns
#     pip list --format=freeze
#     pip freeze
#     pip list --format=json

#demo6 : step1. New/python package  create 'sample' ==========================
# step2. New/python file create math_util.py under sample

# step3 : math_util.py ----------
# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a + b
#     print()

# method 1--------------
#import sample.math_util
# sample.math_util.fib(200)

# method 2 ---------------
# from sample.math_util import fib #sample is package,math_util.py is module,fib is function
# fib(50)

# in  sample package has __init__.py 放出史話內容
# step1 :  __init__.py ------------------------
# sample_string="sample_utility"
# step2 : math_util.py-------------------------
# from sample import sample_string
#
# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a + b
#     print()
#
# def header():
#     print(sample_string)

# step3------------------------------------
# import sample.math_util
# sample.math_util.header()  #__init__() 可以直接使用裏面的變數&function

# step3 可已換成下列程式
# import sample
# print("call __init__.py string from sample package:", sample.sample_string)
# ------------------------
# import sample.math_util
# print("call from math_util:",sample.math_util.sample_string)

# demo7 ------------------------------
# print(2 ** 32)
# print(2 ** 64)
# print(2 ** 512)
# print("In decimal", 100)
# print("In binary", 0b100)
# print("In octal", 0o100)
# print("In hex", 0x100)
# x1 = 100
# print(f"100 in binary {x1:b}")
# print(f"100 in oct {x1:o}")
# print(f"100 in hex {x1:x}")
# print(f"100 in hex {x1:d}")
# print(5 ** 7, 7 ** 5)
# print(5 ^ 7, 7 ^ 5) #5 =101 ， 7 = 111 ，^f 取相異的 =1, result=010=2
# p1 = 5
# p2 = 7
# print(f"5 in binary{p1:b}, 7 in binary{p2:b}")

# # demo8 ------------------------------------------
# x1 = 5
# x2 = 3.14
# x3 = 5 + 4j
# x4 = 'hello'
# x5 = "world"
# x6 = '''中文'''
# x7 = b'hello' # bytes
# x8 = True
# x9 = False
# x10 = None
# l1 = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]
# for l in l1:
#     print(type(l), l)
# print(x3 + x3, x3 - x3, x3 * x3)
# print(abs(x3))
# import math
#
# print(math.sqrt(x3.real ** 2 + x3.imag ** 2))
# print('========================================')
# a1 = '500'
# a2 = '3.14'
# a3 = 'True'
# a4 = '5-4j'
# a5 = 'False'
# a6 = ''
# a7 = 0
# a8 = None
# b1 = int(a1)
# print(type(b1), b1)
# b2 = float(a2)
# print(type(b2), b2)
# b3 = bool(a3)
# print(type(b3), b3)
# b4 = complex(a4)
# print(type(b4), b4)
# b5 = bool(a5)
# print(type(b5), b5)
# b6 = bool(a6)
# print(type(b6), b6)
# b7 = bool(a7)
# print(type(b7), b7)
# b8 = bool(a8)
# print(type(b8), b8)
# b9 = float(a1)
# print(type(b9), b9)

# demo10 ------------------------------------
# from distutils.util import strtobool   # strtobool
#
# strings = ['True', 'true', 'TRUE', 'False', 'false', 'FALSE']
# for s in strings:
#     print(s, "becomes", strtobool(s))

# demo11 -----------------------------------------
# import ast
#
# a1 = None
# a2 = None
# a3 = "None"
# print(a1 == a2, a1 is a2)
# print(a1 == a3, a1 is a3)
# print(type(a1), type(a3))
#
# b3 = ast.literal_eval(a3) # 與eval 相同。但是不合法的類型不能轉換
# print(type(b3), b3)
# b4 = None if a3 == "None" else a3
# print(type(b4), b4)
# b5 = eval(a3)
# print(type(b5), b5)
#
# str_list = '[1,2,3,4]'
# chg_list = eval(str_list)  #eval 將str轉成Llist，tuple，dictionary
# print(chg_list)

# demo12 -----------------------------------------
# def twice(number: float)->float: # float 視為提示，而非強迫轉換型別
#     return 2 * number
#
#
# print(twice(2.54),type(twice(2.54)))      # 5.08 <class 'float'>
# print(twice(500),type(twice(500)))        # 1000 <class 'int'>
# print(twice("5000"),type(twice("5000")))  # 50005000 <class 'str'>

# demo13 執行時期檢查型別錯誤 : pip install mypy  ----------------------
# 字面常數就是直接寫進 Python 程式原始碼的數值
# from typing import Literal
#
#
# def setDirection(direction) -> None: # 提示
#     if direction == "EAST":
#         print("0")
#     elif direction == "NORTH":
#         print("90")
#     elif direction == "WEST":
#         print("180")
#     elif direction == "SOUTH":
#         print("270")
#
#
# setDirection("EAST")
# setDirection("NORTH")
# setDirection("WEST")
# setDirection("SOUTH")
# print("then NW...")
# setDirection("NW")
#
#
# def setDirection2(direction: Literal["EAST", 'NORTH', 'WEST', "SOUTH"]) -> None: # Literal : 提示的Type
#     if direction == "EAST":
#         print("0")
#     elif direction == "NORTH":
#         print("90")
#     elif direction == "WEST":
#         print("180")
#     elif direction == "SOUTH":
#         print("270")
#
# setDirection2("EAST")
# setDirection2("NORTH")
# setDirection2("WEST")
# setDirection2("SOUTH")
# print("then NW...")
# setDirection2("NORTHX")
# print(b"Hello")
# print(b"333-3333")
# print(b'abc')
# print(b'1')

# demo14 使用一個模組放自己的常數----------------------------------------------
# step1 :new/python package : constant
# step2 : in constant package : new python file : my_const.py (my_const is module)
# my_const.py --------------
# PI = 3.14
# GRAVITY = 9.8
# MAX_CONCURRENT_JOB = 2500
# source code ,demo14.py -------------------------
# import constant.my_const as const  # 使用一個模組放自己的常數
# import math
# print(const.PI)
# print(const.GRAVITY)
# print(const.MAX_CONCURRENT_JOB)
# # not good
# const.PI -= 1
# print(const.PI)
# # if really need pi, use system
# print(math.pi)

# demo15 math expression --------------
# x = 5
# y = 7
# print(x + y, x - y, x * y)       # 12 -2 35
# print(x / y, y / x, y // x, y % x)  #0.7142857142857143 1.4 1 2// : 整數除法   % : 餘數
# print(x ** y, y ** x)     #78125 16807
# print(round(1.4), round(2.4), round(3.4))   # 1 2 3 :  round() 四捨五入
# print(round(1.6), round(2.6), round(3.6))   # 2 3 4
# print(round(1.5), round(2.5), round(3.5))   # 2 2 4 遇到5偶數不進位，奇數進一位
# print(round(135.5), round(24.5))            #136 24
# print(round(135.4), round(24.6))            #135 25

# demo16 ------------------------------------
# x = 5
# print(x)
# print(x := 6)   # name : = expr ，直接指定 x=6
# print(x)
#
# inputs = list()
# current = input("write something from user:")
# while current != "quit":
#     inputs.append(current)
#     current = input("write something from user:")
#
# print(inputs)
# demo17 ---------------------------------------
# inputs = list()  # 此方式好 --> Demo 16 修正
#
# while True:
#     current = input("write something from user:")
#     if current == "quit":
#         break
#     inputs.append(current)
#
# print(inputs)

# # demo18 ---------------------------------------
# inputs = list()   # 直接指定並判斷，比Demo 17 好
#
# while (current := input("write something from user:")) != "quit":  #  := 直接指定數值
#     inputs.append(current)
#
# print(inputs)
# #
# # demo19 ---------------------------------------
# x = 5
# print("x=", x, hex(id(x))) # hax():Return the hexadecimal representation of an integer.
#
# x = 6
# print("x=", x, hex(id(x)))
#
# l1 = [5]
# print("l1=", l1, hex(id(l1)))
# print("l1[0]=", l1[0], hex(id(l1[0])))
# l1[0] = 6
# print("l1=", l1, hex(id(l1)))
# print("l1[0]=", l1[0], hex(id(l1[0])))
#
# # List ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# demo20
# l1 = ['A', 'B', 'C']
# l2 = l1
# l3 = ['A', 'B', 'C']
# print(l1, l2, l3)       # ['A', 'B', 'C'] ['A', 'B', 'C'] ['A', 'B', 'C']
# print(l1 == l2, l1 == l3)  # True True
# print(l1 is l2, l1 is l3)
# l1[0] = 'a'
# l2[1] = 'b'
# print(l1, l2, l3)

# demo21 # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# list1 = []
# list2 = ['X']
# list3 = ['X', 'Y', 'Z']
# list4 = [1, 2, 3]
# list5 = ['X', 2, 3]
# print(type(list1), type(list2), type(list3), type(list4), type(list5)) #<class 'list'>
# print(len(list1), len(list4)) # 0 3
# list6 = list()
# print(type(list6), len(list6)) # <class 'list'> 0
# print(list1 == list6, list1 is list6) # True False  # == 是 equal的概念(比值) 是identical(記憶體位置需相同)
# list7 = list('XYZ')
# print(list3, list7)                      # ['X', 'Y', 'Z'] ['X', 'Y', 'Z']
# print(list3 == list7, list3 is list7)    #True False
# print(list3[0], list5[0], list3[0] == list5[0], list3[0] is list5[0]) # X X True True
# print(list3[int(0.5)])  # X

# demo22 ------------------------------------
# l1 = list("ABCDEFG1234567")
# print(l1.count("A"))
# print(l1, 'count=' , len(l1)) # index = 0 to 13 ，count= 14
# print(l1[0], l1[len(l1) - 1]) # first & final  #A 7
# print(l1[-1], l1[-len(l1)])   # final & first  #7 A
#
# print(l1[2:5])          # ['C', 'D', 'E'] , 2 to 4 index 的值
# print(l1[:5], l1[5:])   #['A', 'B', 'C', 'D', 'E'], index 0 to 4  &  ['F', 'G', '1', '2', '3', '4', '5', '6', '7'] 5 to final
# print(l1[-5:-2])        # ['3', '4', '5']倒數第5個 to  倒數第3個 (負號從最後開始算，final =-1)
#
# print(l1[:-5], l1[-5:]) #['A', 'B', 'C', 'D', 'E', 'F', 'G', '1', '2'],0 to 倒數第6個 & ['3', '4', '5', '6', '7']倒數第5個 to final
# print(l1[2:5], l1[5:2]) # ['C', 'D', 'E'], l1[5:2] = [] (不能用)
# print(l1[::2])          #['A', 'C', 'E', 'G', '2', '4', '6'] , All 間隔2的index
# print(l1[5:2:-1]) # ['F', 'E', 'D'] # 5 to 3

# demo23----------------------------------------
# x1 = ['X', 'Y', 'Z', 1, 2, 3]
#
# for x in x1:
#     print(type(x), x)
#     print(2 * x)
#
# for p in x1:
#     if isinstance(p, int):  # isinstance(p, int) : p is int =True， isn't = False
#         print(p / 2)
#     else:
#         print(p," is not support for divide")

# demo24 numpy ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# in Terminal
# pip install numpy
# import numpy as np
# l1 = list('ABCDE')
# print(f'l1 = {l1}')
# print(f'l1 + l1 = {l1 + l1 }')
# print(f'l1 * 3 = {l1 * 3}')
# print(f'3 * l1 = {3 * l1}')
# del l1[2]
# print(l1)
#
# l2 = [1, 2, 3, 4, 5]
# print(" np.array + - * /--------------------------")
# print(f'l2 = {l2}')
# print(f'l2+l2 = {l2+l2}')
# a2 = np.array(l2)
# print(a2)
# print(f'a2+a2, a2-a2, a2*a2,a2/a2 , a2**a2 ={a2+a2, a2-a2, a2*a2,a2/a2,  a2**a2}')

# demo25 ----------------------------------
# l1 = list('ABCDEFG1234567')
# for l in l1:
#     print(l)
# l2 = ['apple','banana','cookie']
# for l in l2:
#     print(l)
#
# l3 = [l for l in l1]
# print(f'l3 = {l3}')
# print([l for l in l1])
# print([l for l in l2])
# print('A' in l1, 'a' in l1, 'A' not in l1)
# print('apple' in l2, 'a' in l2)
#
# print('------------ phase 2 ----------------')
# print(l1.index('C'), l1.index('5'))
# # key1="COOKIE" or key1='C'
# key1 = "C"
# if key1 in l1:
#     print(l1.index(key1))
# else:
#     print(False)
# #print(l1.index('COOKIE'))

# demo 25_1 -------------------------------------------
# l1 = list('ABCDEFG1234567')*2
# for l in l1:
#     print(l)
# l2 = ['apple','banana','cookie']
# for l in l2:
#     print(l)
#
# print([l for l in l1])
# print([l for l in l2])
# print('A' in l1, 'a' in l1, 'A' not in l1) # True False False
# print('apple' in l2, 'a' in l2) # True False
# #phase 2
# print(l1.index('C'), l1.index('5')) #2 11
# # key1="COOKIE" or key1='C'
# key1 = "C++"
# if key1 in l1:
#     print(l1.index(key1))
# else:
#     print(False)   # False
# #print(l1.index('COOKIE'))
# print("using short hand, k1 index=")
# print(key1 in l1 and l1.index(key1)) #False

# demo26 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# a = True
# bs = [500, True, False, None, "Hello World", 1000.3]
# print("a=True,bs= [500, True, False, None, 'Hello World', 1000.3]")
# print('-----------a and b ---------------')
# for b in bs:
#     print(a and b)  # a=True, b是原來的
#
# print("----------- a=False, a and b -------------")
# a = False
# for b in bs:
#     print(a and b) # all is False
# print("---a=False, or condition--")
# for b in bs:
#     print(a or b) # a=False，b是原來的
#
# print("---a=True, or condition--")
# a = True
# for b in bs:
#     print(a or b)  # all is True


# demo27 append() 從list 後面加入---------------------------------------
# x1 = ['a', 'b', 'c']
# x2 = ['a', 'b', 'c']
# x3 = ['a', 'b', 'c']
# a1 = 'd'
# x1 = x1 + [a1]
# print(f"x1 + [a1] = {x1}")
#
# x2.append(a1)
# print(f'x2.append(a1)={x2}')
# x3.extend(a1)
# print(f'x3.append(a1)={x3}')
# print("a2 = ['e', 'f']")
# a2 = ['e', 'f']
# x1 += a2
# print(x1) #['a', 'b', 'c', 'd', 'e', 'f']
#
# x2.append(a2) #['a', 'b', 'c', 'd', ['e', 'f']],append() 只能1個1個加入
# print(x2)
# x3.extend(a2) # 2 個含以上 加入，用extend()
# print(x3)  # ['a', 'b', 'c', 'd', 'e', 'f']

# demo28 insert & remove & sort -------------------------
# x1 = ['P', 'Q', 'R', 'S', 'T']
# x1.insert(0, '*')  # index=0，insert  '*'
# x1.insert(0, '*')
# print(x1)     # ['*', '*', 'P', 'Q', 'R', 'S', 'T']
#
# x1.insert(8, '!')
# print(x1)     # ['*', '*', 'P', 'Q', 'R', 'S', 'T', '!']
#
# x1.remove('*')
# print(x1)
# x1.remove('*')
# print(x1)   # ['P', 'Q', 'R', 'S', 'T', '!']
#
# print('---sort----')
# x2 = [3, 1, 5, 4, 2, 7, 19, 31, 4, 1, 3]
# x2.sort() # samll to big  [1, 1, 2, 3, 3, 4, 4, 5, 7, 19, 31]
# print(x2)
# x2.sort(reverse=True)
# print(x2) # big to small [31, 19, 7, 5, 4, 4, 3, 3, 2, 1, 1]
#
# # x3 = [1, 2, 3, 'A', 'B', 'C', 'a', 'b', 'c']
# # x3.sort()  #不能排序
# # print(x3)
# x4 = ['1', '2', '3', 'A', 'B', 'C', 'a', 'b', 'c']
# x4.sort(reverse=True) # big to samll ['c', 'b', 'a', 'C', 'B', 'A', '3', '2', '1']
# print(x4)
# x4.sort()   # small to big  ['1', '2', '3', 'A', 'B', 'C', 'a', 'b', 'c']
# print(x4)
#
# x5 = list("QWERTYUIOPqwertyuiop")
# x5.sort(key=str.lower, reverse=True) #['Y', 'y', 'W', 'w', 'U', 'u', 'T', 't', 'R', 'r', 'Q', 'q', 'P', 'p', 'O', 'o', 'I', 'i', 'E', 'e']
# print(x5)

# demo 29 list & string 都支援 index, 切割， in ,not in , for loop ----------------
# s1 = "ABCDE"
# l1 = list(s1)
# l2 = list(s1)
#
# print([x for x in s1])
# print([x for x in l1])
# print("A" in s1, "A" in l1)
# print(s1[2:], l1[2:])
# print("l1", hex(id(l1))) # l1 0x1903ed9e9c0
# l1 += ['F']
# print("l1", hex(id(l1)))  # l1 0x1903ed9e9c0 : id 一樣的
# print("l2", hex(id(l2)))
# l2.append('F')
# print("l2", hex(id(l2)))  # id 一樣的
#
# print(hex(id(s1)))    # 0x1903ed37e30
# s1 += 'F'
# print(hex(id(s1)))    #0x1903eda5ef0   , string id 不一樣
# print(l1)
# print(l2)
# print(s1)
#
# l1[0] = '*'  # list is mutable 可變
# print(l1)
# # s1[0]='*'  # string is immutable 不可變

# Demo 30 變數互換值  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# x1 = []
# x2 = ()
# x3 = {}
# print(type(x1), type(x2), type(x3))  # <class 'list'> <class 'tuple'> <class 'dict'>
# x4 = [5]
# x5 = (5)  # x5 = (5,) 才是 tuple
# x6 = {6}
# print(type(x4), type(x5), type(x6))   # <class 'list'> <class 'int'> <class 'set'>
# x7 = (7,)
# x8 = {'k1': 6}
# print(type(x7), type(x8))
# print('----type End!-------')
# a1 = 5
# a2 = 3
# print(a1, a2)
# t = a1
# a1 = a2
# a2 = t
# print(a1, a2)  # a1 , a2 互換
# a3, a4 = 5, 3
# print(a3, a4)
# a3, a4 = a4, a3   # a3 , a4 互換，python 語法
# print(a3, a4)
#
# a5 = 'hello world'
# a6 = 3.14159
# print(a5, a6)   # hello world 3.14159
# a5, a6 = a6, a5
# print(a5, a6)   # 3.14159 hello world
#
# c1, c2, c3, c4, c5 = 'A', 'K', 'Q', 'J', '10'
# p1, p2, p3, p4, p5 = c4, c2, c3, c1, c5
# print(p1, p2, p3, p4, p5)  #J K Q A 10
# # t4 = ('A','K','Q')
# # t4[0]=1

# # demo31 list & tuple 可互換型別 tuple(list1) list(tuple1) ------------------
# x1 = [1, 2, 3]
# x2 = (1, 2, 3)
# print(type(x1), type(x2))  # <class 'list'> <class 'tuple'>
# x3 = tuple(x1)
# x4 = list(x2)
# print(type(x3), type(x4))  # <class 'tuple'> <class 'list'>
# x4.append(4)
# print(x4)          # [1, 2, 3, 4]
# print(hex(id(x3)))
# x3 += (4,)
# print(hex(id(x3)))  # id 不一樣
# print(x3)  #

# demo32 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# a1 = 5
# a2 = a1
# print(a1, a2)
# a1 = 6
# print(a1, a2)
# l1 = [5]
# l2 = l1
# print(l1, l2)
# l1[0] = 6
# print(l1, l2)  # [6] [6]
#
#
# def addAnimal(parameter):
#     parameter.append('zebra')
#
#
# animals = ['alpaca', 'baboon']
# addAnimal(animals)
# print(animals) # ['alpaca', 'baboon', 'zebra']

# Demo 33 copy & deepcopy~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import copy
#
# x1 = list('abcdefg')
# x2 = x1
# x3 = list(x1)
# x4 = x1[:]
# x5 = copy.copy(x1)        # 淺複製僅複製容器中元素的地址
# x6 = copy.deepcopy(x1)    # 深複製完全複製了一份副本，容器與容器中的元素地址都不一樣
# print(x1,'\n', x2,'\n', x3,'\n', x4,'\n', x5,'\n', x6)
# x1[0] = 'A'
# x2[1] = 'B'
# print(x1, x2, x3, x4, x5, x6)

# Demo 34~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import copy
# import numpy
#
# player1 = [['A', 'K'], ['Q', 'J']]
# player2 = player1    #  player1 改變， player2 改變
# player3 = copy.copy(player1)     #  player1 改變， player2 不改變
# player4 = copy.deepcopy(player1) #  player1 改變， player2 不改變
#
# print(player1, player2, player3, player4)
# player1.append('Joker')
# print(player1, player2, player3, player4)
# player1[0][0] = '2'
# print(player1, player2, player3, player4)
# a1 = numpy.array([1, 2, 3])
# a2 = a1          #  a1 改變， a2 改變
# a3 = a1.copy()   #  a1 改變， a3 不改變
# print(a1, a2)
# a1 *= 2
# print(a1, a2)
# print(a1, a2, a3)

# dictionary ----------------------------------
# demo35 ---------------------------------------
# d1 = {'name': 'python', 'duration': 35}
# d2 = {'duration': 35, 'name': 'python'}
# print(d1)
# print(d2)
# print(type(d1), type(d2), d1 == d2, d1 is d2)  #True False,  dictionary 沒有固定順序 --> d1 == d2 is True
# print(d1['name'], d2['duration'])
# # print(d1['XYZ'])
# k1 = 'name'
# print(k1 in d1 and d1[k1])
# d3 = dict(name='python', duration=35)
# d4 = dict([("name", 'python'), ('duration', 35)])
# print(d1 == d2, d1 == d3, d1 == d4)

# demo36 --------------------------------------
# sales = {'iphone12': 100, 'iphone12Pro': 120, 'iphone12ProMax': 80, 'ipad': 200, 'appleWatch': 60}
# for s in sales:
#     print("key={}, value={}".format(s, sales[s]))
#
# for k in sales.keys():
#     print("[keys()]key={}, value={}".format(k, sales[k]))
#
# total = 0
# for v in sales.values():
#     total += v
# print("total amount={}".format(total))
# for item in sales.items():
#     print(type(item), item, item[0], item[1])
#
# for k, v in sales.items():
#     print("key={}, value={}".format(k, v))

# demo37~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# reports = ['s', 's', 'm', 'l', 'xl', 's', 'm', 'l', 'xl', 'm', 'l', 'xl', 's', 'm', 's', 's', 'm', 'ss']
#
# table = {}
# # table = {'s': 0, 'm': 0, 'l': 0, 'xl': 0}
# print(type(table))   # <class 'dict'>
# for report in reports:
#     table.setdefault(report, 0)
#     table[report] = table[report] + 1   # {'s': 6, 'm': 5, 'l': 3, 'xl': 3, 'ss': 1}
# print(table)

# demo38~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# reports = ['s', 's', 'm', 'l', 'xl', 's', 'm', 'l', 'xl', 'm', 'l', 'xl', 's', 'm', 's', 's', 'm', 'ss']
#
# table = {}
# # table = {'s': 0, 'm': 0, 'l': 0, 'xl': 0}
# print(type(table))
# for report in reports:
#     table.setdefault(report, 0)
#     table[report] = table[report] + 1
# print(table)
#
# reports2 = [("s", 20), ("m", 10), ("l", 5), ('xl', 5), ("s", 40), ("m", 20), ("l", 15), ('xl', 50)]
# total = {}
# for size, quantity in reports2:
#     total.setdefault(size,0)
#     total[size]=total[size]+quantity
#
# print(total)

# Demo39 集合 1.沒有順序，沒有索引，2.會刪除重複的 3. use add()& remove()~~~~~~~~
# s1 = {'A', 'P', 'P', 'L', 'E'}
# print(f's1 = {s1}')
# s2 = set(list("PINEAPPLE"))
# print(f's2 = {s2}')
#
# for p in s1:
#     print(p)
#
# s3 = set(list("BANANA"))
# print(f's3 = {s3}')
# print(s1|s3)  # 聯集 {'P', 'N', 'E', 'L', 'B', 'A'}
# print(s1&s3)  # 交集 {'A'}
# print(s1^s3)  # exclusive or ， 個別有的才是True = 聯集 -交集
# print(len(s1|s3))
# s2.add('X')
# print(s2)
# s2.remove('P')
# print(s2)
# #s2.remove('P')
# #s1.add(s2)

# Demo39~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# class Course:
#     def __init__(self, name, duration, instructor):
#         self.name = name
#         self.duration = duration
#         self.instructor = instructor
#
#
# c1 = Course('POOP', 35, "MarkHo")
# c2 = c1                           # 與c1 共用id
# c3 = Course('POOP', 35, "MarkHo")
# c4 = Course("BDPY", 35, "MarkHo")
# s1 = set()
# s1.add(c1)
# print("stage1, s1=", s1)     # stage1, s1= {<__main__.Course object at 0x000001D74E778460>}
# s1.add(c2)
# print("stage2, s1=", s1)     # stage2, s1= {<__main__.Course object at 0x000001D74E778460>}
# s1.add(c3)
# print("stage3, s1=", s1)     # stage3, s1= {<__main__.Course object at 0x000001D74E96B5E0>, <__main__.Course object at 0x000001D74E778460>}
# s1.add(c4)
# print("stage4, s1=", s1)     # stage4, s1= {<__main__.Course object at 0x000001D74E96B5E0>, <__main__.Course object at 0x000001D74E96B6A0>, <__main__.Course object at 0x000001D74E778460>}

# Demo39-1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# class Course:
#     def __init__(self, name, duration, instructor):
#         self.name = name
#         self.duration = duration
#         self.instructor = instructor
#
#     def __str__(self):
#         return "{}/{}/{}".format(self.name, self.duration, self.instructor)
#
#     def __repr__(self):
#         return str(self)
#
#
# c1 = Course('POOP', 35, "MarkHo")
# print(c1)
# c2 = c1
# c3 = Course('POOP', 35, "MarkHo")
# c4 = Course("BDPY", 35, "MarkHo")
# print(c1 == c2, c1 == c3, c1 == c4) # True False False
# print(c1 is c2, c1 is c3, c1 is c4) # True False False
# s1 = set()
# s1.add(c1)
# print("stage1, s1=", s1)  #stage1, s1= {POOP/35/MarkHo}
# s1.add(c2)
# print("stage2, s1=", s1)  #stage2, s1= {POOP/35/MarkHo}
# s1.add(c3)
# print("stage3, s1=", s1)  # stage3, s1= {POOP/35/MarkHo, POOP/35/MarkHo}
# s1.add(c4)
# print("stage4, s1=", s1)  # stage4, s1= {POOP/35/MarkHo, BDPY/35/MarkHo, POOP/35/MarkHo}

# demo39-2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# class Course:
#     def __init__(self, name, duration, instructor):
#         self.name = name
#         self.duration = duration
#         self.instructor = instructor
#
#     def __str__(self):
#         return "{}/{}/{}".format(self.name, self.duration, self.instructor)
#
#     def __repr__(self):
#         return str(self)
#
#     def __eq__(self, other):
#         return self.name == other.name and self.duration == other.duration and self.instructor == other.instructor
#
#
# c1 = Course('POOP', 35, "MarkHo")
# print(c1)
# c2 = c1
# c3 = Course('POOP', 35, "MarkHo")
# c4 = Course("BDPY", 35, "MarkHo")
# print(c1 == c2, c1 == c3, c1 == c4)
# print(c1 is c2, c1 is c3, c1 is c4)
# s1 = set()
# s1.add(c1)
# print("stage1, s1=", s1)
# s1.add(c2)
# print("stage2, s1=", s1)
# s1.add(c3)
# print("stage3, s1=", s1)
# s1.add(c4)
# print("stage4, s1=", s1)

# Demo 39-3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# class Course:
#     def __init__(self, name, duration, instructor):
#         self.name = name
#         self.duration = duration
#         self.instructor = instructor
#
#     def __str__(self):
#         return "{}/{}/{}".format(self.name, self.duration, self.instructor)
#
#     def __repr__(self):
#         return str(self)
#
#     def __eq__(self, other):
#         return self.name == other.name and self.duration == other.duration and self.instructor == other.instructor
#
#     def __hash__(self):
#         return hash((self.name, self.duration, self.instructor))
#
#
# c1 = Course('POOP', 35, "MarkHo")
# print(c1)                          # POOP/35/MarkHo
# c2 = c1
# c3 = Course('POOP', 35, "MarkHo")
# c4 = Course("BDPY", 35, "MarkHo")
# print(c1 == c2, c1 == c3, c1 == c4)  #True True False
# print(c1 is c2, c1 is c3, c1 is c4)  #True False False
# print(hex(hash(c1)), hex(hash(c2)), hex(hash(c3)), hex(hash(c4)))
# # -0x4468a5828843b2c8 -0x4468a5828843b2c8 -0x4468a5828843b2c8 0x585d307bce9c40b1
# s1 = set()
# s1.add(c1)
# print("stage1, s1=", s1)   # stage1, s1= {POOP/35/MarkHo}
# s1.add(c2)
# print("stage2, s1=", s1)   # stage2, s1= {POOP/35/MarkHo}
# s1.add(c3)
# print("stage3, s1=", s1)   # stage3, s1= {POOP/35/MarkHo}
# s1.add(c4)
# print("stage4, s1=", s1)   # stage4, s1= {POOP/35/MarkHo, BDPY/35/MarkHo}
# x1 = 7
# x2 = 7
# print(x1 is x2, x1 == x2)

# Day3 --------------------------------------
# demo40  if 條件判斷式
#
# def judge(inputScore):
#     return 'good' if inputScore >= 80 else 'bad' # condition is true if condition else condition_is_false
#
#
# score = 80
# x1 = judge(score)
# print('%d is %s' % (score, x1))
#
# score = 60
# x1 = judge(score)
# print('%d is %s' % (score, x1))
#
#
# def judge2(inputScore):
#     return ('bad', 'good')[inputScore >= 80]  # (if_test_is_false,if test_is_true)[test]
#
#
# score = 80
# x1 = judge2(score)
# print('%d is %s' % (score, x1))
#
# score = 60
# x1 = judge2(score)
# print('%d is %s' % (score, x1))

# demo41 if/else/   if/elif-------------------------------------
# scores = [70, 60, 80, 50, 90]
# def judge1(x):
#     if x < 60:
#         return 'fail'
#     else:
#         return 'success'
#
#
# for score in scores:
#     print(score, judge1(score))
#
#
# def judge2(x):
#     if x >= 90:
#         return 'A'
#     elif x >= 80:
#         return 'B'
#     elif x >= 70:
#         return 'C'
#     elif x >= 60:
#         return 'D'
#     else:
#         return 'fail'
#
# for score in scores:
#     print(score, judge2(score))

#demo42 for loop ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
#
# sum = 0
# for n in numbers:
#     sum += n
#
# print("sum={}".format(sum))   # sum=48
#
# numbers2 = [6, -5, 3, -8, 4, -2, 5, -4, 11]
#
# for n in numbers2:
#     if n < 0:
#         numbers2.remove(n)
# print(numbers2)              # [6, 3, 4, 5, 11]
#
# numbers3 = [6, -5, 3, -8, 4, -2, 5, -4, 11]
# print(f'numbers3 = {numbers3}')
# for n in numbers3[:]:    #[:] 修改到numbers 加[:] 加複本(for loop 中有改到numbers3的內容， 需要複本
#     if n < 0:
#         numbers3.insert(0, n)  # index 0 insert n ，numbers3 的順序改變了，需要複本，不然程式無法終結
# print(numbers3)

# demo43 range 迭代 ----------------------------------
# x = range(10)   # 產生 0 to 9 的序列
# print(type(x), len(x), x) # <class 'range'> 10 range(0, 10)
#
# y1 = list(x)
# print(y1)
# print([n for n in x])   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# print("-----[n for n in range(20)]-----")
# print([n for n in range(20)])
#
# x2 = range(10, 20, 2)   # 產生 10 to 20 間隔2的序列
# print(x2)
# print([n for n in x2])  # [10, 12, 14, 16, 18]
#
# for n in range(10):
#     print(n, end=' ')     # 0 1 2 3 4 5 6 7 8 9
# print()
#
# for i in range(10):
#     print("[%d]do something" % i)
#
# for _ in range(10):
#     print("do something")
#
# # demo44 -----------------------
# import numpy as np
# a1 = range(5, 50, 3) #start from 5 to 50的前一項 ，間隔 3
# print(list(a1))
#
# a2 = np.arange(0, 5, 0.1)   # 0 to 5的前一項
# print(a2)
#
# a3 = np.linspace(0, 5)     # num: Optional[int] = 50 (default)
# print(a3)
# print(f'a3_count = {len(a3)}')
#
# a4 = np.linspace(0, 5, 51) # # 0 to 5 間隔 共51個
# print(a4)

# demo45 # zip 配對   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# colors = ['red', 'green', 'blue', 'yellow']
# ratios = [0.08, 0.02, 0.03, 0.19]
# for i in range(len(colors)):
#     print(colors[i], ratios[i])
# print('-ZIP-------------------')
# for color, ratio in zip(colors, ratios):
#     print(color, ratio)
#
# products = ['apple', 'ibm', 'microsoft', 'oracle']
# prices = [2.5, 3.5, 1.9, 4.5]
#
# for product, price, color in zip(products, prices, colors):
#     print(f"{product} is {color} and cost ${price}")

# demo46 #~~~zip for list~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# a1 = [1, 2, 3]
# a2 = [4, 5, 6]
# a3 = zip(a1, a2)
# print(type(a3), a3)
#
# for element in a3:
#     print(type(element), element)    # <class 'tuple'> (1, 4)..., element is tuple 配對
#
# a4 = [7, 8, 9]
# a5 = zip(a1, a2, a4)
# for element in a5:
#     print(type(element), element)    #<class 'tuple'> (1, 4, 7)...
#
# a6 = a1 + a2 + a4
# print(a6)   # [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# a7 = list(zip(a1, a2, a4))
# print(a7)   # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
#
# print("numpy-hstack-vstack-------------") # stack 堆疊
# import numpy
#
# array1 = numpy.array([1, 2, 3, 4, 5])
# array2 = numpy.array([6, 7, 8, 9, 10])
# print(array1 + array2)               # [ 7  9 11 13 15]
# array3 = numpy.hstack((array1, array2))  # [ 1  2  3  4  5  6  7  8  9 10]
# print(array3)
# array4 = numpy.vstack((array1, array2))
# print(array4)
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]]

# while -----------------------------
# demo47 ----------------------------
# n = 200
# summation = 0
# counter = 1
# while counter <= n:
#     summation += counter
#     counter += 1
# else:
#     print("calculation terminated")
# print("sum from 1 until %d = %d" % (n, summation))

# demo47' # break~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# n = 200
# summation = 0
# counter = 1
# limit = 10000
# while counter <= n:
#     summation += counter
#     counter += 1
#     if summation > limit:
#         break
# else:
#     print("calculation terminated")
# print("sum from 1 until %d = %d" % (counter, summation))

# demo48 sys.stdin.read(1) like input()-------------------------------------------
# import sys
#
# text = ""
# print("Input something, when finished, press enter:")
# while True:
#     c = sys.stdin.read(1)    # 一次讀一個字
#     text = text + c
#     if c == '\n':
#         break
# print("Input:%s" % text)

# demo49  #---------------------------------
# data = [[1, 2, 3, -4, 5],
#         [6, 7, 8, 9, 10],
#         [1, 3, 5, 7, 9],
#         [2, 4, -6, 8, 10]]
# for row in data:
#     sum = 0
#     for col in row:
#         if col < 0:
#             print("got an outlier:%d" % col)
#             break
#         else:
#             sum += col
#     else:
#         print("row sum=%d" % sum)

# demo49'# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# data = [[1, 2, 3, -4, 5],
#         [6, 7, 8, 9, 10],
#         [1, 3, 5, 7, 9],
#         [2, 4, -6, 8, 10]]
# for row in data:
#     sum = 0
#     for col in row:
#         if col < 0:
#             print("got an outlier:%d" % col)
#             #break
#             #continue
#         else:
#             sum += col
#     else:
#         print("row sum=%d" % sum)

# demo49'' # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# data = [[1, 2, 3, -4, 5],
#         [6, 7, 8, 9, 10],
#         [1, 3, 5, 7, 9],
#         [2, 4, -6, 8, 10]]
# for row in data:
#     sum = 0
#     for col in row:
#         if col < 0:
#             print("got an outlier:%d" % col)
#             # break
#             continue
#
#         sum += col
#     else:
#         print("row sum=%d" % sum)

# demo50 # pass : 是1個 null 指令 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# for _ in range(10):
#     pass
# while False:
#     pass
# def func1():
#     pass
# class myClass():
#     pass
# class myClass():
#     def __init__(self):
#         pass
#     pass

# Python_Introduction file  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Python（英國發音：/ˈpaɪθən/ 美國發音：/ˈpaɪθɑːn/）是一種廣泛使用的直譯式、
# 進階程式、通用型程式語言。Python支援多種程式範式，包括物件導向、結構化、指令式、函數式和反射式程式。它擁有動態型別系統和垃圾回收功能，能夠自動管理記憶體使用，並且其本身擁有一個巨大而廣泛的標準庫。
#
# Python由吉多·范羅蘇姆創造，第一版釋出於1991年，它是ABC語言的後繼者，
# 也可以視之為一種使用傳統中綴表達式的LISP方言[6]。
#
# Python的設計哲學強調代碼的可讀性和簡潔的語法，尤其是使用空格縮排劃分代碼塊。
# 相比於C或Java，Python讓開發者能夠用更少的代碼表達想法。不管是小型還是大型程式，該語言都試圖讓程式的結構清晰明瞭。
#
# Python 直譯器本身幾乎可以在所有的作業系統中執行。
# Python的其中一個直譯器CPython是用C語言編寫的、是一個由社群驅動的自由軟體，目前由Python軟體基金會管理。
#
# enumerate多用於在for循環中得到計數，利用它可以同時獲得索引和值，即需要index和value值的時候可以使用

# *** enumerate can get index & value *** ----------------
# lst = [1, 2, 3, 4, 10, 5]
# print(enumerate(lst))
# for index,value in enumerate(lst):

#    print ('%s,%s' % (index,value))

# demo51 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  manual create a directory data
#  create a file Python_Introduction
# my_file = open('data/Python_Introduction', encoding='utf8')
#
# # *** enumerate 迭代檔案，一行檔案是一個索引(index) ***
# for i, line in enumerate(my_file):
#     print(i, line)
#
# my_file.close()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# manual create a directory data
# create a file Python_Introduction
# my_file = open('data/Python_Introduction', encoding='utf8')

# *** enumerate 迭代檔案，一行檔案是一個索引(index) ***
# for i, line in enumerate(my_file):
#     print(i, line)
#
# my_file.close()
#
# dayOfWeek = ['Sunday', 'Mondy', 'Tuesday', 'Wednesday']
# for index, d in enumerate(dayOfWeek):
#     print(index, d, len(d))

# try: except :
# demo52 : ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def xyz():
#     pass
#
# fileHandler1 = open("help/data1", 'w')
# fileHandler1.write("Hello world")
# fileHandler1.close()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def xyz():
#      pass
# try:
#     print("before open")
#     # data/data1
#     fileHandler1 = open("help/data1", 'w')
#     print("after open")
#     fileHandler1.write("Hello world")
#     print("after write")
#     fileHandler1.close()
# except:   # 所有例外狀況
#     print("oops exception happen")
# print("after close")

# IOError : 與file 有關的 ， TypeError ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def xyz():
#     pass

# try:
#     print("before open")
#     # data/data1
#     fileHandler1 = open("help/data1", 'w')
#     print("after open")
#     fileHandler1.write("Hello world")
#     print("after write")
#     fileHandler1.close()
# #except TypeError as error:
# except IOError as error:
#     print("oops io exception happen", error)
# print("after close")

# demo53 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def divide(x, y):
#     try:
#         result = x / y
#     except ZeroDivisionError:                 # 除 0 ERROR
#         print("ZeroDivisionError : divide by zero")
#     except TypeError:
#          print("TypeError:type not correct")
#     else:                             # try has not error run else
#         print("else:result is:", result)
#     finally:                          # 程式一定執行
#         print("finally: execution terminated")
# #divide(2, 0)
# #divide(2, 1)
# divide("2",'0')

# demo54 使用 raise: 拋出例外~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def myException(level):
#     if level < 1:
#         raise Exception('som reasons', 'some details')
# try:
#     myException(0)
# except Exception as e:
#     print("exception happen, as:", e)
# finally:
#     print("OK")
#
# try:
#     myException(3)
# except Exception as e:
#     print("exception happen, as:", e)
# else:
#     print("execution success")
# finally:
#     print("OK")

# demo54' ***for arg in e.args:   ~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def myException(level):
#     if level < 1:
#         raise Exception('some reasons', 'some details', "some suggestion", "contact numbers")
# try:
#     myException(0)
# except Exception as e:
#     print("exception happen, as:", e)
#     for arg in e.args:
#         print("get an argument:", arg)
# finally:
#     print("OK")
#
# try:
#
#     myException(3)
# except Exception as e:
#     print("exception happen, as:", e)
# else:
#     print("execution success")
# finally:
#     print("OK")

# 'demo55' 使用者定義的例外  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# class MyError(Exception):   # 繼承 Exception class(Exception 的屬性，method 皆可用)
#     def __init__(self, value):
#         self.value = value
#
#     def __str__(self):
#         return "error=%d" % (self.value)
#
# try:
#     raise MyError(2*2)
# except MyError as e:
#     print(e)          #error=4
#     print(e.value)    # 4


# function --------------------
# 'demo56'  # *** ''' XXX ''' 在function 中，是help 說明 help(somethingGreat) ~~~~~~-------------
# def somethingGreat():
#     """                  # help 說明
#     Demo python function purpose:
#     :return:
#     """
#     return "awesome"
#
# print('--------------------------------')
# print(somethingGreat())        # awesome
# print('--------------------------------')
# print(somethingGreat)          # <function somethingGreat at 0x0000021574B51EE0> : 記憶體本身
# print('--------------------------------')
# help(somethingGreat)
# # Help on function somethingGreat in module __main__:
# # somethingGreat()
# #    Demo python function purpose:
# #    :return:
# print('--------------------------------')
# help(somethingGreat())

# # 'demo57' * 指定keyword only argument ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def ping_to_m2(*, ping):    # 呼叫要指定 (ping=10) 使用 *
#     return ping * 3.3058
#
#
# def ping_to_m2_2(ping):
#     return ping * 3.3058
#
# def m2_to_ping(*, m_square):
#     return m_square*0.3025
#
# #print(ping_to_m2(10))
# print(ping_to_m2(ping=10))
# print(ping_to_m2_2(10))
# print(ping_to_m2_2(ping=10))
# print(m2_to_ping(m_square=10))
# 呼叫要指定 (ping=10) 使用 *~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def ping_to_m2(*, ping):
#     return ping * 3.3058
#
#
# def ping_to_m2_2(ping):
#     return ping * 3.3058
#
#
# def m2_to_ping(*, m_square):
#     return m_square * 0.3025
#
#
# def m2_to_price(*, m_square, price_per_ping):
#     return m_square * 0.3025 * price_per_ping
#
#
# # print(ping_to_m2(10))
# print(ping_to_m2(ping=10))
# print(ping_to_m2_2(10))
# print(ping_to_m2_2(ping=10))
# print(m2_to_ping(m_square=10))
# print(m2_to_price(m_square=10, price_per_ping=20000))

#demo58 # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def sample1(a, b, c):
#     print('a=', a)
#     print('b=', b)
#     print('c=', c)
#
# sample1("hello", 'world', 'welcome')
# sample1(a='hello', b='world', c='welcome')
# sample1("hello", 'world', c='welcome')
# sample1("hello", b='world', c='welcome')

# demo59 / : positional only argument ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def incrementBy1(x):
#     return x + 1
#
# print(incrementBy1(1), incrementBy1(x=2))    #2 3 不指定都可以
#
# def incrementBy1ONlyPosition(x, /):  # 使用 / only positoin 只能傳值，不能用鍵值但表參數
#     return x + 1
#
# print(incrementBy1ONlyPosition(5)) # 6
# #print(incrementBy1ONlyPosition(x=5))  # positional-only arguments 不能寫x=5
# # TypeError: incrementBy1ONlyPosition() got some positional-only arguments passed as keyword arguments: 'x'
# demo 60 ----------------------------
# def myAdd(x, y, /):
#     return x + y
#
# print(myAdd(3, 4))
# # print(myAdd(x=3, y=4)) TypeError: incrementBy1ONlyPosition() got some positional-only arguments passed as keyword arguments: 'x'
# def greeting(name, /, greeting="Hi"): # name positional-only arguments
#     return f"{greeting},{name}"
#
# print(greeting("Mark", "Hello"))
# print(greeting("Mark", greeting="Hello"))
# print(greeting("MarkHo"))
# print(greeting(name="Mark", greeting="Hello"))
# # TypeError: greeting() got some positional-only arguments passed as keyword arguments: 'name'

# demo 61 positional-only & ~keyword only~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# detail :positional-only ， size is keyword only
# def arrangeTitle(title, detail, /, padding="#", *, size=20, repeat=1):
#     return f"{title}[{detail}]".center(size, padding) * repeat
#
#
# print(arrangeTitle("hello", "world"))
# #print(arrangeTitle(title="hello", detail="world"))
# print(arrangeTitle("hello","world",'-'))
# print(arrangeTitle("hello","world",padding='-'))
# print(arrangeTitle("hello","world",padding='-',size=30))
# print(arrangeTitle("hello","world",padding='-',size=30,repeat=2))

# demo62 巢狀 function~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def outer(num1):
#     def inner_increment(x):
#         return x + 1
#
#     num2 = inner_increment(num1)
#     print(num1, num2)   # 100 101
#
# outer(100)
# #inner_increment(100)
# #outer.inner

# demo63: isinstance（object，type） 判断是否是一个已知的类型------------------------------------
# def factorial(number):
#     if not isinstance(number, int):   # 判断number 是 int type
#         raise TypeError("Oops, number should be a integer")
#     if not number >= 0:
#         raise ValueError("Sorry, number should be positive")
#
#     def inner_factorial(x):
#         if x <= 1:
#             return 1
#         return x * inner_factorial(x - 1)
#
#     return inner_factorial(number)
#
# try:
#   # print(factorial(5))
#   # print(factorial(3.5))
#   print(factorial("5"))
#   # print(factorial(-2))
# except TypeError as e:
#   print(e)
# except ValueError as e:
#     print(e)
# else:
#     pass
#
# for i in range(10):
#     print(factorial(i))
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def factorial(number):
#     if not isinstance(number, int):
#         raise TypeError("Oops, number should be a integer")
#     if not number >= 0:
#         raise ValueError("Sorry, number should be positive")
#
#     def inner_factorial(x):
#         if x <= 1:
#             return 1
#         return x * inner_factorial(x - 1)
#
#     return inner_factorial(number)
#
#
# try:
#     print(factorial(20))
#     print(factorial(3.5))
#     print(factorial("5"))
#     print(factorial(-2))
# except TypeError as e:
#    print(e)
# except ValueError as e:
#    print(e)
# else:
#    pass
#
# for i in range(10):
#     print(factorial(i))

# demo64 # ~ global: 存取外層變數~， if mutable(list,object) 不需要 global~~~~~~~~~~~~~~~~
# x = 'global'
# y = 5
# z = [5]   # 不需 global

# def foo():
#     print("[foo],x=", x)
#
# print("outside, x=", x)
#
# foo()
#
# def bar():
#     global y
#     global x
#     print('[bar]y=', y)
#     y *= 2
#     x *= 2
#     z[0] *= 2
#
#
# print("y=", y)  #y = 5
# print("z=", z)  # z= [5]
# bar()           # [bar]y= 5
# print("y=", y)  #y= 10
# print("x=", x)  # x= globalglobal
# print("z=", z)  # z= [10]

# nonlocal 找上層函數的變數 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# x = 5
# def foo():
#     x = 10
#     y = "local"
#     print("inside, y=", y, " ,x=", x)    # inside, y= local  ,x= 10
#
# print("[1],x=", x) #[1],x= 5  # function foo()的x 不影響 foo?()外部的 x
# foo()
# print("[1],x=", x) #[1],x= 5
#
# # print(y)
#
# def outer():
#     x = "local1"
#     def inner():
#         nonlocal x      # nonlocal 找上層函數的變數
#         x = "local2"
#         print("inner:x=", x)
#
#     print("[1]outer:", x)   # [1]outer: local1
#     inner()                 # inner:x= local2
#     print("[2]outer:", x)   # [2]outer: local2
# outer()

# demo66 ***lambda : 用lambda 取代function 比較簡單 ~~~~~~~~~~~~~~~~~~~~~~~~~~
# lambda 參數 : return
# import math
#
# def square_root(x):
#     return math.sqrt(x)   # math.sqrt 開根號
#
# def square_root2(x):
#     return math.sqrt(x)
#
# square_root3 = lambda x: math.sqrt(x)  # lambda 參數 : return : 取代function 比較簡單
#
# print(square_root(5))
# print(square_root2(5))
# print(square_root3(5), square_root3(6), square_root3(7))
# print(type(square_root3), type(square_root2), type(square_root))
# #<class 'function'> <class 'function'> <class 'function'>

# demo67 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def make_increment(n):
#     return lambda x: x + n
#
# f = make_increment(30)
#
# print(f(100), f(150))
# ------------------------------------------------------------------
# def make_tuple(p):
#     return lambda x: (x, 'p' * p)
#
# g1 = make_tuple(5)
# g2 = make_tuple(10)
# print(g1(3), g1(5), g2(3), g2(5))  # 3是 x , 5是 x , 3是 x, 5是 x
#-------------------------------------------------------------------
# pairs = [(4, 'cookie'), (1, 'banana'), (2, 'donut'), (3, 'apple')]
# pairs.sort(key=lambda t:t[0] )
# print(pairs)
# pairs.sort(key=lambda t:t[1])
# print(pairs)

# demo68 # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# class Counter(object):
#     def __init__(self):
#         print("object created")
#         pass
#     def __iter__(self):
#         print("prepare to iterate")
#         return self
#     def __next__(self):
#         #return 3
#         print("call next for next object")
#         raise StopIteration
#     pass
#
# c1 = Counter()
# for c in c1:
#     print(c)

# demo68' ----------------------------------------------
# class Counter(object):
#     def __init__(self, low, high):
#         # print("object created")
#         self.current = low
#         self.high = high
#         pass
#
#     def __iter__(self):             # 有迭代觸發 (for)
#         # print("prepare to iterate")
#         return self
#
#     def __next__(self):            # for loop next 觸發
#         # return 3
#         # print("call next for next object")
#         if self.current > self.high:
#             raise StopIteration        #迴圈結束時 stop error
#         else:
#             self.current += 1
#             return self.current - 1
#     pass
#
#
# # c1 = Counter(5, 15)
# # for c in c1:
# #     print(c)
# c2 = Counter(5, 15)
# print([c for c in c2])  # [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# print([c for c in c2])  # []
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# class Counter(object):
#     def __init__(self, low, high):
#         # print("object created")
#         self.current = low
#         self.high = high
#         pass
#
#     def __iter__(self):
#         # print("prepare to iterate")
#         return self
#
#     def __next__(self):
#         # return 3
#         # print("call next for next object")
#         if self.current > self.high:
#             raise StopIteration
#         else:
#             self.current += 1
#             return self.current - 1
#     pass
#
#
# c1 = Counter(5, 15)
# for c in c1:
#     print(c)
# c2 = Counter(5, 15)
# print([c for c in c2])
# print([c for c in c2])
#
# c3 = Counter(5,8)
# print(next(c3))
# print(next(c3))
# print(next(c3))
# print(next(c3))
#print(next(c3))

# # demo 70 : yield :直到下一次的遞迴，程式才會從 yield 的下一行開始執行~~~~~~~~~~~~~~
# yield 暫時看成 return，但是這個 return 的功能只有單次。而且，一旦我們的程式執行到 yield 後，程式就會把值丟出，並暫時停止。
# 直到下一次的遞迴，程式才會從 yield 的下一行開始執行。那哪裡有遞迴呢？沒錯，最常被用到 for 迴圈裡，而且 for 迴圈自帶 next() 的功能
# def infinite_generator(start=0):
#     while True:
#         yield start
#         start += 2
#
#
# for num in infinite_generator(5):
#     print(num, end=" ")　　　　　　　　　＃　5 7 9 11 13 15 17 19 21
#     if num > 20:
#         break

####################################################
# demo71 python function 傳入另一function----------------------------------------
# def my_oreo(func):
#     print("upper side chocolate cookie")
#     func()
#     print("lower side chocolate cookie")
#
#
# def add_filling():
#     print("butter_cream")
#
# my_oreo(add_filling)
# # print("------")
# # print("butter_cream")
# # my_oreo(None)
# # my_oreo(add_filling())
# demo 72 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def my_oreo(func):
#     print("upper side chocolate cookie")
#     func()
#     print("lower side chocolate cookie")
#
#
# def add_peanut_filling():
#     print("peanut butter!")
#
#
# def add_regular_filling():
#     print("butter cream!")
#
#
# fillings = [add_peanut_filling, add_regular_filling, add_peanut_filling]
# for filling in fillings:
#     print("---get a oreo:---")
#     my_oreo(filling)
#     print("----------------------------")

# demo73 ----------------------------------------
# def my_oreo(func):
#     print("upper side chocolate cookie")
#     func()
#     print("lower side chocolate cookie")
#
# # 程式(1) --------------------
# # def add_filling():
# #     print("butter_cream")
#
# # my_oreo(add_filling)
#
# # @my_oreo 等於程式(1)  -----------------
# @my_oreo
# def add_filling():
#     print("butter_cream")
#
# add_filling
# demo73' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def my_oreo(func):
#     def wrapper():
#         print("upper side chocolate cookie")
#         func()
#         print("lower side chocolate cookie")
#
#     return wrapper
#
#
# @my_oreo
# def add_filling():
#     print("butter_cream")
#
#
# add_filling()

# demo74' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def my_oreo(func):
#     def wrapper():
#         print("upper side chocolate cookie")
#         func()
#         print("lower side chocolate cookie")
#
#     return wrapper
#
#
# @my_oreo
# def add_peanut_filling():
#     print("peanut butter!")
#
#
# @my_oreo
# def add_regular_filling():
#     print("butter cream!")
#
#
# fillings = [add_peanut_filling, add_regular_filling, add_peanut_filling]
# for filling in fillings:
#     print("---get a oreo:---")
#     filling()
#     print()

# demo71_wrapper # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def my_oreo(func):
#     def wrapper():
#         print("upper side chocolate cookie")
#         func()
#         print("lower side chocolate cookie")
#
#     return wrapper
#
#
# def add_filling():
#     print("butter_cream")
#
#
# print(type(my_oreo(add_filling)))
# # way1, create a function variable
# my_oreo_function = my_oreo(add_filling)
# my_oreo_function()
# #way2
# my_oreo(add_filling)()

# demo72_wrapper # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def my_oreo(func):
#     def wrapper():
#         print("upper side chocolate cookie")
#         func()
#         print("lower side chocolate cookie")
#
#     return wrapper
#
#
# def add_peanut_filling():
#     print("peanut butter!")
#
#
# def add_regular_filling():
#     print("butter cream!")
#
# #
# fillings = [add_peanut_filling, add_regular_filling, add_peanut_filling]
# for filling in fillings:
#     print("---get a oreo:---")
#     # my_oreo(filling)()
#     m = my_oreo(filling)
#     m()
#     print()

# demo75 # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def my_oreo(func):
#     def wrapper(x):    # 傳值 x  = "vanilla_chocolate"-------
#         print("upper side chocolate cookie")
#         func(x)
#         print("lower side chocolate cookie")
#
#     return wrapper
#
# @my_oreo
# def add_filling(fill):
#     print(f"{fill}_cream")
#
#
# add_filling("vanilla_chocolate")

# demo76 *x 可以傳多個值~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def my_multi_layer_oreo(func):
#     def wrapper(*x):       #  *x 可以傳多個值
#         print("upper side chocolate cookie")
#         func(*x)
#         print("lower side chocolate cookie")
#
#     return wrapper
#
#
# @my_multi_layer_oreo
# def add_filling(*fills):
#     for fill in fills:
#         print(f"{fill}_cream")
#
#
# add_filling()
# print('----')
# add_filling("vanilla")
# print('---')
# add_filling('pineapple', 'apple', 'banana')

# demo77 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def my_oreo(func):
#     def wrapper(x):
#         print("upper side chocolate cookie")
#         print(f"middle side {func(x)}")
#         print("lower side chocolate cookie")
#
#     return wrapper
#
#
# @my_oreo
# def add_filling(fill):
#     return f"{fill}_cream"
#
#
# add_filling("vanilla")
# print('--------------------------')
# add_filling("chocolate")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# log in to
# https: // github.com /
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import functools
# def my_oreo(func):
#     @functools.wraps(func)
#     def wrapper():
#         print("upper side chocolate cookie")
#         func()
#         print("lower side chocolate cookie")
#
#     return wrapper
#
# @my_oreo
# def add_normal_filling():
#     print("butter_cream")
#
# @my_oreo
# def add_special_filling():
#     print("walnut_cream")
#
# print(repr(my_oreo))  #repr : function type & explanation
# # <function my_oreo at 0x000001C4C7641EE0>
# print(repr(print))
# print(repr(add_normal_filling))
# print(repr(add_special_filling))
# # add_normal_filling()
# # add_special_filling()

# demo79 # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def my_timer(func):
#     def wrapper_timer(*args, **kwargs):
#         print("start a timer")
#         value = func(*args, **kwargs)
#         print("function return, stop timer")
#         return value
#     return wrapper_timer
#
# @my_timer
# def spend_time_to_calculate(num_times):
#     result = 0
#     for _ in range(num_times):
#         result = sum([i ** 2 for i in range(10000)])
#     return result
#
# print("spend_time_to_calculate result=", spend_time_to_calculate(1))

# 使用裝飾函數來計數~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import time
#
#
# def my_timer(func):
#     def wrapper_timer(*args, **kwargs):  # *args 傳多個變數，**kwargs : (K1:V1,K2:V2...)
#         print("start a timer")
#         startTime = time.perf_counter()   #time.perf_counter: 啟動 timer
#         value = func(*args, **kwargs)
#         endTime = time.perf_counter()    # end time
#         runTime = endTime - startTime
#         print(f"{func.__name__} return, stop timer, total cost:{runTime:.4f}")
#         return value
#
#     return wrapper_timer
#
#
# @my_timer
# def spend_time_to_calculate(num_times):
#     result = 0
#     for _ in range(num_times):
#         result = sum([i ** 2 for i in range(20000)])
#     return result
#
#
# print("spend_time_to_calculate result=", spend_time_to_calculate(1000))

# 物件導向程式開發
# demo 80~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# class Layout:   # 定義類別
#     pass
# class Layout2(object):
#     pass
#
# l1 = Layout()
# l2 = Layout2()
# print(type(Layout), type(Layout2))   # <class 'type'> <class 'type'>
# print(type(l1), type(l2))            # instance 實例 <class '__main__.Layout'> <class '__main__.Layout2'>
# print(l1.__class__, l2.__class__)    # <class '__main__.Layout'> <class '__main__.Layout2'>

# demo81 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# class Layout(object):
#     def __init__(self, layers):
#         self.layers = layers
#
#
# l1 = Layout([1, 2, 3, 4])
# l2 = Layout([1, 3, 5, 7])
# print(l1.layers)
# print(l2.layers)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# class Layout(object):
#     vias = ['v1', 'v2', 'v3']
#
#     def __init__(self, layers):
#         self.layers = layers
#
#
# l1 = Layout([1, 2, 3, 4])
# l2 = Layout([1, 3, 5, 7])
# print(l1.layers)
# print(l2.layers)
# print(l1.vias, l2.vias, Layout.vias)
# print("process upgrade")
# Layout.vias.append("v4")
# print(l1.vias, l2.vias, Layout.vias) # ['v1', 'v2', 'v3', 'v4'] ['v1', 'v2', 'v3', 'v4'] ['v1', 'v2', 'v3', 'v4']
# l1.layers.append(5)
# l2.layers.append(9)
# print(l1.layers, l2.layers) # [1, 2, 3, 4, 5] [1, 3, 5, 7, 9]
# # Vendor，直译供应商，在软件中（比如 C, Go 等语言中），是一种把第三方库的代码直接内嵌到软件中的方式。
# # https://frostming.com/2022/03-12/how-to-vendor-in-python/
# l1.vendor = 'TSMC'
# print(l1.vendor, l1.layers)  # TSMC [1, 2, 3, 4, 5]
# l2.owner = 'ibm'
# print(l2.owner, l2.layers)   #ibm [1, 3, 5, 7, 9]

# demo 82 物件繼承 : ---------------------------------------
#(1)可以從副類別取得屬性和方法
#(2)子類別繼承父類別所有屬性和方法
# (3)子類別可以增加自己的行為

# class Employee:         #parent class
#     def __init__(self):               # 建構含式 ，物件建立時自動執行
#         self.work_content = "work"    #屬性 : work_content
#
#     def doWork(self):                 #方法 : doWork
#         print("working on: %s" % self.work_content)
#
#
# class RD(Employee):   # child class
#     pass
#
#
# class FAE(Employee):
#     pass
#
#
# class Scientist(Employee):
#     pass
#
#
# e1 = Employee()   # 建立class instance
# e2 = RD()
# e3 = FAE()
# e4 = Scientist()
# employees = [e1, e2, e3, e4]
# for e in employees:
#     e.doWork()
# # e1.doWork()
# # e2.doWork()
# # e3.doWork()
# # e4.doWork()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~------
# class Employee:
#     def __init__(self):
#         self.work_content = "work"
#
#     def doWork(self):
#         print("working on: %s" % self.work_content)
#
#
# class RD(Employee):
#     def __init__(self):
#         self.work_content = "Research and Development"
#
#
# class FAE(Employee):
#     def __init__(self):
#         self.work_content = "Work with clients"
#
#     pass
#
#
# class Scientist(Employee):
#     def __init__(self):
#         self.work_content = "do some research"
#
#     pass
#
#
# e1 = Employee()
# e2 = RD()
# e3 = FAE()
# e4 = Scientist()
# employees = [e1, 'hello world', e2, None, e3, 500, e4, 3.14]
# for e in employees:
#     if isinstance(e, Employee):   # *** isinstance
#         e.doWork()
#     else:
#         pass
# # e1.doWork()
# # e2.doWork()
# # e3.doWork()
# # e4.doWork()
# ----------------------------------
# class Employee:
#     def __init__(self):
#         self.work_content = "work"
#
#     def doWork(self):
#         print("working on: %s" % self.work_content)
#
#
# class RD(Employee):
#     def __init__(self):
#         self.work_content = "RD: Research and Development"
#     pass
#
# class FAE(Employee):
#     def __init__(self):
#         self.work_content = "FAE: Cooperate some Consultant"
#     pass
#
# class Scientist(Employee):
#     def __init__(self,drcret_mission):
#         self.work_content = drcret_mission
#     pass
#
# e1 = Employee()
# r1 = RD()
# f1 = FAE()
# s1 = Scientist("client deep learning") # child class overwrite parent class
#
# e1.doWork()  # working on: work
# r1.doWork()  # working on: RD: Research and Development (子類別先找，再找副類別)
# f1.doWork()  # working on: FAE: Cooperate some Consultant (子類別先找，再找副類別)
# s1.doWork()  # working on: client deep learning (子類別先找，再找副類別)

# demo83 make a directory logs~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 在python中__setitem__(self,value,key)方法时python魔法方法的一种，
# 这个方法会让类按照一定的方法存储和key映射的value。该值可以使用另一种魔法方法__getitem__(self,key)来获取。
# super().__init__會去呼叫父類別的initializer__init__
# new/Directory : logs
# import logging
#
# class LoggingDict(dict):
#     def __setitem__(self, key, value):   # set key & value
#         super().__setitem__(key, value)
#         logging.info(f"setting {value} to {key} position")
#         pass
#     pass
#
# logging.basicConfig(filename='logs/demo83.log', level=logging.INFO)
# l1 = LoggingDict()
# l1['ken'] = 'ios'
# l1['frank'] = 'oracle'
# print(l1)#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # **** make a directory logs
# import logging
#
#
# class LoggingDict(dict):
#     def __setitem__(self, key, value):
#         super().__setitem__(key, value)
#         logging.debug(f"setting {value} to {key} position")
#         logging.info(f"setting {value} to {key} position")
#         logging.warning(f"setting {value} to {key} position")
#         logging.error(f"setting {value} to {key} position")
#         logging.critical(f"setting {value} to {key} position")
#
#         pass
#
#     pass
#
#
# logging.basicConfig(filename='logs/demo83.log', level=logging.WARNING)
# l1 = LoggingDict()
# l1['ken'] = 'ios'
# l1['frank'] = 'oracle'
# print(l1)

# demo84 # *** UserList~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 1. UserList模擬 list ，可經由data 物件存取，預設是一個空白list
# 2. list 可以是任何可迭代的資料類型
# from collections import UserList
#
# class MyOwnList(UserList):
#
#     def __setitem__(self, key, value):
#         if key == len(self.data):
#             self.data.append(value)
#         else:
#             self.data[key] = value
#             pass
#         pass
#
#     def square(self):
#         for i in range(0, len(self.data)):
#             self.data[i] = self.data[i] ** 2
#
#
# l1 = MyOwnList()
# for p in range(10):
#     l1[p] = 2 * p + 1
# print(l1)     # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# l1.square()
# print(l1)     # [1, 9, 25, 49, 81, 121, 169, 225, 289, 361]

# ***demo85 #UserDict~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# from collections import UserDict
#
# class MyOwnDict(UserDict):
#     def __init__(self, data={}, **kwargs):  #data={} 初始化
#         super().__init__()
#         self.update(data)
#         self.update(kwargs)
#
#     def __add__(self, other):
#         self.data.update(other)
#         return self
#
#
# # a = {'k1': 'v1'}
# # b = {'k2': 'v2'}
# # print(a + b)
#
# a = MyOwnDict(a=1)
# b = MyOwnDict(b=2)
# c = MyOwnDict(c=3)
# d = MyOwnDict(d={'A': 777})
# print(a, b, c, d)  # {'a': 1} {'b': 2} {'c': 3} {'d': {'A': 777}}
# print(a + b)       # {'a': 1, 'b': 2}
# print(a + b + c)   # {'a': 1, 'b': 2, 'c': 3}
# print(a + b + c + d)  # {'a': 1, 'b': 2, 'c': 3, 'd': {'A': 777}}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# from collections import UserDict
#
# class MyOwnDict(UserDict):
#     def __init__(self, data={}, **kwargs):
#         super().__init__()
#         self.update(data)
#         self.update(kwargs)
#         print("--------------------")
#         print(data)
#         print(kwargs)
#
#     def __add__(self, other):
#         self.data.update(other)
#         return self
#
#
# # a = {'k1': 'v1'}
# # b = {'k2': 'v2'}
# # print(a + b)
#
# a = MyOwnDict(data={'a': 1, 'A': 100})  #傳給 data {'a': 1, 'A': 100}
# b = MyOwnDict(b=2, B=200)               # 傳給  **kwargs  {'b': 2, 'B': 200}
# c = MyOwnDict(c=3, C='cookie')          # 傳給  **kwargs  {'c': 3, 'C': 'cookie'}
# d = MyOwnDict(d={'A': 777})             # 傳給  **kwargs  {'d': {'A': 777}}
# print(a, b, c, d)
# print(a + b)       # {'a': 1, 'A': 100, 'b': 2, 'B': 200}
# print(a + b + c)   # {'a': 1, 'A': 100, 'b': 2, 'B': 200, 'c': 3, 'C': 'cookie'}
# print(a + b + c + d) # 'a': 1, 'A': 100, 'b': 2, 'B': 200, 'c': 3, 'C': 'cookie', 'd': {'A': 777}}

# ps:----------------------------------
# class Test():
#     def __init__(self):
#             pass
#     def __repr__(self):
#             return "the repr"
#     def __str__(self):
#             return "the str"
#
# a = Test()
#
# print(a)
# print(str(a))
# print(repr(a))
# demo 86 把類別物件加入set~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 1. __eq__ : objA == objB 判定兩個物件是否相等
# 2. 需要__hash__ 函數，被 hash()呼叫 hash 回傳整數
# 3. __eq__，__hash__  兩個要一起使用: 如果相等就不要寫入set1
# class Course:
#     def __init__(self, name, instructor, duration):
#         self.name = name
#         self.instructor=instructor
#         self.duration=duration
#     def __eq__(self, other):
#         return self.name == other.name
#         AND
#         self.instructor == other.instructor
#         AND
#         self.duration == other.duration
#     def __hash__(self):
#         return hash((self.name, self.instructor, self.duration ))
#     def __repr__(self):
#         return '<repr: course {},{},{}>'.format(self.name,self.instructor,self.duration)
#     def __str__(self):
#         return '<str:course {},{},{}>'.format(self.name, self.instructor, self.duration)
# c1 = Course('BDPY', 'Mark', '35')
# c2 = Course('PYOO', 'Mark', '35')
# c3 = Course('BDPY', 'Mark', '35')
# c4 = Course('PYKT', 'Mark', '35')
# #print(repr(c1))
# print(c1,c3)
# print(c2)
# set1 = set()
# set1.add(c1)
# set1.add(c2)
# set1.add(c3)
# set1.add(c4)
# print(set1)

# demo 87----------------------------------------------------------
# from abc import ABC, abstractmethod
#
# class A1(ABC):
#     def __init__(self, value):
#         super().__init__()
#         self.value = value
#
#     @abstractmethod  # 抽象型別必須由子類別實作(創建物件)
#     def do_something(self):
#         #pass
#         print('a1_do_something')

# class B1(A1):
#     # pass
#     def do_something(self):
#         print("hello, I will really do something, and my value=", self.value)

# instance1 = B1(-5)
# instance1.do_something()  # hello, I will really do something, and my value= -5
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# from abc import ABC, abstractmethod
#
# class Foo(ABC):
#     @abstractmethod
#     def fun(self):
#         print("please Implemente in subclass")
#         #'''please Implemente in subclass'''
#
#
# class SubFoo(Foo):
#     def fun(self):
#         print('fun in SubFoo')
#
# a = SubFoo()
# a.fun()
#--------------------------------------------
# class UCOM(object):
#     def __str__(self):
#         return "ucom in taipei"
#
#     def __repr__(self):
#         return "[Taipei]UCOM[Nanging-Fuxing]"
# u1 = UCOM()
# print(u1)
# print(repr(u1))
#
# # README.md
# # POOP course 22-Oct-2019
# ## Last modified 22-Oct-2019#

# # demo 88 metaclass 後設類別 --------------------------------------------
# 1.metaclass 生成出來的類別就是 class
# 2.一般類別定義實例，後設類別定義類別的行為
# 3.後設類別 用在 (1)log & 效能 (2)檢視介面 (3)在類別初期檢視生成實例 (4)自動屬性合成
# 4.後設類別 繼承type的類別
# 5.沒有meta 的類別會呼叫 type() 的 __call__
# 6.有mataclass 的就會呼叫 new
# class SimpleMeta(type):
#     def __new__(cls, className, superClass, attributeDict):   #生成時呼叫
#         print("class name:", className)
#         print("super class name:", superClass)
#         print("attribute:", attributeDict)
#         return type.__new__(cls, className, superClass, attributeDict)
#     pass
#
# class S:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# class A(S, metaclass=SimpleMeta):     #A 定義時 呼叫 new
#      pass
# print(" 1 一般類別: type , 後設類別繼承-----")
# print(type(SimpleMeta), type(S), type(A))  # <class 'type'> <class 'type'> <class '__main__.SimpleMeta'>
# print(" 2----------------------------")
# s1 = S('James', 38)
# print(f' type(s1)={type(s1)}')
# print(s1)
# print(" 3----------------------------")
# a1 = A('Mark', 43)
# print(type(a1), a1.name, a1.age)

# ps: -------------------------------------------
# class MyInt(int):
#     def __add__(self, other):
#         print("specializing addition")
#         return super(MyInt, self).__add__(other)
#
# i = MyInt(2)
# # print(i)
# print(i+5)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ps:enumerate
# print(list(enumerate("abc")))  # enumerate 同時輸出索引與元素 (index,value) is tuple type
# List = ['a', 'b', 'c', 'd', 'e']
#
# for value in enumerate(List):
#     print(value)
#
# for index, value in enumerate(List):
#     print(index, value)

#------------------------------------------------
# class SimpleMeta(type):
#     def __new__(cls, className, superClass, attributeDict):
#         print("1.創建類別時呼叫的")
#         print("class name:", className)
#         print("super class name:", superClass)
#         print("attribute:", attributeDict)
#         return type.__new__(cls, className, superClass, attributeDict)
#
#     def __call__(self, *args, **kwargs):
#         print("2.創建物件時呼叫的")
#         for arg in args:
#             print(f'創建時有一個引數{arg}')
#         return super().__call__(*args, **kwargs)
#
#     pass
#
#
# class S:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# print(" 1----------------------------")
# print("now create class A")
# class A(S, metaclass=SimpleMeta): # 創建 metaclass 類別，呼叫 new
#     pass
#
# print(" 2----------------------------")
# print(type(SimpleMeta), type(S), type(A))
#
# print(" 3----------------------------")
# s1 = S('James', 38)
# print(type(s1), s1.name, s1.age)
#
# print(" 4----------------------------")
# a1 = A('Mark', 43)               # 實作 呼叫__call__
# print(type(a1), a1.name, a1.age)

# demo 90~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# class SimpleMeta(type):
#     def __new__(cls, className, superClass, attributeDict):
#         print("創建類別時呼叫的")
#         print("class name:", className)
#         print("super class name:", superClass)
#         print("attribute:", attributeDict)
#         return type.__new__(cls, className, superClass, attributeDict)
#
#     def __call__(self, *args, **kwargs):
#         print("創建物件時呼叫的")
#         for arg in args:
#             print(f'創建時有一個引數{arg}')
#         return super().__call__(*args, **kwargs)
#     pass
#
#
# class S:
#     def __init__(self, name, age):
#         print("init in S")
#         self.name = name
#         self.age = age
#
#
# print("now create class A----------------")
# class A(S, metaclass=SimpleMeta):
#     def __init__(self, name, age):
#         print("init in A")
#         super().__init__(name, age)  # 呼叫父class  __init__
#         print("customize in A")
#
# print("---------- 1-type(SimpleMeta), type(S), type(A)--------")
# print(type(SimpleMeta), type(S), type(A))
#
# print("---------- type(s1) -----------------------------------")
# s1 = S('James', 38)
# print(type(s1), s1.name, s1.age)
#
# print("-------------現在生成物件a1------------------------------")
# a1 = A('Mark', 43)
# print(type(a1), a1.name, a1.age)
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#--------------------------------------------------------------------
# class MetaSingleton(type):
#     _instances = {}
#
#     def __call__(self, *args, **kwargs):
#         if self not in self._instances:
#             print("really, create an instance")
#             self._instances[self] = super().__call__(*args, **kwargs)
#         return self._instances[self]
#
#
# class SingletonATM(object, metaclass=MetaSingleton):
#     def __init__(self):
#         print("create a atm")
#
#
# class RegularClass(object):
#     pass
#
#
# r1 = RegularClass()
# r2 = RegularClass()
# print(hex(id(r1)), hex(id(r2)))     # 0x216e586b580 0x216e586b5e0 不一樣
# print("create atm1")
# atm1 = SingletonATM()     # 呼叫 __call__  再呼叫 __init__ ， 最後 super __init__
# print("create atm2")
# atm2 = SingletonATM()
# print(hex(id(atm1)), hex(id(atm2)))  # 0x216e586b7f0 0x216e586b7f0 一樣 (__new__ : id 一樣)
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# class MetaSingleton(type):
#     _instances = {}
#
#     def __call__(self, *args, **kwargs):
#         if self not in self._instances:
#             print("really, create an instance")
#             self._instances[self] = super().__call__(*args, **kwargs)
#         return self._instances[self]
#
#
# class SingletonATM(object, metaclass=MetaSingleton):
#     def __init__(self):
#         print("create a atm")
#
#
# class SingletonTicket(object, metaclass=MetaSingleton):
#     def __init__(self):
#         print("create a ticket machine")
#
#
# class RegularClass(object):
#     pass
#
#
# r1 = RegularClass()
# r2 = RegularClass()
# print(hex(id(r1)), hex(id(r2)))    # 0x1cde0d2b580 0x1cde0d2b5e0 id 不一樣
# print("1 -------------------------------")
# print("create atm1")
# atm1 = SingletonATM()
# print(" 2.-------------------------------")
# print("create atm2")
# atm2 = SingletonATM()
# print(hex(id(atm1)), hex(id(atm2)))  # 0x1cde0d2b880 0x1cde0d2b880 id 是一樣的 (__new__ : id 一樣)
# print(" 3. -------------------------------")
# t1 = SingletonTicket()
# t2 = SingletonTicket()
# print(hex(id(t1)), hex(id(t2)))  # 0x1cde0d2b4c0 0x1cde0d2b4c0 : id 是一樣的
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# class SingletonParent(object):
#     _instance = None
#
#     def __init__(self):
#         print("init is called")
#
#     # def __new__(cls, *args, **kwargs):
#     #     if not cls._instance:
#     #         print("new a instance")
#     #         cls._instance = object.__new__(cls, *args, **kwargs)
#     #     return cls._instance
#
#
# class RegularClass():
#     pass
#
#
# class SingletonClass(SingletonParent):
#     pass
#
#
# r1 = RegularClass()
# r2 = RegularClass()
# print(hex(id(r1)), hex(id(r2)), r1 is r2)  # 0x22e06a6b580 0x22e06a6b5e0 False
# s1 = SingletonClass()  # 產生第一次 : __new__ 再__init__
# s2 = SingletonClass()  # __init_
# print(hex(id(s1)), hex(id(s2)), s1 is s2) # 0x22e06a6b7f0 0x22e06a6b7f0 True (有__new__ id 才一樣)
# # /data/Python_Introduction ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Python（英國發音： / ˈpaɪθən / 美國發音： / ˈpaɪθɑːn /）是一種廣泛使用的直譯式、
# 進階程式、通用型程式語言。Python支援多種程式範式，包括物件導向、結構化、指令式、函數式和反射式程式。它擁有動態型別系統和垃圾回收功能，能夠自動管理記憶體使用，並且其本身擁有一個巨大而廣泛的標準庫。
#
# Python由吉多·范羅蘇姆創造，第一版釋出於1991年，它是ABC語言的後繼者，
# 也可以視之為一種使用傳統中綴表達式的LISP方言[6]。
#
# Python的設計哲學強調代碼的可讀性和簡潔的語法，尤其是使用空格縮排劃分代碼塊。
# 相比於C或Java，Python讓開發者能夠用更少的代碼表達想法。不管是小型還是大型程式，該語言都試圖讓程式的結構清晰明瞭。
#
# Python
# 直譯器本身幾乎可以在所有的作業系統中執行。
# Python的其中一個直譯器CPython是用C語言編寫的、是一個由社群驅動的自由軟體，目前由Python軟體基金會管理。
#
# Python（パイソン）はインタープリタ型の高水準汎用プログラミング言語である。グイド・ヴァン・ロッサムにより創り出され、1991
# 年に最初にリリースされたPythonの設計哲学は、その顕著なホワイトスペースの使用によってコードの可読性が重視されている。その言語構成とオブジェクト指向のアプローチは、プログラマが小規模なプロジェクトから大規模なプロジェクトまで、明確で論理的なコードを書くのを支援することを目的としている。


# 檔案的處理 : 1 文字檔 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# demo91 open() 開啟黨俺
# file1 = open('data/Python_Introduction', encoding='UTF-8')
# print(type(file1))         # <class '_io.TextIOWrapper'>
# readme_txt = file1.read()  #readme_txt is string
# file1.close()
# print(type(readme_txt), len(readme_txt), readme_txt[:50])   # [:50] 前 50 個字
# # <class 'str'> 642 Python（英國發音： / ˈpaɪθən / 美國發音： / ˈpaɪθɑːn /）是一種廣泛使
#
# # 下列方法比較好 -------------------------------------------------
# with open('data/Python_Introduction', encoding='UTF-8') as file2:
#     readme_txt = file2.read()
#     print(type(readme_txt), len(readme_txt), readme_txt[:50])
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# file1 = open('data/Python_Introduction', encoding='UTF-8')
# print(type(file1))
# readme_txt = file1.read()
# file1.close()
# print(type(readme_txt), len(readme_txt), readme_txt[:50])
#
# file3 = open('data/clone1', 'w', encoding='UTF-8')
# file3.write(readme_txt)
# file3.close()
#
# with open('data/Python_Introduction', encoding='UTF-8') as file2:
#     readme_txt2 = file2.read()
#     print(type(readme_txt2), len(readme_txt2), readme_txt2[:50])
#
# print(readme_txt2)
#
# with open('data/clone2', 'w', encoding='UTF8') as file4:
#     file4.write(readme_txt2)

#
# PS 補充1  : 物件導向 ----------------------------- ------------------------
# class C1(object):
#     ''' mika test'''       # class 的說明文件
#     x=58
#
# print(f'C1.x = {C1.x}')
#
# class C2(C1):
#     pass
# C2.x =54
# print(f'C2.x = {C2.x}')
#
# C2.y = 38             # 屬性可以加入
# print(f'C2.y = {C2.y}')
#
# print(f'C1.__name__ = {C1.__name__}')  # C1
# print(f'C2.__base__ = {C2.__base__}')  # <class '__main__.C1'> : 上一層 class
# # class 類別主體中的第一個字串，會當作是class 的說明文件
# print(f'C1.__doc__ = {C1.__doc__}') # mika test

# 補充2 --------------------------------------------------------------------
# class Const(object):
#    def __init__(self, value):
#        self.value = value
#
#    def __set__(self, *_):
#        print('set-----')
#        self.value =50
#
#    def __get__(self, *_):
#        print('get-----')
#        return self.value
#
# class X(object):
#     c = Const(23)
#
# x = X()
# print(x.c)   #  23 執行 __get__
# x.c = 42     # 無法設值
# print(x.c)
# # x.set(20)
# -----------------------------------
# class Student(object):
#     def __int(self, age=0):
#         self._age = age
#
#     # getter方法
#     def get(self):
#         print('get-------')
#         return self._age
#
#
#     # setter方法
#     def set(self, value):
#         print('set-------')
#         self._age = value
#
# xiaoming = Student()
# # 使用setter方法设置age
# xiaoming.set(20)      # run set(self, value)
# # 使用getter方法返回age
# print(xiaoming.get()) # run def get(self):
# print(xiaoming._age)


# Day 5 -------------------------------
# demo92-------------------------------
# myOutputfile = open('data/demo92.txt', 'w')
# linesToWrite = ["POOP\n", "BDPY\n", "PYKT\n", "...\n", "AIOCV\n"]
# myOutputfile.writelines(linesToWrite)
# myOutputfile.close()
#
# for i in range(0, 10):
#     myOutputfile2 = open('data/demo92.txt', 'a', encoding='UTF-8')
#     nextLine = ["加入一些在最後面\n"]
#     myOutputfile2.writelines(nextLine)
#     myOutputfile2.close()

# demo93 使用 glob 處理目錄: glob.glob----------------------------------
# import os
# from glob import glob
#
# #paths = "c:\\windows"
# paths = "c:/windows"
# print(type(paths))                # <class 'str'>
# allDlls = os.path.join(paths, "*/*.dll")   # <class 'str'> c:/windows\*/*.dll
#
# print(len(allDlls))   # 18
#
# print(type(allDlls), allDlls)
#
# for dll in glob(allDlls):   # get c:\\windows 所有 dll 路徑(含子目錄下) : ex: c:/windows\apppatch\AcRes.dll
#     print(dll)
#
# allExes = os.path.join(paths, "*/*.exe") # get 所有 exe 路徑 : ex:
# for exe in glob(allExes):
#     print(exe)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import os
# import glob
#
# # paths = "c:\\windows"
# paths = "c:/windows"
# print(type(paths))
# allDlls = os.path.join(paths, "**/*.dll")
# print(len(allDlls))  # 19
# print(type(allDlls), allDlls)
# for dll in glob.glob(allDlls):
#     print(dll)
#
# allExes = os.path.join(paths, "*/*.exe")
# for exe in glob.glob(allExes):
#     print(exe)

# files = os.path.join(paths,"*/amd*.*")
# for f in glob.glob(files):
#     print(f)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import os
# import glob
#
# # paths = "c:\\windows"
# paths = "c:/windows"
# print(type(paths))
# allDlls = os.path.join(paths, "**/*.dll")
# print(len(allDlls))
# print(type(allDlls), allDlls)
# for dll in glob.glob(allDlls):
#     print(dll)
#
# allExes = os.path.join(paths, "*/*.exe")
# for exe in glob.glob(allExes):
#     print(exe)
#
# files = os.path.join(paths,"*/amd*.*")
# for f in glob.glob(files):
#     print(f)
#
# files2 = os.path.join(paths,"*/[abc]*.*")
# for f in glob.glob(files2):
#     print(f)
#
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import glob
# import os
#
# paths = 'c:\\windows'
# paths2 = 'c:/windows'
# allDlls = os.path.join(paths, '*/*.dll')
# allDlls2 = os.path.join(paths, '**/*.dll')
# allDlls3 = os.path.join(paths2, '*/*.dll')
# print(allDlls)
# print(allDlls2)
# print(allDlls3)
# d1 = [d for d in glob.glob(allDlls)]
# d2 = [d for d in glob.glob(allDlls2)]
# d3 = [d for d in glob.glob(allDlls3)]
# print(len(d1))
# print(len(d2))
# print(len(d3))
# print(d1 == d2)
# print(d1 == d3)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import glob
# import os
#
# paths = 'c:\\windows'
# paths2 = 'c:/windows'
# # allDlls = os.path.join(paths, '*/*.dll')
# # allDlls2 = os.path.join(paths, '**/*.dll')
# # allDlls3 = os.path.join(paths2, '*/*.dll')
# allDlls = os.path.join(paths, '*.dll')
# allDlls2 = os.path.join(paths, '*.dll')
# allDlls3 = os.path.join(paths2, '*.dll')
#
# print(allDlls)
# print(allDlls3)
# d1 = [d for d in glob.glob(allDlls)]
# d2 = [d for d in glob.glob(allDlls2)]
# d3 = [d for d in glob.glob(allDlls3)]
# print(len(d1))
# print(len(d2))
# print(len(d3))
# print(d1 == d2)
# print(d1 == d3)
# print(d1[:5])
# print(d2[:5])
# print(d3[:5])
#
# demo94 os.walk~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import os
# from pprint import pprint
#
# myPath = "c:/windows/system32"
#
# for currentFolder, subFolders, fileNames in os.walk(myPath):
#     print('---- currentFolder ------------')
#     print(currentFolder)           # c:/windows/system32 下的所有目錄，含c:/windows/system32
#     print('---- subFolders ------------')
#     pprint(subFolders)             # currentFolder的次目錄 :
#     print('---- fileNames ------------')
#     for f in fileNames:            # c:/windows/system32 下的所有檔案
#         pprint(f"...{f}")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# https://en.wikipedia.org/wiki/List_of_file_signatures
# #
# images = ['./data/image1.jpg', './data/image2.jpg']
#
# for image in images:
#     print(image)
#     with open(image, "rb") as imageFile:
#         index = 1
#         byte = imageFile.read(1)
#         while byte != "" and index < 9:
#             print(byte)
#             x = int.from_bytes(byte, byteorder='little')   # 把bytes类型的变量x，转化为十进制整数
#             print("[%d]%s,%s" % (index, str(hex(x)),str(x)))
#             byte = imageFile.read(1)
#             index += 1
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# images = ['./data/image1.jpg', './data/image2.jpg']
#
# for image in images:
#     print(image)
#     with open(image, "rb") as imageFile:
#         index = 1
#         while (byte := imageFile.read(1)) != "" and index < 9:
#             x = int.from_bytes(byte, byteorder='little')
#             print("[%d]%s" % (index, str(hex(x))))
#             index += 1
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# images = ['./data/image1.jpg', './data/image2.jpg', './data/image3.png',
#           './data/compress1.rar','./data/compress2.rar']
#
# for image in images:
#     print(image)
#     with open(image, "rb") as imageFile:
#         index = 1
#         while (byte := imageFile.read(1)) != "" and index < 9:
#             x = int.from_bytes(byte, byteorder='little')
#             print("[%d]%s" % (index, str(hex(x))))
#             index += 1

# demo 97 二進問黨但讀寫  struc~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#sample :
# import struct
#
# # native byteorder
# buffer = struct.pack("ihb", 1, 2, 3)
# # b'\x01\x00\x00\x00\x02\x00\x03' : "i" integer(4 bytes), h: short(2 bytes) b:signedchar(1 bytes)
# print(buffer)
# print(repr(buffer))
# print("unpack--------------")
# print(struct.unpack("ihb", buffer))
#
# data = [1, 2, 3]
# buffer = struct.pack("!ihb", *data) # b'\x00\x00\x00\x01\x00\x02\x03'  ("!ihb" : \x00 放前面)
# print(repr(buffer))
# print(struct.unpack("!ihb", buffer))
# ---------------------------------------------------------
# import struct
#
# output_file1 = open("data/myfile.bin", "wb")
# output_file2 = open("data/my_file.ascii", "w")
#
# for i in range(0, 100):
#     print("i=%d, pack=%s" % (i, repr(struct.pack('i', i))))
#     output_file1.write(struct.pack('i', i))
#     output_file2.write("%s\n" % str(i))
# output_file1.close()
# output_file2.close()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import struct
#
# output_file1 = open("data/myfile.bin", "wb")
# output_file2 = open("data/my_file.ascii", "w")
#
# for i in range(0, 100):
#     print("i=%d, pack=%s" % (i, repr(struct.pack('i', i)))) # struct.pack 的format string "i" is int
#     output_file1.write(struct.pack('i', i))
#     output_file2.write("%s\n" % str(i))
# output_file1.close()
# output_file2.close()
#
#
# input_file1 = open("data/myfile.bin", "rb")
# data = input_file1.read(400)
#
# str2 = ""
# str1 = ""
# count1 = 0
#
# for ch in data :
#     if ((count1 % 4) == 0) :
#        print(ch)
#        str2 += hex(ch) + " "
#        str1 += str(ch) + ", "
#     count1 = count1 + 1
#
# print(str2)
# print(str1)
#
# input_file1.close()
# #
# https://www.reddit.com/.rss
#
# jupyter-notebook
#
# demo98 使用 XML : urllib 從遠方取得訊息 parse(): 來創建樹狀結構
# demo98 : used Jupter Notebook-------------------------------
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import urllib.request
# import xml.dom.minidom
# URL = 'https://www.reddit.com/.rss'
# file1 = urllib.request.urlopen(URL)
# DOMTree = xml.dom.minidom.parse(file1)
# file1.close()
#
# DOMTree
#
# file1
#
#
# https://chrome.google.com/webstore/detail/view-xml/geikflidhgdlfgmfoheimkibmodlipeh?hl=zh-TW
#
#
# collection = DOMTree.documentElement
# if collection.hasAttribute("xmlns"):
#     print("xmlns value=%s"%collection.getAttribute("xmlns"))
# used Jupter Notebook~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# collection = DOMTree.documentElement
# if collection.hasAttribute("xmlns"):
#     print("xmlns value=%s, xmlns:media value=%s"%(collection.getAttribute("xmlns"),collection.getAttribute("xmlns:media")))
#
#
# entries = collection.getElementsByTagName("entry")
# for entry in entries:
#     print("id=",entry.getElementsByTagName('id')[0].childNodes[0].data)
#
# used Jupter Notebook~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# entries = collection.getElementsByTagName("entry")
# for entry in entries:
#     print("~~~~~~~~~~~~~~~~~~~~~")
#     print("id=",entry.getElementsByTagName('id')[0].childNodes[0].data)
#     print("title=",entry.getElementsByTagName('title')[0].childNodes[0].data)
#     print("last updated=",entry.getElementsByTagName('updated')[0].childNodes[0].data)
#     authors = entry.getElementsByTagName("author")
#     for author in authors:
#         print("*** get an author***")
#         print("author name=%s"%author.getElementsByTagName('name')[0].childNodes[0].data)
#         print("author uri=%s"%author.getElementsByTagName('uri')[0].childNodes[0].data)
#     print()
# used Jupter Notebook~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# entries = collection.getElementsByTagName("entry")
# for entry in entries:
#     print("~~~~~~~~~~~~~~~~~~~~~")
#     print("link=", entry.getElementsByTagName("link")[0].getAttribute("href"))
#     print("id=",entry.getElementsByTagName('id')[0].childNodes[0].data)
#     print("title=",entry.getElementsByTagName('title')[0].childNodes[0].data)
#     print("last updated=",entry.getElementsByTagName('updated')[0].childNodes[0].data)
#     authors = entry.getElementsByTagName("author")
#     for author in authors:
#         print("*** get an author***")
#         print("author name=%s"%author.getElementsByTagName('name')[0].childNodes[0].data)
#         print("author uri=%s"%author.getElementsByTagName('uri')[0].childNodes[0].data)
#     print("content=",entry.getElementsByTagName('content')[0].childNodes[0].data)
#     print()
#

## 12 偵錯與測試  ##
# from calculator import Calculator
# from calculator.Calculator import calculate
# if __name__ == '__main__':
#     calc = Calculator()
#     result = calc.calculate("1+1+3+23-1")
#     print(result)
# (1) unit Test
# Sample: -------------------
# import unittest
# import calculator
#
# class CalculatorTestCase(unittest.TestCase):
#     def setUp(self):
#         self.args = (3, 2)
#         print("setUp-----------------------")
#
#     def tearDown(self):
#         self.args = None
#         print("tearDown-----------------------")
#
#     def test_plus(self):
#         expected = 5
#         result = calculator.plus(*self.args)
#         self.assertEqual(expected, result)
#         print(f"result ={result}--------------")
#
#     def test_minus(self):
#         expected = 1
#         result = calculator.minus(*self.args)
#         self.assertEqual(expected, result)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import unittest
#
# def addBy1(x):
#     return x + 1
#
# # unittest 模組提供了一個基礎類別 TestCase，你可以繼承它來建立新的測試案例
# class MyTest(unittest.TestCase):
#     def test(self):
#         print("test running...")
#         self.assertEqual(addBy1(3), 4)
#
#     def test2(self):
#         print("test2 running...")
#         self.assertEqual(addBy1(-1), 0)
#
#     def test3(self):
#         print("test3 running...")
#         self.assertEqual(addBy1(1), 2)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import unittest
#
#
# def addBy1(x):
#     return x + 1
#
#
# class MyTest(unittest.TestCase):
#     def setUp(self) -> None:
#         print("prepare something")
#         pass
#     def tearDown(self) -> None:
#         print("store and clean up")
#         pass
#     def test1(self):
#         print("test1 running...")
#         self.assertEqual(addBy1(0), 1)
#
#     def test2(self):
#         print("test2 running...")
#         self.assertEqual(addBy1(-1), 0)
#
#     def test3(self):
#         print("test3 running...")
#         self.assertEqual(addBy1(1), 2)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import unittest
#
# def addBy1(x):
#     return x + 1
#
# class MyTest(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls) -> None:     #
#         print("1.one term setup")
#     @classmethod
#     def tearDownClass(cls) -> None:
#         print("2.whole clean up")
#
#     def setUp(self):
#         print("3.prepare something")
#         pass
#
#     def tearDown(self):
#         print("4.store and clean up")
#         pass
#
#     def test1(self):
#         print("5.test1 running...")
#         self.assertEqual(addBy1(0), 1)
#
#     def test2(self):
#         print("6.test2 running...")
#         self.assertEqual(addBy1(-1), 0)
#
#     def test3(self):
#         print("7.test3 running...")
#         self.assertEqual(addBy1(1), 2)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import unittest
#
# def addBy1(x):
#     return x + 1
#
# class MyTest(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls) -> None:
#         print("one term setup")
#     @classmethod
#     def tearDownClass(cls) -> None:
#         print("whole clean up")
#
#     def setUp(self):
#         print("prepare something")
#         pass
#
#     def tearDown(self):
#         print("store and clean up")
#         pass
#
#     def test1(self):
#         print("test1 running...")
#         self.assertEqual(addBy1(0), 1)
#
#     def test2(self):
#         print("test2 running...")
#         self.assertEqual(addBy1(-1), 0)
#
#     @unittest.skip("will do it in later release")
#     def test3(self):
#         print("test3 running...")
#         self.assertEqual(addBy1(1), 2)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# python -m unittest demo99.py
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import unittest
#
# def addBy1(x):
#     return x + 1
#
# class MyTest(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls) -> None:   # 建立類別之前執行
#         print("1.one term setup")  # 第1執行
#
#     @classmethod
#     def tearDownClass(cls) -> None: # 結束之後執行
#         print("2.whole clean up")   #  # 第5執行
#
#     def setUp(self):    # 測試之前執行
#         print("3.prepare something")  # 第2執行
#         pass
#
#     def tearDown(self):  # 測試之後執行
#         print("4.store and clean up")  # # 第4執行
#         pass
#     #
#     def test1(self):
#         print("5.test1 running...")   # # 第3執行
#         self.assertEqual(addBy1(0), 1)   # 比較 addBy1(0) & 1 是否相等 ， 相等 is True
#
#     def test2(self):
#         print("6.test2 running...")
#         self.assertEqual(addBy1(-1), 1)
#
#     @unittest.skip("7.will do it in later release")
#     def test3(self):
#         print("test3 running...")
#         self.assertEqual(addBy1(1), 2)
#
# if __name__ == '__main__':
#     unittest.main()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# (2) doc test
# demo100--Run in CMD (if has : if __name__ == '__main__':)--
# write in doctest.py & Run : python -m doctest -v doctest1.py---------------------------------
# import doctest1
#
# def square(x):
#     """Return the square of x
#
#     >>> square(2)
#     4
#     >>> square(-2)
#     4
#     """
#     # :param x:
#     # :return:
#
#     return x * x

# if __name__ == '__main__':
#     doctest.testmod()

# demo101 偵錯--: 設中斷點，按 Debug(Shift+F9)， F8: step over， F7: step 進入涵式內-------------------------------
#
# def getDigit(x):
#     returnDigit = 0
#     while x > 0:
#         # x = x / 10
#         x = x // 10
#         returnDigit += 1
#     return returnDigit
#
#
# print(getDigit(100))
# print(getDigit(1000))
# print(getDigit(10000))
# print(getDigit(65536))
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 13. 程序和執行緒 : Process and Thread ----------------------
# (1) 程序 Process : 使用  multiprocessing 套件，主程式中呼叫許多子程序
# demo 102 Run in CMD------------------------------------------------------
# import multiprocessing
#
# def worker():
#     print("worker is working...")
#
# if __name__ == '__main__':
#     jobs = []
#     for i in range(5):
#         print("now executing part: %d" % i)
#         p = multiprocessing.Process(target=worker)  # target=worker
#         jobs.append(p)
#         p.start()
#     print("result=", jobs)

# Answer : ----------------------------------------
# now executing part: 0
# now executing part: 1
# now executing part: 2
# now executing part: 3
# now executing part: 4
# result= [<Process name='Process-1' pid=14344 parent=23324 started>,
#          <Process name='Process-2' pid=14664 parent=23324 started>,
#          <Process name='Process-3' pid=5636 parent=23324 started>,
#          <Process name='Process-4' pid=21408 parent=23324 started>,
#          <Process name='Process-5' pid=23136 parent=23324 started>]
# worker is working...
# worker is working...
# worker is working...
# worker is working...
# worker is working...

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import multiprocessing
# import time
#
# def worker():
#     print("worker is working...")
#     time.sleep(5)
#     print("work done")
#
#
# if __name__ == '__main__':
#     jobs = []
#     for i in range(5):
#         print("now executing part: %d" % i)
#         p = multiprocessing.Process(target=worker()) # target=worker() 執行一個再一個
#         jobs.append(p)
#         p.start()
#     print("result=", jobs)

# Answer: ----------------------------------------------------
# now executing part: 0
# worker is working...
# work done
# now executing part: 1
# worker is working...
# work done
# now executing part: 2
# worker is working...
# work done
# now executing part: 3
# worker is working...
# work done
# now executing part: 4
# worker is working...
# work done
# result= [<Process name='Process-1' pid=21508 parent=20332 stopped exitcode=0>,
# <Process name='Process-2' pid=13032 parent=20332 stopped exitcode=0>,
# <Process name='Process-3' pid=1700 parent=20332 stopped exitcode=0>,
# <Process name='Process-4' pid=16144 parent=20332 stopped exitcode=0>,
# <Process name='Process-5' pid=17864 parent=20332 started>]

# 使用 args 參數來傳入參數 : 參數必須以tuple 形式存入~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import multiprocessing
# import time
#
# def worker(num):
#     print("worker start as parameter:", num)
#     time.sleep(5)
#     print("worker done as parameter:", num)
#     return
#
#
# if __name__ == '__main__':
#     jobs = []
#     for i in range(5):
#         print('now process part:%d' % i)
#         p = multiprocessing.Process(target=worker, args=(i,))  # target=worker, args=(i,)
#         jobs.append(p)
#         p.start()
#     print("jobs=", jobs)
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import multiprocessing
# import time
#
#
# def worker(num, num2):
#     print("worker start as parameter:", num, num2)
#     time.sleep(5)
#     print("worker done as parameter:", num, num2)
#     return
#
#
# if __name__ == '__main__':
#     jobs = []
#     for i in range(5):
#         print('now process part:%d' % i)
#         p = multiprocessing.Process(target=worker, args=(i, i ** 2))
#         jobs.append(p)
#         p.start()
#     print("jobs=", jobs)

#demo 104 用名字來檢查程序~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# (1)use : current_process() 函數來取得目前執行的程序
# (2) use name 成員變數存取道程序的名字
# import multiprocessing
# import time
#
#
# def worker():
#     name = multiprocessing.current_process().name
#     print(f'{name} worker starting')
#     time.sleep(2)
#     print(f'{name} worker exiting')
#
#
# def my_service():
#     name = multiprocessing.current_process().name
#     print(f'{name} my_service starting')
#     time.sleep(2)
#     print(f'{name} my_service exiting')
#
#
# if __name__ == '__main__':
#     service = multiprocessing.Process(name="ftp_service", target=my_service)
#
#     worker_1 = multiprocessing.Process(name="worker_1", target=worker)
#     worker_2 = multiprocessing.Process(target=worker)
#     worker_3 = multiprocessing.Process(target=worker)
#     worker_1.start()
#     worker_2.start()
#     worker_3.start()
#     service.start()

# Demo 105 常駐程序(daemon)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# (1) 當主程式終止時，有daemon 屬性的程式也會被終止
# (2) 比繳 daemon vs 沒有daemon  的差異
# import multiprocessing
# import time
#
# def non_daemon():
#     name = multiprocessing.current_process().name
#     print(f'{name} start')
#     time.sleep(5)
#     print(f'{name} finish')
#
#
# def is_daemon():
#     name = multiprocessing.current_process().name
#     print(f'{name} start')
#     time.sleep(5)
#     print(f'{name} finish')
#
#
# if __name__ == '__main__':
#     p1 = multiprocessing.Process(name="normal_process", target=non_daemon)
#     p2 = multiprocessing.Process(name="daemon_process", target=is_daemon)
#     p2.daemon = True    # setting daemon will be stopped when parent stop
#     p2.start()          # default : daemon = False
#     p1.start()
#     time.sleep(2)
#     print("main program finished")
# Answer :
# daemon_process start
# normal_process start
# main program finished  # daemon_process stop 不會finish
# normal_process finish
# ps: if __name__ == '__main__': time.sleep(6)  daemon_process 會先finish ，Answer is:
# daemon_process start
# normal_process start
# normal_process finish
# daemon_process finish
# main program finished

# demo 106 加了 join() 主程式會等 daemon 完成~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import multiprocessing
# import time
#
#
# def daemon():
#     name = multiprocessing.current_process().name
#     print(f"{name} start")
#     time.sleep(6)
#     print(f"{name} stop")
#
#
# if __name__ == '__main__':
#     d = multiprocessing.Process(name="primary_daemon", target=daemon)
#     d.daemon = True
#     d.start()
#     print("program prepare to wait")
#     d.join()    # join() 主程式會等 daemon 完成
#     print("program terminated")
# Answer :
# program prepare to wait
# primary_daemon start
# primary_daemon stop
# program terminated

# demo107 is_alive()------------------------------------------
# (1) join(timeout) 可以替代 thread 的程式增加timeout
# (2) terminate() 可以停止程序
# (3) 使用alive 檢查程序是否在執行執行 : is_alive()
# import multiprocessing
# import time
#
#
# def daemon():
#     name = multiprocessing.current_process().name
#     print(f"{name} start")
#     time.sleep(6)
#     print(f"{name} stop")
#
#
# def non_daemon():
#     name = multiprocessing.current_process().name
#     print(f"{name} start")
#     print(f"{name} stop")
#
#
# if __name__ == '__main__':
#     p1 = multiprocessing.Process(name='daemon', target=daemon)
#     p1.daemon = True
#
#     p2 = multiprocessing.Process(name='non-daemon', target=non_daemon)
#     p2.daemon = False
#
#     print(f'[before start]d1={p1.is_alive()}, d2={p2.is_alive()}')       # [before start]d1=False, d2=False
#     p1.start()
#     p2.start()
#
#     print(f'[just after start]d1={p1.is_alive()}, d2={p2.is_alive()}')   # [just after start]d1=True, d2=True
#     p1.join(1)    #timeout = 1 second
#
#     print(f'[after join 1 sec]d1={p1.is_alive()}, d2={p2.is_alive()}')   # [after join 1 sec]d1=True, d2=False
#     time.sleep(1)
#
#     print(f'[after sleep 1 sec]d1={p1.is_alive()}, d2={p2.is_alive()}')  # [after sleep 1 sec]d1=True, d2=False
#     p1.join()
#
#     print(f'[after join p1]d1={p1.is_alive()}, d2={p2.is_alive()}')      # [after join p1]d1=False, d2=False

# Answer:
# [before start]d1=False, d2=False
# [just after start]d1=True, d2=True
# daemon start
# non-daemon start
# non-daemon stop
# [after join 1 sec]d1=True, d2=False
# [after sleep 1 sec]d1=True, d2=False
# daemon stop
# [after join p1]d1=False, d2=False

# demo 108 terminate()~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import multiprocessing
# import time
#
#
# def daemon():
#     name = multiprocessing.current_process().name
#     print(f"{name} start")
#     time.sleep(6)
#     print(f"{name} stop")
#
#
# def non_daemon():
#     name = multiprocessing.current_process().name
#     print(f"{name} start")
#     time.sleep(2)
#     print(f"{name} stop")
#
# if __name__ == '__main__':
#     p1 = multiprocessing.Process(name='daemon', target=daemon)
#     p1.daemon = True
#     p2 = multiprocessing.Process(name='non-daemon', target=non_daemon)
#     p2.daemon = False
#
#     print(f'[before start]p1={p1.is_alive()}, p2={p2.is_alive()}')   # [before start]p1=False, p2=False
#     p1.start()
#     p2.start()
#     print(f'[after start]p1={p1.is_alive()}, p2={p2.is_alive()}')    # [after start]p1=True, p2=True
#
#     p1.terminate()
#     p2.terminate()
#     print(f'[just after terminate]p1={p1.is_alive()}, p2={p2.is_alive()}')   # [just after terminate]p1=True, p2=True
#
#     time.sleep(1)
#     print(f'[ after terminate 1 second]p1={p1.is_alive()}, p2={p2.is_alive()}') # [ after terminate 1 second]p1=False, p2=False
# # Answer:
# [before start]p1=False, p2=False
# [after start]p1=True, p2=True
# [just after terminate]p1=True, p2=True
# [ after terminate 1 second]p1=False, p2=False

# demo109 ----------------------------------------------
# import multiprocessing
# import time
#
# def demo_worker():
#     print("start worker")
#     time.sleep(1)
#     print("stop worker")
#
# if __name__ == '__main__':
#     p1 = multiprocessing.Process(target=demo_worker)
#     print("before start:",p1,p1.is_alive())  # before start: <Process name='Process-1' parent=9908 initial> False
#     p1.start()
#     print("after start:", p1, p1.is_alive()) # after start: <Process name='Process-1' pid=16096 parent=9908 started> True
#     # out of control path
#     # p1.terminate()
#     # print("just after terminate:",p1,p1.is_alive())
#     # time.sleep(1)
#     # print("after terminate 1 sec:",p1,p1.is_alive())
#
#     # normal path
#     p1.join()
#     print("after join",p1,p1.is_alive()) # after join <Process name='Process-1' pid=16096 parent=9908 stopped exitcode=0> False
# Answer:
# before start: <Process name='Process-1' parent=9908 initial> False
# after start: <Process name='Process-1' pid=16096 parent=9908 started> True
# start worker
# stop worker
# after join <Process name='Process-1' pid=16096 parent=9908 stopped exitcode=0> False

# demo110 在join 之後可以取得回傳值~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 如果例外發生，會產生執行時期錯誤 runtime error
#
# import multiprocessing
# import sys
# import time
#
# def exit_error():
#     sys.exit(1)
#
# def exit_ok():
#     return
#
# def return_value():
#     return 1
#
# def raises():
#     raise RuntimeError("There was an error!")
#
# def terminated():
#     time.sleep(3)
#
# if __name__ == '__main__':
#     jobs = []
#     for f in [exit_error, exit_ok, return_value, terminated]:
#         print("start process for", f.__name__)
#         j = multiprocessing.Process(target=f, name=f.__name__)
#         jobs.append(j)
#         j.start()
#     jobs[-1].terminate()
#     for j in jobs:
#         j.join()
#         print(f'{j.name} exit code={j.exitcode}')
# Ans: --------------------------------------------
# start process for exit_error
# start process for exit_ok
# start process for return_value
# start process for terminated
# exit_error exit code=1
# exit_ok exit code=0
# return_value exit code=0
# terminated exit code=-15
# demo114~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import multiprocessing
# import sys
# import time
#
#
# def exit_error():
#     sys.exit(1)
#
#
# def exit_ok():
#     return
#
#
# def return_value():
#     return 1
#
#
# def raises():
#     raise RuntimeError("There was an error!")
#
#
# def terminated():
#     time.sleep(3)
#
#
# if __name__ == '__main__':
#     jobs = []
#     for f in [exit_error, exit_ok, return_value, terminated]:
#         print("start process for", f.__name__)
#         j = multiprocessing.Process(target=f, name=f.__name__)
#         jobs.append(j)
#         j.start()
#     jobs[-1].terminate()
#     for j in jobs:
#         j.join()
#         print(f'{j.name} exit code={j.exitcode}')
#
#     for f in [raises]:
#         print("starting process for", f.__name__)
#         j = multiprocessing.Process(target=f, name=f.__name__)
#         jobs.append(j)
#         j.start()
# Ans:
# start process for exit_error
# start process for exit_ok
# start process for return_value
# start process for terminated
# exit_error exit code=1
# exit_ok exit code=0
# return_value exit code=0
# terminated exit code=-15
# starting process for raises
# Process raises:
# Traceback (most recent call last):
#   File "C:\Python\Python38\lib\multiprocessing\process.py", line 315, in _bootstrap
#     self.run()
#   File "C:\Python\Python38\lib\multiprocessing\process.py", line 108, in run
#     self._target(*self._args, **self._kwargs)
#   File "C:\Users\mikal\PycharmProjects\PythonBible\ch01_Python_Introduction\CH01.py", line 3704, in raises
#     raise RuntimeError("There was an error!")
# RuntimeError: There was an error!

# sys.stdout.flush()注释的话，你就只能等到程序执行完毕，屏幕上会一次性输出0，1，2，3，4。 如果你加上
# sample:-----------------------------
# import time
# import sys
#
# for i in range(10):
#     print(i)
#     if i == 5:
#         print("Flushing buffer")
#         sys.stdout.flush()
#     time.sleep(1)

# for i in range(10):
#     print(i,)
#     if i == 5:
#         print("Flushing buffer")
#         sys.stdout.flush()

# for x in range(10000):
#     print ("HAPPY >> %s <<\r" % str(x))
#     sys.stdout.flush()
# -----------------------------------------
# demo111 : 在使用程序時可以有更詳細的輸出訊息 ----------------------------
# import logging
# import multiprocessing
# import sys
#
# def worker():
#     print("doming some work")
#     sys.stdout.flush()   # 寫出訊息
#
# if __name__ == '__main__':
#     multiprocessing.log_to_stderr(logging.DEBUG)
#     p = multiprocessing.Process(target=worker)
#     print("prepare start process")
#     p.start()
#     print("before join process")
#     p.join()
#     print('after join process')
#
#Ans:
# prepare start process
# before join process
# doming some work
# after join process
# [INFO/Process-1] child process calling self.run()
# [INFO/Process-1] process shutting down
# [DEBUG/Process-1] running all "atexit" finalizers with priority >= 0
# [DEBUG/Process-1] running the remaining "atexit" finalizers
# [INFO/Process-1] process exiting with exitcode 0
# [INFO/MainProcess] process shutting down
# [DEBUG/MainProcess] running all "atexit" finalizers with priority >= 0
# [DEBUG/MainProcess] running the remaining "atexit" finalizers

# demo112 自訂日誌 :使用 getLogger 取得日誌並設定它~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import logging
# import multiprocessing
# import sys
#
# def worker():
#     print("doming some work")
#     sys.stdout.flush()
#
# if __name__ == '__main__':
#     multiprocessing.log_to_stderr()
#     logger = multiprocessing.get_logger()
#     logger.setLevel(logging.INFO)
#
#     p = multiprocessing.Process(target=worker)
#     print("prepare start process")
#     p.start()
#     print("before join process")
#     p.join()
#     print('after join process')

# Ans:
# prepare start process
# before join process
# doming some work
# after join process
# [INFO/Process-1] child process calling self.run()
# [INFO/Process-1] process shutting down
# [INFO/Process-1] process exiting with exitcode 0
# [INFO/MainProcess] process shutting down
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 執行續 (Thread)#
#-------------- #
## demo 113 使用Thread 的子類別，來產生一個執行緒
# import threading
# import time
#
# exitFlag = 0
#
#
# class myThread(threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.coutner = counter
#
#
# print("start in main thread")
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)
#
# thread1.start()
# thread2.start()
# print("thread return, prepare to join")
# thread1.join()
# thread2.join()
# print("Main thread complete, prepare to quit")
# Ans:
# start in main thread
# thread return, prepare to join
# Main thread complete, prepare to quit

# demo 114~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import threading
# import time
#
# exitFlag = 0

#
# class myThread(threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.coutner = counter
#
#     def run(self) -> None:
#         print("start a thread:", self.name)
#         time.sleep(2)
#         print("thread finished:", self.name)
#
# print("start in main thread")
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)
#
# thread1.start()
# thread2.start()
# print("thread return, prepare to join")
# # thread1.join()
# # thread2.join()
# print("Main thread complete, prepare to quit")

# ans:
# start in main thread
# start a thread: Thread-1
# start a thread: Thread-2
# thread return, prepare to join
# Main thread complete, prepare to quit
# thread finished: Thread-2
# thread finished: Thread-1

# demo115~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import threading
# import time
# from builtins import next
#
# exitFlag = 0
#
# class myThread(threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.coutner = counter
#
#     def run(self) -> None:
#         global exitFlag
#         print("start a thread:", self.name)
#         print("current exitFlag=",exitFlag)
#         exitFlag += 1
#         time.sleep(2)
#         print("thread finished:", self.name)
#
# print("start in main thread")
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)
#
# thread1.start()
# thread2.start()
# print("thread return, prepare to join")
# thread1.join()
# thread2.join()
# print("Main thread complete, prepare to quit")
# Ans :
# start in main thread
# start a thread: Thread-1
# current exitFlag= 0
# start a thread: Thread-2
# current exitFlag= 1
# thread return, prepare to join
# thread finished: Thread-1
# thread finished: Thread-2
# Main thread complete, prepare to quit

# ---------------#
#Iterator(迭代器) #
# ---------------#
# demo1 (1) iter()  and  next() -----------------------------
# fruits = ["apple","orange","banana","grape"]
# fruits_iterator = iter(fruits)
# for i in range(4):
#     print(next(fruits_iterator))
# next(fruits_iterator)  # StopIteration exception

# Generator (生成器) -------------------
# # demo2 "yield" -----------------------
# def my_gen():
#     n=1
#     print('This is printed first')
#     yield n
#     n+=1
#     print('This is printed second')
#     yield n
#     n += 1
#     print('This is printed at last')
#     yield n
#
# for item in my_gen():
#     print(item)
# print("--------------------")
# a= my_gen()
# next(a)
# next(a)
# next(a)

# demo3 : Decorator :lambda
# 傳統 --------------
# def add_one(num):
#     return num+1
#
# add1 = add_one(10)
# print(add1)
# # 改寫 lambda ---------------
# add2 =lambda x:x+1
# print(add2(10))

# demo4 nested Function --------------------------
# def add_one(num):
#     def plus_one(num):
#         return num+1
#     ans = plus_one(num)
#     return ans
# print(f'add_one(10) ={add_one(10)}')

#demo5 function 當作引數傳遞 ----------------

# def add_one(num):
#     return num+1
#
# def myfunc(func):
#     num = 12
#     return func(num)
#
# print(myfunc(add_one))







