#--------------------------------#
#    例外處理                     #
#------------------------------- #
#  try .... except ......except Exception ......except .....else ......finally
# (1) try :
#        可能引起例外的程式區塊
# (2) except  [as 參數1]:
#        處理例外的程式區塊一
# (3) except  [as 參數2]:
#        處理例外的程式區塊一
# (4) except Exception [as 參數]:
#        處理所有其他例外的程式區塊
# (4) except :
#        處理所有其他可能發生的例外，包括了所有的系統例外
# (5) else:
#        try 中程式正確後的執行區塊
# (6) finally:
#        一定會執行的程式區塊
# Test1 --------------------------------
# n=2
# try:
#     n+=1
# except:
#     print("This number is exist!")
# else:
#     print("n=",n)
# Test2 --------------------------------
# try:
#    print(n)
# except Exception as e :  # Exception 自動Get error
#     print('error:', e)
# finally:                 # finally : 一定會執行的程式段
#     print("must be executed ")
# # # Test3 ---------------------------------
# try:
#     a=int(input("Please Input first number:"))
#     b=int(input("Please Input second number:"))
#     r=a+b
#     print("r=",r)
# except:
#     print("Input is not number")
#
# # Built-in Exceptions ----------------------
# # (1) AttributeError  物件無此屬性
# # (2) Exception       所有的錯誤
# # (3) FileNotFoundError  : open 開啟檔案時找不到檔案
# # (4) IOError : input/output Error
# # (5) IndexError : index Over range
# # (6) MemoryError : 記憶體空間不足
# # (7) NameError : 變數名稱未宣告的錯誤
# # (8) SyntaxError : 語法錯誤
# # (9) TypeError: 資料型別錯誤
# # (10)ValueError : 傳入無效的參數，產生數值錯誤
# # (11)ZeroDivisonError : 除數為0 的錯誤
# # # Test 4 ------------------------------------
# try:
#     a=int(input("Please Input first number:"))
#     b=int(input("Please Input second number:"))
#     r=a%b
# except ValueError:
#     print("傳入無效的參數，產生數值錯誤")
# except Exception as e:
#     print("happen",e)
# else:
#     print("r=", r)
# finally:
#     print("must be executed ")
# # # Test 5 catch multiple errors --------------------------------------
# try:
#     a = int(input("Please Input first number:"))
#     b = int(input("Please Input second number:"))
#     r= a%b
# except(ValueError,ZeroDivisionError):
#     print("Happen Input or zero Error")
# else:
#     print("r=", r)
# # # Test 6 ---------------------------------------------------------------
# try:
#     a = int(input("Please Input first number:"))
#     b = int(input("Please Input second number:"))
#     r= a%b
# except(ValueError, ZeroDivisionError) as e:
#     print("Happen {} zero Error!".format(e))
# else:
#     print("r=", r)
# # # Test 7 ---------------------------------------------------------------
# raise   # 主動拋出例外訊息
# def CheckSpeed(speed) :
#     if speed < 70 :
#         raise Exception("Speed is too slow") # 拋出的例外訊息: Speed is too slow
#     if speed > 110:
#         raise Exception("Speed is over speed") # 拋出的例外訊息: Speed is over speed
#
# for speed in (60,100,150):
#     try:
#         CheckSpeed(speed)
#     except Exception as e:  # e is 拋出例外訊息
#         print("現在速度: {},{} ".format(speed,e))
#     else:
#         print("現在速度: {} is OK! ".format(speed))
# # # # Test 8(key 一遍) ------------------------------------------------------------------
# class MyException(RuntimeError):  # 繼承RuntimeError class
#     def __init__(self, arg):
#         self.args = arg    # 建立建構式接收參數
#
# def CheckSpeed(speed):  # 檢查速度
#     if speed < 70:
#         raise Exception("速度太慢了!")  # 拋出 Exception 型別例外
#     if speed > 110:
#         raise Exception("已經超速了!")  # 拋出 Exception 型別例外
#     else:
#         raise MyException("快樂駕駛，平安返家!")  # 拋出 MyException 型別例外
#
# def convertTuple(tup):  # tuple 轉換為字串
#     str = ''.join(tup)
#     return str
#
# for speed in (60, 100, 150):
#     try:
#         CheckSpeed(speed)  # 檢查速度
#     except MyException as e:  # 接收 MyException 的例外
#         err = convertTuple(e.args)  # tuple 轉換為串字
#         print("目前時速：{}，{}".format(speed, err))
#     except Exception as e:  # 接收 Exception 的例外
#         print("現在速度：{}，{}".format(speed, e))
# # # Test 9 (key 一遍)-------------------------------------------------------------------
# # use traceback Module : format_exc()  將例外引發的資訊的過程記錄在檔案中
# import traceback
#
# def CheckSpeed(speed): #檢查速度
#     if speed < 70:
#         raise Exception("速度太慢了!") # 拋出 Exception 型別例外
#     if speed > 110:
#         raise Exception("已經超速了!") # 拋出 Exception 型別例外
#
# for speed in (60,100,150):
#     try:
#         CheckSpeed(speed) #檢查速度
#     except Exception as e: #接收 Exception的例外
#         with open("err.txt","a") as f:
#             f.write(traceback.format_exc()) #寫入例外過程
#         print("錯誤資訊寫入完成!")
#     else:
#         print("目前時速：{}" .format(speed))
# # # Test 10 --------------------------------------------------------------------
# # # assert: assert 條件式, 參數 (程式開發階段，協助程式設計師檢查程式是否有指定錯誤
# class Car():
#     def __init__(self,speed):
#         self.speed = speed
#     def Turbo(self,n):
#         assert speed >=0,"速度不可能為負"
#         self.speed+=n
#
# for speed in (60,-20):
#     bus = Car(speed)
#     print ("start speed = ",bus.speed, end=" ")
#     bus.Turbo(50)
#     print ("add speed =",bus.speed)