## t1 -----------------------------
# dict1 = {"香蕉": 20, "蘋果": 50, "橘子": 30}
# print("香蕉 = %d 元" % dict1["香蕉"])
# key1 = list(dict1.keys())              # keys()
# print("{} = {} 元".format(key1[0], dict1[key1[0]]))
## t2 -----------------------------
# dict1 = {"A": "內向穩重", "B": "外向樂觀", "O": "堅強自信", "AB": "聰明自然"}
# name = input("輸入要查詢的血型:")
# blood = dict1.get(name)                  #get()
# if blood == None:
#     print("沒有「" + name + "」血型！")
# else:
#     print(name + " 血型的個性為：" + str(dict1[name]))
# ## t3 ------------------------------
# dict1 = {"香蕉": 20, "蘋果": 50, "橘子": 30}
# dict1["蘋果"] = 80  # modify dictionary value fo key
# print(dict1)        # {'香蕉': 20, '蘋果': 80, '橘子': 30}
# del dict1["蘋果"]   # del element
# print(dict1)        # {'香蕉': 20, '橘子': 30}
# dict1.clear()       # del all element
# print(dict1)        # {}
# del dict1           # del dict1
# #print(dict1)        # NameError: name 'dict1' is not defined
# # # t4 -- Advanced Functions -----------------------------------
# # (1) len()
dict1 = {"banana": 20, "apple": 50, "orange": 30}
# dict1len = len(dict1)
# print("dict1 len = %d" % dict1len)  # 3
# # # (2) copy() -------------------------------------------------
# # dict2 = dict1.copy()
# # print(dict2)
# # # (3) in -----------------------------------------------------
# b = "job" in dict1
# c = "apple" in dict1
# print("b={},c={}".format(b,c))
#
# item1=dict1.items()
# print(item1)
# print(type(item1))
# for itemx in item1 :   # itemx is tuple
#      print(itemx)
# #
# listkey = list(dict1.keys())
# listvalue = list(dict1.values())
# for i in listkey :
#     print(i)
# for j in listvalue :
#     print(j)
#
# #(4) # ***** Important  for dictionary Items()******
# item1=dict1.items()
# for itemx in item1 :
#     print(itemx)
#
# for (k,v) in item1 :
#     print(type(k),k)
#     print(type(v),v)
# #(5) key() & values() ------------------------------------------
listkey = list(dict1.keys())
listvalue = list(dict1.values())
for i in listkey :
   print(i)
for j in listvalue :
   print(j)
# #(6) setfefault()-----------------------------------------------
# # if isn't dict1 element ， add key& value and read default value =100
x = dict1.setdefault("pineapple",100)
y = dict1.setdefault("apple",300)      # if is dict1 element, read value
print(dict1,x,y)   # {'banana': 20, 'apple': 50, 'orange': 30, 'pineapple': 100} 100 50
# # t4 --------------------------------------------------------
dict1 = {"林小明":85, "曾山水":93, "鄭美麗":67}
name = input("輸入學生姓名：")
if name in dict1:
    print(name + "的成績為 " + str(dict1[name]))
else:
    score = input("輸入學生分數：")
    dict1[name] = score
print("字典內容：" + str(dict1))
#
#  # t5 --------------------------------------------------
# dict1={"金牌":26, "銀牌":34, "銅牌":30}
# listkey = list(dict1.keys())
# listvalue = list(dict1.values())
# for i in range(len(listkey)):
#     print("得到的 %s 數目為 %d 面" % (listkey[i], listvalue[i]))
#
# # t6 -----------------------------------------------
# dict1={"金牌":26, "銀牌":34, "銅牌":30}
# item1 = list(dict1.items())
# for name, num in item1:
#     print("得到的 %s 數目為 %d 面" % (name, num))
