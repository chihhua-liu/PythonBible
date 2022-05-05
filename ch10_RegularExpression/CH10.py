#  regular expressio sample
# (1)整數 : [0-9]+
# (2)有小數點的實數 : [0-9]+\.+[0-9]
# (3)英文詞彙 : [A-Za-z]+
# (4)變數名稱 : [A-Za-z_][A-Za-z0-9_]*
# (5)Email: [A-Za-z_]+@[A-Za-z\._]+
# (6)URL : http://[A-Za-z\./_]+

# 電話號碼 : r'\d{4}-\d{6}'

##################################
#   使用re.compile()             #
#   import re                    #
#   pat=re.compile(r'[a-z]+')    #
#   1. match(string)             #
#   2. search(string)            #
#   3. findall()                 #
##################################

# # test 1 : Creat Pattern -------------------------
# import re
# pat = re.compile(r'[a-z]+') # Creat  Pattern
# print(pat, type(pat))
# # -------------------------------------------------
#
# # # test 2 match()---------------------------------
# import re
# pat = re.compile(r'[a-z]+')   #Create pattern
# m = pat.match('tem12po')      # match 找到一個就停
# print(m)   # <re.Match object; span=(0, 3), match='tem'>
# if not m == None:
#    print(m.group())  # tem
#    print(m.start())  # 0
#    print(m.end())    # 3
#    print(m.span())   # (0,3)
# ----------------------------------

# test3 search() =====================================
# import re
# pat = re.compile('[a-z]+')
# m=pat.search('3tem12po')   # 找第一個
# print(m)
# if not m == None:
#     print(m.group())
#     print(m.start())
#     print(m.end())
#     print(m.span())
# =============================================

# test4 findall()------------------------------------------
# import re
#
# pat = re.compile('[a-z]+')
# m = pat.findall('tem12po')
# print(m)
# print(m[0])
# print(m[1])#

# # test 5 re.compile 可省略 ，直接放入收尋的方法中-------------------
# import re
# pat = r'[a-z]+'
# m = re.match(pat,'tem12po')
# print(m)                      # <re.Match object; span=(0, 3), match='tem'>
#
# pat = '[a-z]+'
# m = re.search(pat,'3tem12po')
# print(m)                      # <re.Match object; span=(1, 4), match='tem'>
#
# m=re.findall(r'[a-z]+','tem12po')  # ['tem', 'po']  is list
# print(m)

# test6  phone1 ------------------------------
# import re
# numStr = 'tel:04-12345678'
# pat = r'(\d{2})-(\d{8})'
# phone = re.search(pat,numStr)
# if not phone == None:
#     print(phone.group())     # 完整的搜尋字串  04-12345678
#     print(phone.group(0))    # 完整的搜尋字串  04-12345678
#     print(phone.group(1))    # 第一組字串     04
#     print(phone.group(2))    # 第二組字串     12345678

# test7 phone 2 ------------------------------
# import re
#
# numStr = "tel:(04)12345678"
# pat = r'(\(\d{2}\))(\d{8})'
# phone = re.search(pat, numStr)
# if not phone == None:
#     print(phone.group())      # (04)12345678
#     print(phone.group(0))     # (04)12345678
#     print(phone.group(1))     # (04)
#     print(phone.group(2))     # 12345678

# test8 phone 3 -------------------------------
# import re
# phonelist = ["(04)12345678", "(04)-12345678"]
# pat = r'(\(\d{2}\))-?(\d{8})'   #表示前一項目-? -可以出現0次或1次
# for phone in phonelist:
#     phoneNum = re.search(pat, phone)
#     if not phoneNum == None:
#         print(phoneNum.group())

# test 9 phone 4  區分有括弧與無括弧:------------------------------
# | 同時搜尋比對多個正規表達式
# import re
#
# phonelist = ["0412345678", "(04)12345678", "(04)-12345678", "(049)-2987654", "0937-998877"]
# pat = r'\(\d{2,4}\)-?\d{6,8}|\d{9,10}|\d{4}-\d{6,8}'
#
# for phone in phonelist:
#     phoneNum = re.search(pat, phone)
#     print(phoneNum)
#     if not phoneNum == None:
#         print(phoneNum.group())

# test 10 [+] = [/+] /可省略------------------------------------
# import re
#
# pat = r'[0-9+]+'
# s = "Amy was 18 years old, she likes python and c++123."
# m = re.findall(pat, s)
# print(m)

