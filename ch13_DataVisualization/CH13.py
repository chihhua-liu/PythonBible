# 13_Data_Visualize
## Matplotlib module install: pip install matplotlib
## import matplotlib as plt
# 1. 折線圖
# test1 ###(一).繪製折線圖 plot --------------------------------------------
# plot paramater : (1)linewidth or lw : lw=5.0
#                (2)color = 'red' or 'r','cyan'or 'c'. 'magenta' or 'm' ...
#                (3)linestyle or ls : -(實線),--(虛線),-.虛)點線點線,:(點線)
# (4) marker "."(點),"o"(圓),"*"(星),"^"(三角形),"<",">"(三角形),'s'(矩形),'p'(五角形),
#          "h","H"(6邊)"d","D"(鑽型),"+"(十字),"X"(叉叉),"_","|","1","2","3","4"(上下左右人字形)
# import matplotlib.pyplot as plt
#
# listx = [1, 5, 7, 9, 13, 16]
# listy = [15, 50, 80, 40, 70, 50]
# # label 要搭配legend()   #(g--*) 簡寫比較好用
# plt.plot(listx, listy, color='magenta', lw=1.0, ls=':', marker='D', markersize=6, label='label')
# plt.legend()
# plt.show()

# test 2.設定標題&設定座標範圍&設定格線 ---------------------------------------------
# import matplotlib.pyplot as plt
#
# plt.title("Chart Title", fontsize=20)
# plt.xlabel("X-Label", fontsize=14)
# plt.ylabel("Y-Label", fontsize=14)
# listx = [1, 5, 7, 9, 13, 16]
# listy = [15, 50, 80, 40, 70, 50]
# # (g--*) 簡寫比較好用= color="green",is="--",marker="*"
# plt.xlim(0, 20)  # 設定座標範圍
# plt.ylim(0, 100)
# plt.grid(color='red', ls=':', lw=2, alpha=0.5)  # 設定格線, alpha is 透明度
# plt.plot(listx, listy, "g--*", lw=1.0, markersize=6, label='label')
# plt.legend()  # label 要搭配legend()
# plt.show()
# # test3 # 3.同時繪製多組資料 ---------------------------------------------
# import matplotlib.pyplot as plt
#
# listx1 = [1, 5, 7, 9, 13, 16]
# listy1 = [15, 50, 80, 40, 70, 50]
# plt.plot(listx1, listy1, "r-.s")
# listy2 = [10, 40, 30, 50, 80, 60]
# plt.plot(listx1, listy2, "y-.s")
# plt.show()
# # 法二
# plt.plot(listx1, listy1, "r-.s", listx1, listy2, "y-.s")
# plt.show()
#
# # # test 4.設定座標刻度格式 ------------------------------------------------
# import matplotlib.pyplot as plt
#
# listx = [1000, 2000, 3000, 4000, 5000]
# listy = [15, 50, 80, 70, 50]
# plt.grid(color='red', ls=':', lw=2, alpha=0.5)  # 先劃格線
# plt.plot(listx, listy, marker="s")
# plt.xticks(listx)
# plt.tick_params(axis='both', labelsize=16, color='red')
# plt.show()
# # test 5繪製折線圖 & 顯示中文 & 圖表樣式 ------------------------------------
# import matplotlib.pyplot as plt
#
# year = [2015, 2016, 2017, 2018, 2019]
# city1 = [128, 150, 199, 180, 150]
# plt.plot(year, city1, 'r-.s', lw=2, ms=10, label="台北")
# city2 = [120, 145, 180, 170, 120]
# plt.plot(year, city2, 'g--*', lw=2, ms=10, label="台中")
# plt.legend()
# plt.ylim(50, 250)
# plt.xticks(year)
# plt.title("銷售報表", fontsize=18)
# plt.xlabel("Year", fontsize=12)
# plt.ylabel("Million", fontsize=12)
# plt.grid(color='k', ls=':', lw=1, alpha=0.5)
# plt.style.use('seaborn-notebook')  # 圖表樣式
# plt.rcParams["font.sans-serif"] = ['Microsoft JhengHei']  # 顯示中文加2行
# plt.rcParams["axes.unicode_minus"] = False
# plt.show()
# print(plt.style.available)  # 檢視所有預設樣式
# # test 6.繪製折線圖 & 顯示中文 & 圖表樣式 ---------------------------------
# import matplotlib.pyplot as plt
#
# year = [2015, 2016, 2017, 2018, 2019]
# city1 = [128, 150, 199, 180, 150]
# plt.plot(year, city1, 'r-.s', lw=2, ms=10, label="台北")
# city2 = [120, 145, 180, 170, 120]
# plt.plot(year, city2, 'g--*', lw=2, ms=10, label="台中")
# plt.legend()
# plt.ylim(50, 250)
# plt.xticks(year)
# plt.title("銷售報表", fontsize=18)
# plt.xlabel("Year", fontsize=12)
# plt.ylabel("Million", fontsize=12)
# plt.grid(color='k', ls=':', lw=1, alpha=0.5)
# plt.style.use('classic')  # 圖表樣式
# plt.rcParams["font.sans-serif"] = ['Microsoft JhengHei']  # 顯示中文加2行
# plt.rcParams["axes.unicode_minus"] = False
# plt.show()
# print(plt.style.available)  # 檢視所有預設樣式 plt.style.use()
#
# # 2長條圖
# # test1 並列長條圖 ---------------------------------------------------------
# # plt.bar(x座標串列,y座標串列,width =0.8, bottom= 0, color ='red' )
# # (1)bottom: y 座標的起始位置，預設=0
# # (2)label(配合lengnd )
# import matplotlib.pyplot as plt
# import numpy as np
#
# listx = ['c', 'c++', 'c#', 'java', 'python']
# x = np.arange(len(listx))  # 文字必須轉換成數值才能畫圖
# listy = [45, 28, 38, 32, 50]
# listy1 = [40, 25, 48, 22, 50]
# width = 0.2
# plt.ylim(15, 55)
# plt.bar(x, listy, width, color='g', label='Class Program')
# plt.bar(x + width, listy1, width, color='r', label='NO Class')
# plt.xticks(x + width / 2, listx)  # 設定刻度座標& 寫入listx
# plt.title("資訊課程選修人數")
# plt.xlabel("程式課程")
# plt.ylabel("選修/不選修 人數")
# # 加入標籤數值
# for a, b in zip(x, listy):
#     plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=11)
# for a, b in zip(x + width, listy1):
#     plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=11)
# plt.grid(True)  # 加格線
# plt.rcParams["font.sans-serif"] = ['Microsoft JhengHei']  # 顯示中文加2行
# plt.rcParams["axes.unicode_minus"] = False
# plt.legend(bbox_to_anchor=(1, 1), loc='upper left')
# plt.show()
# # test2 堆疊長條圖 -----------------------------------------------------
# import numpy as np
# import matplotlib.pyplot as plt
#
# students = ['Jack', 'Mary', 'Mike', 'David']
# math_scores = [78, 67, 90, 81]
# history_scores = [94, 71, 65, 88]
# x = np.arange(len(students))
# plt.bar(x, math_scores, width=0.2, color='blue', label='Math')
# # 第二組長條圖的bottom 設第一組長條圖的y值
# plt.bar(x, history_scores, width=0.2, color='green', label='History', bottom=math_scores)
# # 加入標籤數值
# for a, b in zip(x, math_scores):
#     plt.text(a, b + 0.05, '%.0f' % b, ha='center', color='red', va='bottom', fontsize=11)
# counter = 0
# for a, b in zip(x, history_scores):
#     global counter
#     h1 = math_scores[counter]
#     plt.text(a, (h1 + b + 0.05), '%.0f' % b, ha='center', color='red', va='bottom', fontsize=11)
#     counter += 1
# plt.xticks(x, students)
# plt.xlabel('Students')
# plt.ylabel('Math')
# plt.title('Final Term')
# plt.legend(bbox_to_anchor=(1, 1), loc='upper left')
# plt.show()

