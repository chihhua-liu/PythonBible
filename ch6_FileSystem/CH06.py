# 1.os
import os
# (1). getcwd() -------------------------------------
print(os.getcwd()) # working directory
# (2). path.exists(file) , remove(file)-----------------------------------
file ='myFile.txt'
if os.path.exists(file):
  os.remove(file)
else:
 print(file+'檔案未建立')
# # (3). os.mkdir('myDir')--------------------------------------
# dir1 = 'myDir'
# if not os.path.exists(dir1):
#    os.mkdir(dir1) #建立指定目錄
# else:
#    print(dir1+" directory is created")
# # (4) os.rmdir() ---------------------------------------------
# dir1 = 'myDir'
# if os.path.exists(dir1):
#   os.rmdir('myDir')   #刪除目錄
# else:
#   print(dir1+" directory is not created")
# # (5) system() -----------------------------------------------
# cur_path=os.getcwd() # 取得目前路徑
# os.system("cls")  # 清除螢幕
# os.system("mkdir dir2")  # 建立 dir2 目錄
# os.system("copy ossystem.py dir2\copyfile.py") # 複製檔案
# file=cur_path + "\dir2\copyfile.py"
# os.system("notepad " + file)  # 以記事本開啟 copyfile.py 檔
# # (6) os.path.abspath()---------------------------------------------
# filename=os.path.abspath("osexists.py")        #完整路徑名稱：C:\Users\mikal\PycharmProjects\PythonBible\ch6\osexists.py
# if os.path.exists(filename):                   #檢查檔案是否存在
#     print("完整路徑名稱：" + filename)
#     print("檔案大小：" , os.path.getsize(filename))
# # (7) os.path.dirname(__file__) -------------------------------------------------------------
# cur_path=os.path.dirname(__file__) # 現在目錄路徑：C:/Users/mikal/PycharmProjects/PythonBible/ch6
# print("現在目錄路徑："+cur_path)
# # # (8) os.path.abspath & basename & dirname & isdir() & isfile() & split() & splitdriver() & join()-------------------
# filename=os.path.abspath("ospath.py")
# if os.path.exists(filename):
#    basename=os.path.basename(filename) # os.path.basename(filename)
#    print("最後的檔案或路徑名稱：basename : " + basename)  # ospath.py
#
#    dirname=os.path.dirname(filename)
#    print("目前檔案目錄路徑：dirname : " + dirname)  # C:\PythonBook
#
#    print("是否為目錄：isdir : ",os.path.isdir(filename)) # False (is file)
#    print("是否為檔案：isfile : ", os.path.isfile(filename))  # True (is file)
#
#    fullpath,fname=os.path.split(filename)
#    print("目錄路徑：split : " + fullpath)   # C:\PythonBook
#    print("檔名：split : " + fname)          # ospath.py
#    mainfileName,1.os
# import os
# # (1). getcwd() -------------------------------------
# print(os.getcwd()) # working directory
# # (2). path.exists(file) , remove(file)-----------------------------------
# file ='myFile.txt'
# if os.path.exists(file):
#   os.remove(file)
# else:
#  print(file+'檔案未建立')
# # (3). os.mkdir('myDir')--------------------------------------
# dir1 = 'myDir'
# if not os.path.exists(dir1):
#    os.mkdir(dir1) #建立指定目錄
# else:
#    print(dir1+" directory is created")
# # (4) os.rmdir() ---------------------------------------------
# dir1 = 'myDir'
# if os.path.exists(dir1):
#   os.rmdir('myDir')   #刪除目錄
# else:
#   print(dir1+" directory is not created")
# (5) system() -----------------------------------------------
# cur_path=os.getcwd() # 取得目前路徑
# os.system("cls")  # 清除螢幕
# os.system("mkdir dir2")  # 建立 dir2 目錄
# os.system("copy ossystem.py dir2\copyfile.py") # 複製檔案
# file=cur_path + "\dir2\copyfile.py"
# os.system("notepad " + file)  # 以記事本開啟 copyfile.py 檔
# (6) os.path.abspath()---------------------------------------------
# filename=os.path.abspath("osexists.py")        #完整路徑名稱：C:\Users\mikal\PycharmProjects\PythonBible\ch6\osexists.py
# if os.path.exists(filename):                   #檢查檔案是否存在
#     print("完整路徑名稱：" + filename)
#     print("檔案大小：" , os.path.getsize(filename))
# # # (7) os.path.dirname(__file__) -------------------------------------------------------------
# cur_path=os.path.dirname(__file__) # 現在目錄路徑：C:/Users/mikal/PycharmProjects/PythonBible/ch6
# print("現在目錄路徑："+cur_path)
# # # (8) os.path.abspath & basename & dirname & isdir() & isfile() & split() & splitdriver() & join()-------------------
# filename=os.path.abspath("ospath.py")
# if os.path.exists(filename):
#    basename=os.path.basename(filename) # os.path.basename(filename)
#    print("最後的檔案或路徑名稱：basename : " + basename)  # ospath.py
#
#    dirname=os.path.dirname(filename)
#    print("目前檔案目錄路徑：dirname : " + dirname)  # C:\PythonBook
#
#    print("是否為目錄：isdir : ",os.path.isdir(filename)) # False (is file)
#    print("是否為檔案：isfile : ", os.path.isfile(filename))  # True (is file)
#
#    fullpath,fname=os.path.split(filename)
#    print("目錄路徑：split : " + fullpath)   # C:\PythonBook
#    print("檔名：split : " + fname)          # ospath.py
#    mainfilename,extension = fname.split('.')
#    print('-------------mainfilename,extension ====================')
#    print(mainfilename,extension)
#
#    Drive,fpath=os.path.splitdrive(filename)
#    print("磁碟機：splitdrive : " + Drive)   # C:
#    print("路徑名稱：splitdrive : " + fpath) # \PythonBook\ospath.py
#
#    fullpath = os.path.join(fullpath + "\\" + fname)
#    print("組合路徑=join :  " + fullpath) # C:\PythonBook\ospath.py