# test11 * 找不到,回傳空字串-----------------------------------------------
# import re
# pat=re.compile(r'[aeiou]*') # * 可以出現0次到無限次
# s = "John is my best friend."
# m = re.findall(pat,s)    # m is list
# print(m) #['', 'o', '', '', '', 'i', '', '', '', '', '', '', 'e', '', '', '', '', '', 'ie', '', '', '', '']
#
# test 12 + -------------------------------------------------------------
# import re
# pat=re.compile(r'[aeiou]+')    # + 可以出現1次到無限次
# s = "John is my best friend."
# m = re.findall(pat,s)
# print(m)  # ['o', 'i', 'e', 'ie']
#
# test 13 不分大小寫搜尋 re.I ----------------------------------------------
# import re
# pat = r'PYTHON|ANDROID'
# s = "I like Python and Android!"
# m = re.findall(pat, s, re.I)   # m is list
# print(m)  # ['Python', 'Android']

# test 14 ^ (^ 在括號內 : not 的意思) -----------------------------------------------
# import re
#
# pat = r'[^a-z. ]+'
# s = "John was 18 year old."
# m = re.findall(pat, s)
# print(m)  # ['J', '18']
#
# test 15 ^\d+(^ 在正規表達式的起始位置，找符合條件的地一個字 and -------------------------
# \w+$(ru,結束必須是\w，最後一個字) \w = [0-9a-zA-Z] # $符合條件的最後一個字
# import re
#
# pat = r'^\d+'
# s = "2020 is coming soon"
# m = re.findall(pat, s)
# print(m)            # ['2020']
# m2 = re.findall(r'\w+$', s)
# print(m2)           # ['soon']
#
# test 16 r'.o'( and r'.*o'  # .搜尋一個除了\n 以外的字元 , '.o'------------------------
# # 前面有一個字元+以o結尾 '.*o' 前面有2個以上字元+以o結尾
# import re
# pat =r'.o'
# s="DDo your best!"
# m = re.findall(pat,s)
# print(m) # ['Do', 'yo']
# m2 = re.findall(r'.*o',s)
# print(m2) # ['Do yo']

# test17 r'.*' and re.DOTALL(不管換列字元 \n) -----------------------------------------
# import re
# pat = r'.*'    #碰到\n 停止搜尋
# s = "Do your best,\nGo Go Go!"
# m = re.search(pat, s)
# print(m.group())  # Do your best,
# m2 = re.search(r'.*', s, re.DOTALL)  # * 可以出現0次到無限次,re.DOTALL不管換列字元 \n
# print(m2.group())  # Do your best,\nGo Go Go!
# #
# # test 18  re.sub()  --------------------------------------------------------
# import re
# pat=r"\d+"
# substr="123"
# s="Password:1234,ID:5678"
# result = re.sub(pat,substr,s,2)   # 0 全部取代  1取代1次，以此類推
# print(result) # Password:*,ID:*
# # # test 19 ---------------------------------------------------------------
# import re
# def multiply(m):
#     v = int(m.group())
#     return str(v * 2)
#
# result = re.sub("\d+", multiply, "10 20 30 40 50", 3)  # 10,20,30 進入multiply *2 後。回填入
# print(result)  # 20 40 60 40 50
#
# # test 20 Important for application ------------------------------------
html = """
<div class="content">
    E-Mail：<a href="mailto:mail@test.com.tw">mail</a><br>
    E-Mail2：<a href="mailto:mail2@test.com.tw">mail2</a><br>
    <ul class="price">定價：360元 </ul>
    <img src="http://test.com.tw/p1.jpg">
    <img src="http://test.com.tw/p2.jpg">
    <img src="http://test.com.tw/p3.png">
    電話：(04)-76543210、0937-123456
</div>
# """
import re
emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', html)
for email in emails:
     print(email)
price = re.findall(r'[\d]+元', html)[0].split('元')[0]
print(price)

imglist = re.findall(r'[http://]+[a-zA-Z0-9-/.]+\.[jpgpng]+', html)
for img in imglist:  #
    print(img)  # 顯示圖片網址

phonelist = re.findall(r'\(?\d{2,4}\)?\-\d{6,8}', html)
for phone in phonelist:
    print(phone)  # 顯示電話號碼