# # test3 繪製橫條圖 -------------------------------------------------------------
# import matplotlib.pyplot as plt
#
# listy = ['c', 'c++', 'c#', 'java', 'python']
# listx = [45, 28, 38, 32, 50]
# plt.barh(listy, listx, height=0.5, color='g', left=0)  # listx,listy 對調，記得要設height
# plt.title("資訊程式課程選修人數")
# plt.xlabel("程式課程")
# plt.ylabel("選修人數")
# # 設定中文字型及負號正確顯示
# plt.rcParams["font.sans-serif"] = ['Microsoft JhengHei']  # 顯示中文加2行
# plt.rcParams["axes.unicode_minus"] = False
# plt.show()
# # 3 串列綜合表達式
# # [表達式(運算式) for 元素 in 串列(if 條件式)]
# # test1
# price = [30, 40, 50, 80, 100]
# tprice = []
# for item in price:
#     tprice.append(item * 1.05)
# print(tprice)
# # 串列綜合表達式簡化程式
# tprice = [item * 1.05 for item in price]
# print(tprice)

# # test2繪製並列長條圖 ---------------------------------------------------
# import matplotlib.pyplot as plt
#
# width = 0.25
# listx = ['c', 'c++', 'c#', 'java', 'python']
# listx1 = [x - width / 2 for x in range(len(listx))]
# listx2 = [x + width / 2 for x in range(len(listx))]
# listy1 = [25, 20, 20, 16, 28]
# listy2 = [20, 8, 18, 16, 22]
# plt.bar(listx1, listy1, width, label='男')
# plt.bar(listx2, listy2, width, color='red', label='女')
# plt.xticks(range(len(listx)), labels=listx)
# plt.legend()
# plt.title("資訊程式課程選修人數")
# plt.xlabel("程式課程")
# plt.ylabel("選修人數")
# # 設定中文字型及負號正確顯示
# plt.rcParams["font.sans-serif"] = ['Microsoft JhengHei']  # 顯示中文加2行
# plt.rcParams["axes.unicode_minus"] = False
# plt.show()
#
# # 4 圓餅圖 -----------------------------------------------------------
# # 參數 : (1)labels : 項目標題的list (2)colors : list:ex:'rgb',['r','g','b']
# # (3)explode : 某一項凸出距離: explode =0.1, (4)labeldistance:項目標題是半徑的多少倍
# # (5)autopct : 項目的百分比的格式: ex: %2.1f%% is 整數2位，小數1位
# # (6)pctdistance : 百分比與圓心距離是半徑的幾倍
# # (7)shadow:布林(True，False) 有沒有陰影
# # (8)startangle: 開始繪圖的起始角度，逆時針計算
# test1 -------------------------------------------------------------
# import matplotlib.pyplot as plt
#
# sizes = [25, 30, 15, 10]
# labels = ["北部", "西部", "南部", "東部"]
# colors = ["red", "green", "blue", "yellow"]
# explode = (0, 0, 0.1, 0)
# plt.style.use('seaborn-notebook')  # 圖表樣式
# plt.pie(sizes,
#         explode=explode,
#         labels=labels,
#         colors=colors,
#         labeldistance=1.1,
#         autopct="%2.1f%%",
#         pctdistance=0.6,
#         shadow=True,
#         startangle=90)
# plt.rcParams["font.sans-serif"] = ['Microsoft JhengHei']  # 顯示中文加2行
# plt.rcParams["axes.unicode_minus"] = False
# plt.show()