# # # (9) os.walk -----------------------------------------------------------
# cur_path = os.path.dirname(__file__)  # 取得目前路徑
# sample_tree = os.walk(cur_path)
# for dirname, subdir, files in sample_tree:
#     print("檔案路徑：", dirname)
#     print("目錄串列：", subdir)
#     print("檔案串列：", files)
#     print()
#
# 2. shutil & glob 模組
# import shutil    # 使用 shutil.py
# import os
# cur_path=os.path.dirname(__file__) # 取得目前路徑
# print(cur_path)
# destfile= cur_path + "\\" + "newfile.py"
# shutil.copy("shutil.py", destfile)  # 檔案複製
# shutil.copyfile("shutil.py", "new.py")  # 檔案複製
# #------------------------------------------------------
# import shutil
# shutil.copytree("oswalk","C:\\newoswalk" )  # 目錄複製
# #------------------------------------------------------
# import shutil
# shutil.rmtree("C:\\newoswalk" )  # 刪除目錄
# from glob2 import glob
# files = glob("glob.py")+glob("os*.py")+glob("*.txt")
# for file in files:
#     print(file)
#
# 3. 檔案的讀寫
# -------------------------------------------------
# with open('file.bin', 'rb') as f:
#     content=f.read().decode("utf-8")
#     print(content)
# # #------------------------------------------------------
# # file.bin 內容
# '''Hello Python
# 中文字測試
# Welcome
# '''
# f=open('file.bin', 'rb')
# print("目前文件索引位置：",f.tell()) #0
# f.seek(6) #移到索引第 6 (第7個字元)位置
# str1=f.read(7) #讀取 7 個字元
# print(str1)  # b'Python\n'
# print("目前文件索引位置：",f.tell()) #13
#
# f.seek(0) #回文件最前端
# print("目前文件索引位置：",f.tell()) #0
# str2=f.read(5) #讀取 5 個字元
# print(str2)  # b'Hello'
#
# f.seek(-8,2) #移至最尾端，向前取 8 個字元
# str3=f.read()
# print(str3)  # b'Welcome\n'
#
# f.close()
#
#
#
#    Drive,fpath=os.path.splitdrive(filename)
#    print("磁碟機：splitdrive : " + Drive)   # C:
#    print("路徑名稱：splitdrive : " + fpath) # \PythonBook\ospath.py
#
#    fullpath = os.path.join(fullpath + "\\" + fname)
#    print("組合路徑=join :  " + fullpath) # C:\PythonBook\ospath.py
#
# # # (9) os.walk -----------------------------------------------------------
# cur_path = os.path.dirname(__file__)  # 取得目前路徑
# sample_tree = os.walk(cur_path)
# for dirname, subdir, files in sample_tree:
#     print("檔案路徑：", dirname)
#     print("目錄串列：", subdir)
#     print("檔案串列：", files)
#     print()
#
# 2. shutil & glob 模組
# import shutil    # 使用 shutil.py
# import os
# cur_path=os.path.dirname(__file__) # 取得目前路徑
# print(cur_path)
# destfile= cur_path + "\\" + "newfile.py"
# shutil.copy("shutil.py", destfile)  # 檔案複製
# shutil.copyfile("shutil.py", "new.py")  # 檔案複製
# #------------------------------------------------------
# import shutil
# shutil.copytree("oswalk","C:\\newoswalk" )  # 目錄複製
# #------------------------------------------------------
# import shutil
# shutil.rmtree("C:\\newoswalk" )  # 刪除目錄
# from glob2 import glob
# files = glob("glob.py")+glob("os*.py")+glob("*.txt")
# for file in files:
#     print(file)
#
# 3. 檔案的讀寫
# f.write
content='''Hello Python
英文字測試
Welcome
'''
# ''' 保持原來的格式輸出 '''
f=open('file1.txt', 'w')
f.write(content)
f.close()
#--------------------------------------------
f=open('file1.txt', 'rt')  # t:文字檔 ，b: 二進位檔
for line in f:
    print(line,end="")
