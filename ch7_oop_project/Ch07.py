# 1.Class
# 1. building class-------------------------------
# class Animal():
#     name = "Bird"        # attribute
#     def sing(self):      # Method
#         print("Very Good at singing!")
#
# bird = Animal()         # Object = classname()
# print(bird.name)        # object.attribute
# bird.sing()             # object.mathod()
# 2. class constructs & initial construct ------------------------------
# class Animal():
#     def __init__(self,name):     # initial construct
#         self.name =name
#     def sing(self):
#         print(self.name+" is very good at singing!")
# bird = Animal("parrot")
# print(bird.name)
# bird.sing()
# # ----------------------------------------------------------------------
# class Animal():  # 定義類別
#     def __init__(self, name, age):
#         self.name = name               # 定義屬性
#         self.age = age
#     def sing(self):                    # 定義方法
#         print(self.name + str(self.age) + "歲，很會唱歌!")
#     def grow(self, year):  # 定義方法
#         self.age += year
# bird = Animal("鸚鵡", 1)  # 以 Animal 類別，建立一個名叫鸚鵡、1歲大的 bird物件
# bird.grow(1)  # 長大1歲
# bird.sing()  # 鸚鵡2歲，很會唱歌!
# #----------------------------------------------------------------------
# 3 封裝   encapsulation(使用 private 屬性 & 方法 )
# class Animal():  # 定義類別
#     def __init__(self, name, age):
#         self.__name = name  # 定義私用屬性(只有愛Class 內可以用)
#         self.__age = age
#
#     def __sing(self):       # 定義私用方法 (只有愛Class 內可以用)
#         print(self.__name + str(self.__age), end="歲，很會唱歌，")
#
#     def talk(self):  # 定義共用方法
#         self.__sing()  # 使用私用方法
#         print("也會模仿人類說話!")
# bird = Animal("灰鸚鵡", 2)    # 以 Animal 類別，建立一個名叫灰鸚鵡、2歲大的 bird物件
# bird.talk()                  # (需外部呼叫) 灰鸚鵡2歲，很會唱歌，也會模仿人類說話!

# # 4. 類別繼承  (定義子類別 and used)
# class Animal():  # 定義父類別
#     def __init__(self, name):
#         self.name = name  # 定義共用屬性
#     def fly(self):        # 定義共用方法
#         print(self.name + "很會飛!")
#
# class Bird(Animal):  # 定義子類別
#     def __init__(self, name):
#         self.name = "粉紅色" + name  # 覆寫父類別的建構式
#     def sing(self):  # 定義子類別的方法
#         print(self.name + "也愛唱歌!")
#
# pigeon = Animal("小白鴿")  # 以 Animal 類別，建立一個名叫小白鴿的 pigeon 物件
# pigeon.fly()  # 小白鴿很會飛!
# parrot = Bird("小鸚鵡")  # 以 Bird 類別，建立一個名叫小鸚鵡的 parrot 物件
# parrot.fly()  # 粉紅色小鸚鵡很會飛!
# parrot.sing()  # 粉紅色小鸚鵡也愛唱歌!
# #super() : 子類別用來執行父類別的方法--------------------------------------
# class Animal():  # 定義父類別
#     def __init__(self, name):
#         self.name = name  # 定義共用屬性
#     def fly(self):  # 定義共用方法
#         print(self.name + "很會飛!")
# class Bird(Animal):  # 定義子類別
#     def __init__(self, name, age):
#         super().__init__(name)  # 執行父類別的 __init__()方法
#         self.age = age  # 定義子類別共用屬性
#     def fly(self):  # 定義子類別共用方法
#         print(str(self.age), end="歲")
#         super().fly()  # 執行父類別的 fly方法
# pigeon = Animal("小白鴿")  # 以 Animal 類別，建立一個名叫小白鴿的 pigeon 物件
# pigeon.fly()  # 小白鴿很會飛!
# parrot = Bird("小鸚鵡", 2)  # 以 Bird 類別，建立一個名叫小鸚鵡、2歲大的 parrot 物件
# parrot.fly()  # 2歲小鸚鵡很會飛!
# # 7.4 多型 (polymorphism) ------------------------------------------
# class Animal():  # 定義父類別
#     def fly(self):  # 定義共用方法
#         print("時速 20公里!")
# class Bird(Animal):  # 定義子類別
#     def fly(self, speed):  # 定義共用方法
#         print("時速 " + str(speed) + "公里!")
# class Plane():  # 定義類別
#     def fly(self):  # 定義共用方法
#         print("時速 1000公里!")
# def fly(speed):  # 定義函式
#     print("時速 " + str(speed) + "英哩!")
# animal = Animal()  # 以 Animal 類別建立 animal 物件
# animal.fly()  # 時速 20公里!
# bird = Bird()  # 以 Bird 類別建立 bird 物件
# bird.fly(60)  # 時速 60公里!
# plane = Plane()  # 以 Plane 類別建立 plane 物件
# plane.fly()  # 時速 1000公里!
# fly(5)  # 時速 5英哩!
# # 取得父類別私有型別 -----------------------------------
# class Father():  # 定義父類別
#     def __init__(self, name):
#         self.name = name
#         self.__eye = "黑色"  # 定義私用屬性
#     def getEye(self):  # 定義共用方法傳回私用屬性
#         return self.__eye
#
# class Child(Father):  # 定義子類別
#     def __init__(self, name, eye):
#         super().__init__(name)
#         self.eye = eye
#         self.fatherEye = super().getEye()  # 取得私用屬性
# joe = Child("小華", "棕色")  # 建立子類別物件 joe
# print(joe.name + "眼睛是" + joe.eye + "，他的父親則是" + joe.fatherEye)
# 執行結果：小華眼睛是棕色，他的父親則是黑色
# #7.5 #多重繼承: 先找child#  class method，再由左至右找 parent class method
# class Father():  # 定義父類別
#     def say(self):  # 定義共用方法
#         print("明天會更好!")
#
# class Mother():  # 定義父類別
#     def say(self):  # 定義共用方法
#         print("包容、尊重!")
#
# class Child(Father,Mother):  # 定義子類別，依順序繼承 先Father再Mother
#     pass
# child = Child()  # 建立 child 物件 ,
# child.say()  # 明天會更好!