# # 5 設定圖表區# 繪製圖時，會自動產生圖表區
# #: figure (圖表區是figure 設定) plt.figure([屬性參數]) : 裡面是list
# # 參數:
# # (1)figsize =[長,寬],ex:[6.4,4.8],(2)dip:解析度(Dots per inch),(3)facecolor:背景顏色,(4)edgecolor:邊線顏色
# # (5)frameon: 布林值(True,False) 是否有邊框 (6) 圖表間是否有邊界:True,False
# test2 -------------------------------------------------------
# import matplotlib.pyplot as plt
#
# plt.figure()
# plt.plot([1, 2, 3])
# plt.figure(figsize=[3, 2], dpi=192, facecolor="whitesmoke", edgecolor="r", linewidth=1, frameon=True)
# plt.plot([1, 2, 3])
# plt.show()


# # 6 多張圖表 : subplot、axes ---------------------------------------------------
# (1) plt.subplot(橫列數，直欄數，圖表索引值)
# Test1
# import matplotlib.pyplot as plt
#
# plt.figure(figsize=[8, 8])  # 自訂圖表區
# plt.subplot(211)  # 2 列 1欄的第1個
# plt.title(label='Chart 1',fontsize=20)
# plt.plot([1, 2, 3], 'r:o')
#
# plt.subplot(212)  # 2 列 1欄的第2個
# plt.title(label='Chart 2',fontsize=20)
# plt.plot([4, 5, 6], 'g--o')
# plt.show()
#
# # Test2 ---------------------------------------------
# import matplotlib.pyplot as plt
#
# plt.figure(figsize=[4, 4])
# plt.subplot(121)  # 1 列 2欄的第1個
# plt.title(label='Chart 1')
# plt.plot([1, 2, 3], 'r:o')
# plt.subplot(122)  # 1 列 2欄的第2個
# plt.title(label='Chart 2')
# plt.plot([1, 2, 3], 'g--o')
# plt.show()