f.close()
#--------------------------------------------
import locale
print(locale.getpreferredencoding())   #cp950 Microsoft 的繁體中文字元集標準 ，約=Big5
#-------------------------------------------
f =open('file2.txt', 'r', encoding ='UTF-8')     #  encoding ='UTF-8'
for line in f:
    print(line,end="")
f.close()
# #-------------------------------------------
with open('file1.txt', 'r') as f:
    str1=f.read()
    print(str1)  # Hello
#----------------------------------------------
with open('file2.txt', 'r', encoding ='UTF-8') as f:
    # print(f.readline())  # 123中文字\n
    # print(f.readline()) # abc
    # print(f.readline())  # abc
    print(f.readlines())   # ['\ufeff123中文字\n', 'abcde\n', 'hello\n'] 會有擋頭\ufe
# #---------------------------------------------
with open('file1.txt', 'r') as f:
    content=f.readlines()
    print(type(content))   # <class 'list'>
    print(content)
#---BOM ------------------------------------------------------------------------
with open('file2.txt', 'r', encoding='UTF-8-sig') as f: #UTF-8-sig: sig 去檔頭
    doc = f.readlines()
    print(doc)

with open('file2.txt', 'r', encoding='UTF-8-sig') as f:   # UTF-8-sig : delete file header
    str1 = f.read(5)
    print(str1)  # 123中文
#---------------------------------------------------------
# -------------------------------------------------
with open('file.bin', 'rb') as f:
    content=f.read().decode("utf-8")
    print(content)
# # #------------------------------------------------------
# # file.bin 內容
# '''Hello Python
# 中文字測試
# Welcome
# '''
# f=open('file.bin', 'rb')
# print("目前文件索引位置：",f.tell()) #0
# f.seek(6) #移到索引第 6 (第7個字元)位置
# str1=f.read(7) #讀取 7 個字元
# print(str1)  # b'Python\n'
# print("目前文件索引位置：",f.tell()) #13
#
# f.seek(0) #回文件最前端
# print("目前文件索引位置：",f.tell()) #0
# str2=f.read(5) #讀取 5 個字元
# print(str2)  # b'Hello'
#
# f.seek(-8,2) #移至最尾端，向前取 8 個字元
# str3=f.read()
# print(str3)  # b'Welcome\n'
#
# f.close()
# load Json.file------------------------------------------
import json
data = dict()
with open('password.txt', 'r', encoding ='UTF-8-sig') as f:
   filedata = f.read()
   print(filedata)
#   filedata = filedata.replace("\'", "\"")
#   data = ast.literal_eval(filedata)
   data = json.loads(filedata)
print(type(data),data)