# 7.6 類別應用------------------------------------------------
class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class Triangle(Rectangle):
    def area2(self):
        return (self.width * self.height) / 2

triangle = Triangle(5, 6)
print("矩形面積=", triangle.area())
print("三角形面積=", triangle.area2())
# # #2. Create project ----------------------------------------------------
# # # Step1 : in PyCharm : File/New Project(project name: 07ProjectHello)
# # # Step2 : 建立一個package 目錄 : (在07ProjectHello，按右鍵:select : New /Directory)
# # #         directory name: mypackage
# # # Step3 : in mypackage 目錄下: New/Python File: 建立 __init__.py & Hello.py
# # # Step4 : in 07ProjectHello目錄下:New/Python File: 建立 index.py
# # # Step5 : write Hello.py code---------------
# # def sayHello():
# #     print("Hello")

# # #Step6 : index.py code---------------
# # from mypackage.Hello import sayHello
# # sayHello()
# # #Step7: run index.py

# # # 2. Bulid your own module ------------------------------------------
# # # (1) 一個XXX.py 可以當作一個模組，用import XXX，可以使用XXX.py 的function: yyy()
# # #     用法 : XXX.yyy()
# # # (2) 用From XXX import yyy ，可以直接使用function:yyy()
# # #     用法 : yyy()
# # # example -----------------
# # # <1> calculate.py as module
# def add(n1,n2)
#    return n1+n2
# def sub(n1,n2)
#    return n1-n2
# <2> 呼叫 Module
import calculate
print(calculate.add(5,2))
print(calculate.sub(5,2))
# # -----------------------------------
# from calculate  import add,sub
print(add(5,2))
print(sub(5,2))
# #------------------------------------
# from calculate  import *     # * is 萬用字(匯入所有函式)
# print(add(5,2))
# print(sub(5,2))
#
# from calculate  import add as a   # as 別名 for 簡化
# print(a(5,2))
# #------------------------------------
# # 3. 類別的模組運用
# # <1> in 07ProjectHello/mypackage 目錄 add Rectangle.py
# # Rectangle.py code:
# class Rectangle()
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width*self.height

# # <2> in 07ProjectHello/mypackage 目錄 add Triangle.py
# Triangle.py code:
# from mypackage.Rectangle import Rectangle
# # Triangle.py 可以繼承Rectangle.py class
# class Triangle(Rectangle):   # 繼承Rectangle.py class
#     def area2(self):
#         return (self.width*self.height)/2

# # <3> index.py code (執行)
# from mypackage.Rectangle import Rectangle  # 父類別先匯入
# from mypackage.Triangle import Triangle    # 子類別後匯入
# triangle = Triangle(5,6)
# print("rectangle area",triangle.area())  # 繼承父類別function
# print("triangle area",triangle.area2())
#