# # Test 3  ----------------------------------------------
# import matplotlib.pyplot as plt
#
# plt.figure(figsize=[4, 4])
# plt.subplot(221)
# plt.title(label='Chart 1')
# plt.plot([1, 2, 3], 'r:o')
# plt.subplot(222)
# plt.title(label='Chart 2')
# plt.plot([1, 2, 3], 'g--o')
# plt.subplot(223)
# plt.title(label='Chart 3')
# plt.plot([1, 2, 3], 'b:o')
# plt.subplot(224)
# plt.title(label='Chart 4')
# plt.plot([1, 2, 3], 'y--o')
# plt.show()
#
# # (2) pit.axes([與左邊界距離, 與下邊界距離，寬，高]) :左下角是圓點
# # test1 -----------------------------------------------------
# import matplotlib.pyplot as plt
#
# plt.figure(figsize=[4, 2])
# plt.axes([0, 0, 0.4, 1])  # 0.4 是寬的0.4倍，1是寬的1倍
# plt.title(label='Chart 1')
# plt.plot([1, 2, 3], 'r:o')
#
# plt.axes([0.5, 0, 0.4, 1])  # 0.5是寬度的0.5倍
# plt.title(label='Chart 2')
# plt.plot([1, 2, 3], 'g--o')
# plt.show()
# # test2
# import matplotlib.pyplot as plt
#
# plt.figure(figsize=[8, 4])
# plt.axes([0, 0, 0.8, 1])
# plt.title(label='Chart 1')
# plt.plot([1, 2, 3], 'r:o')
# plt.axes([0.55, 0.1, 0.2, 0.2])
# plt.title(label='Chart 2')
# plt.plot([1, 2, 3], 'g--o')
# plt.show()
#
# # 7. 股市趨勢圖  # twstock 台灣股市資訊模組
# # pip install twstock   import twstock
# # stock = twstock.Stock(‘2603’) 利用Stock 查詢歷史股票資料ev =twtock.Stock('股票代號')
# # 預設讀近31日資料
# # test1 twstock.Stock -----------------------------------------------
# import twstock
#
# Evergreen = twstock.Stock('2603')
# print(Evergreen.price), print("*" * 30)
# print(Evergreen.date[-1])  # [-1] = 資料最後一筆=today
# print(f'Open開盤價 = {Evergreen.open[-1]}')  # 開盤價
# print(f'high 最高價= {Evergreen.high[-1]}')  # 最高價
# print(f'low 最低價 = {Evergreen.low[-1]}')  # 最低價
# print(f'price 收盤價= {Evergreen.price[-1]}')  # 收盤價
# print(f'capacity成交股數 = {Evergreen.capacity[-1]}')  # 成交股數 [kəˋpæsətɪ]
# print(f'turnover成交金額 = {Evergreen.turnover[-1]}')  # 成交金額
# print(f'change 跌幅價差= {Evergreen.change[-1]}')  # 跌幅價差
# print(f'transaction 成交筆數= {Evergreen.transaction[-1]}')  # 成交筆數

# # teat2 stock.fetch(2022,2)----------------------------------------
# # 1 fetch 方法查歷史資料 : (1) fetch(西元年，月) : 指定月份 (2)  fetch_31() : 最近31天資料
# #                        (3)fetch_from(西元年，月):指定月份到現在
# import twstock
# import matplotlib.pyplot as plt
#
# stock = twstock.Stock('2615')  # 以萬海的股票代號建立 Stock 物件
# stocklist = stock.fetch(2022, 2)  # 取得 2022 年 2 月的資料
# listx = []
# listy = []
# for s in stocklist:
#     print(s.date.strftime('%Y\\%m\\%d'), end='\t')
#     listx.append(s.date.strftime('%d'))
#     print(s.open, end='\t')
#     print(s.high, end='\t')
#     print(s.low, end='\t')
#     print(s.close)
#     listy.append(s.close)
# print(listx)
# print(listy)
# plt.figure(figsize=[8, 8])
# plt.plot(listx, listy, 'r-s', lw=2, ms=10, label="四月股價")
# plt.legend()
# plt.ylim(140, 220)
# plt.xticks(listx)
# plt.title("萬海股價", fontsize=18)
# plt.xlabel("Date", fontsize=16)
# plt.ylabel("收盤價", fontsize=16)
# plt.grid(color='k', ls=':', lw=1, alpha=0.5)
# plt.style.use('seaborn-notebook')  # 圖表樣式
# plt.rcParams["font.sans-serif"] = ['Microsoft JhengHei']  # 顯示中文加2行
# plt.rcParams["axes.unicode_minus"] = False
# plt.show()

# # test3 查即時交易資訊: twstock.realtime.get('股票代號')---------------------------------
# import twstock
# Gigabyte = twstock.realtime.get('3455')
# print(Gigabyte)
# print('*' * 30)
# print(Gigabyte['realtime']['latest_trade_price'])
#
# # test 4 --------------------------------------------
# import matplotlib.pyplot as plt
# import twstock
#
# # 以東鹼的股票代號建立 Stock 物件
# stock = twstock.Stock('1708')
# # 取得 2022 年 3 月的資料
# stocklist = stock.fetch(2022, 3)
# listx = []
# listy = []
# for s in stocklist:
#     listx.append(s.date.strftime('%Y-%m-%d'))
#     listy.append(s.close)
# print(listy)
# plt.figure(figsize=[10, 5])
# plt.title('東鹼2022年3月股價', fontsize=18)
# plt.xlabel("日期", fontsize=14)
# plt.ylabel("股價", fontsize=14)
# plt.plot(listx, listy, 'r:s')
# plt.xticks(rotation=45)
# plt.grid('k:', alpha=0.5)
# plt.ylim(30, 70)
# x = np.arange(len(listx))
# for a, b in zip(x, listy):
#     plt.text(a, b + 0.1, '%.0f' % b, ha='center', color='green', va='bottom', fontsize=13)
# plt.rcParams["font.sans-serif"] = ['Microsoft JhengHei']  # 顯示中文加2行
# plt.rcParams["axes.unicode_minus"] = False
# plt.show()
