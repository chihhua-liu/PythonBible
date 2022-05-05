# 1 Numpy
#(1) Create Numpy:  1D array : shape(4,) ，2D array: shape(2,4)，3D array: shape(3,2,4)
# test 1--------------------------------------
# import numpy as np
# np1 = np.array([1,2,3,4])	#使用list
# np2 = np.array((5,6,7,8))	#使用tuple
# print(np1)
# print(np2)
# print(type(np1), type(np2))
# test2 # dtype------------------------------------
# import numpy as np
# na = np.array([1,2,3,4], dtype=int)
# print(na)            # [1 2 3 4]
# na = np.array([1,2,3,4], dtype=float)
# print(na)            # [1. 2. 3. 4.]
# # np.arange()
# na = np.arange(0, 31, 2)
# print(na)           # [ 0  2  4  6  8 10 12 14 16 18 20 22 24 26 28 30]
# # np.linspace() 等距陣列
# na = np.linspace(1, 15, 8)  # 1 to 15 平均分8個數(頭尾都算7個間隔)
# print(na)           # [ 1.  3.  5.  7.  9. 11. 13. 15.]
# # zeros
# a = np.zeros((4,3,2))
# print(a)
# # ones
# a = np.ones((4,3,2))
# print(a)
# c = np.empty((2,5))  # 隨機值陣列
# print(c)
#[[0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]]
# # Test 3  ---------------------------------
# import numpy as np
# listdata = [[1,2,3,4,5],
#             [6,7,8,9,10],
#             [11,12,13,14,15]]
# na = np.array(listdata)
# print(na)
# print('維度', na.ndim)  #2
# print('形狀', na.shape)  #(3,5)
# print('數量', na.size)    # 15
# adata = np.arange(1,17)
# print(adata)
# bdata = adata.reshape(4,4)
# print(bdata)
# (2) Numpy 取值
# #test 1-------------------------------------
# import numpy as np
# na = np.arange(0,6)
# print(na)           #[0 1 2 3 4 5]
# print(na[0])        #0
# print(na[5])        #5
# print(na[1:5])      #[1 2 3 4]
# print(na[1:5:2])    #[1 3]
# print(na[5:1:-1])   #[5 4 3 2]
# print(na[:])        #[0 1 2 3 4 5]
# print(na[:3])       #[0 1 2]
# print(na[3:])       #[3 4 5]
# # test 2 -----------------------------
# import numpy as np
# na = np.arange(1, 17).reshape(4, 4)
# print(na)
# print(na[2, 3])			#12
# print(na[1, 1:3])		#[6,7]
# print(na[1:3, 2])		#[7,11]
# print(na[1:3, 1:3])		#[[6,7],[7,11]]
# print(na[::2, ::2])		#[[1,3],[9,11]]
# print(na[:, 2])			#[3,7,11,15]
# print(na[1, :])			#[5,6,7,8]
# print(na[:, :])			#矩陣全部
# # test 3 產生隨機資料-----------------------------------
# import numpy as np
# print('1.產生2x3 0~1之間的隨機浮點數\n',
#       np.random.rand(2,3))
# print('2.產生2x3常態分佈的隨機浮點數\n',
#       np.random.randn(2,3))
# print('3.產生0~4(不含5)隨機整數\n',
#       np.random.randint(5))
# print('4.產生2~4(不含5) 5個隨機整數\n',
#       np.random.randint(2,5,[5]))
# print('5.產生3個 0~1之間的隨機浮點數\n',
#       np.random.random(3),'\n',
#       np.random.random_sample(3),'\n',
#       np.random.sample(3))
# print('6.產生0~4(不含5)2x3的隨機整數\n',
#       np.random.choice(5,[2,3]))
# print('7.產生0~42(不含43)6個不重複的隨機整數\n',
#       np.random.choice(43,6,replace=False))   # replace =False 直不重複

# # test 5 np.genfromtxt-------------------------------------
# import numpy as np
# # delimiter = 分隔符號，skip_header=1 (略過第1列)
# a = np.genfromtxt('scores.csv', delimiter=',', skip_header=1)
# print(a.shape)

# # test 6 numpy 運算功能 --------------------------
# import numpy as np
# a = np.arange(1,10).reshape(3,3)
# b = np.arange(10,19).reshape(3,3)
# print('陣列的內容：\n', a)
# print('a array add value 3:\n',a+3)
# print('a array 平方:\n',a**2)
# print('a array 判斷:\n',a<5)
# print('a array 第一row+1:\n',a[0,:]+1)
# print('a array 第一column+1:\n',a[:,0]+1)
# print('a+b = \n',a+b)
# print('a*b = \n',a*b)
# print('a dot b 內積=\n', np.dot(a,b))

# # test 7 ----------------------------------------------
# print('1.最小值與最大值：\n',
#       np.min(a), np.max(a))
# print('2.每一直行最小值與最大值：\n',
#       np.min(a, axis=0), np.max(a, axis=0))
# print('3.每一橫列最小值與最大值：\n',
#       np.min(a, axis=1), np.max(a, axis=1))
# print('4.加總、乘積及平均值：\n',
#       np.sum(a), np.prod(a), np.mean(a))
# print('5.每一直行加總、乘積與平均值：\n',
#       np.sum(a, axis=0), np.prod(a, axis=0), np.mean(a, axis=0))
# print('6.每一橫列加總、乘積與平均值：\n',
#       np.sum(a, axis=1), np.prod(a, axis=1), np.mean(a, axis=1))
# # test 7  ----------------------------------------
# import numpy as np
# a = np.random.randint(100,size=50)
# print('陣列的內容：', a)
# print('1.標準差：', np.std(a))
# print('2.變異數：', np.var(a))
# print('3.中位數：', np.median(a))
# print('4.百分比值：', np.percentile(a, 80))
# print('5.最大最小差值：', np.ptp(a))
# print('6.the index of array min value：',np.argmin(a))
# print('7.the index of array max value：',np.argmax(a))
# print('8.array cumsum：',np.cumsum(a))
# print('9.array cumsprod：',np.cumprod(a))
# # test 8 --------------------------------------------
# import numpy as np
# a = np.random.choice(50, size=10, replace=False)
# print('排序前的陣列：', a)
# print('排序後的陣列：', np.sort(a))
# print('排序後的索引：', np.argsort(a))   # return 排列後的索引 list
# #用索引到陣列取值
# for i in np.argsort(a):
#     print(a[i], end=',')
# # test 9 ---------------------------------------------
# import numpy as np
# a = np.random.randint(0,10,(3,5))
# print('原陣列內容：'), print(a)
# print('將每一直行進行排序：')
# print(np.sort(a, axis=0))
# print('將每一橫列進行排序：')
# print(np.sort(a, axis=1))
# # test10  --------------------------------------
# import numpy as np
# a = np.random.randint(100,size=50)
# print('陣列的內容：', a)
# print('1.標準差：', np.std(a))
# print('2.變異數：', np.var(a))
# print('3.中位數：', np.median(a))
# print('4.百分比值：', np.percentile(a, 80))
# print('5.最大最小差值：', np.ptp(a))
# print('6.the index of array min value：',np.argmin(a))
# print('7.the index of array max value：',np.argmax(a))
# print('8.array cumsum：',np.cumsum(a))  # 索引位置的值 = 自己的值+前面所有位置的值累加
# #print('9.array cumsprod：',np.cumprod(a))
# # test11  --------------------------------------
# import numpy as np
# a = np.arange(1,10).reshape(3,3)
# b = np.arange(10,19).reshape(3,3)
# print('a 陣列的內容：\n', a)
# print('b 陣列的內容：\n', b)
# print('a array add value 3:\n',a+3)
# print('a array 平方:\n',a**2)
# print('a array 判斷:\n',a<5)
# print('a array 第一row+1:\n',a[0,:]+1)
# print('a array 第一column+1:\n',a[:,0]+1)
# print('a+b = \n',a+b)
# print('a*b = \n',a*b)
# print('a dot b 內積=\n', np.dot(a,b))

#  2 Pandas
# (1) Series : 1D , pd.Series(Data[,index = 索引])
# test 1 -----------------------------------------------
# import pandas as pd
# se = pd.Series([1,2,3,4,5])
# print(se)
# print(se.values)
# print(se.index)
#
# print(r'se[2]', se[2])
# print(r'se[2:5]','\n', se[2:5])   # index 2 to (5-1)

# test2  自訂索引-------------------------------------------
# import pandas as pd
# se = pd.Series([1,2,3,4,5], index = ['a','b','c','d','e'])
# print(se)
# print(se['b'])
# print(r'["b":"d"] =')
# print(se['b':'d'])

# test3 # used dictionary build Series ----------------
# import pandas as pd
# dict1 = {'Taipei': '台北', 'Taichung': '台中', 'Kaohsiung':'高雄'}
# se = pd.Series(dict1)
# print(se)
# print("==== value =====")
# print(se.values)
# print("==== index =====")
# print(se.index)
# print("==== se['Taipei']=====")
# print(se['Taipei'])
# print("==== se['Taipei': 'Kaohsiung']=====")
# print(se['Taipei': 'Kaohsiung'])


# # (2)Pandas DataFrame : 2D , like Excel
# # pd.DataFrame(Data [,index = 索引, colunm =欄位])
# # test1 --------------------------------------
# import pandas as pd
# df = pd.DataFrame([[65,92,78,83,70],
#                    [90,72,76,93,56],
#                    [81,85,91,89,77],
#                    [79,53,47,94,80]])
# print(df)  # 自動產生 index & column  number
# test2 -------------------------------------------------
# import pandas as pd
# df = pd.DataFrame([[65,92,78,83,70],
#                    [90,72,76,93,56],
#                    [81,85,91,89,77],
#                    [79,53,47,94,80]],
#                    index=['王曉明', '李小美','陳大明','林小玉'],
#                    columns=['國文','英文','數學','自然','社會'])
# print(df)
#
#
# # Test3 - used dictionary build DataFrameConcat  ----------------------
# import pandas as pd
# scores = {'國文':{'王小明':65,'李小美':90,'陳大同':81,'林小玉':79},
#           '英文':{'王小明':92,'李小美':72,'陳大同':85,'林小玉':53},
#           '數學':{'王小明':78,'李小美':76,'陳大同':91,'林小玉':47},
#           '自然':{'王小明':83,'李小美':93,'陳大同':89,'林小玉':94},
#           '社會':{'王小明':70,'李小美':56,'陳大同':94,'林小玉':80}}
# df = pd.DataFrame(scores) , print(df)

# # Test4  used Series build DataFrame ------------------------------------
# import pandas as pd
# se1 = pd.Series({'王小明':65,'李小美':90,'陳大同':81,'林小玉':79})
# se2 = pd.Series({'王小明':92,'李小美':72,'陳大同':85,'林小玉':53})
# se3 = pd.Series({'王小明':78,'李小美':76,'陳大同':91,'林小玉':47})
# se4 = pd.Series({'王小明':83,'李小美':93,'陳大同':89,'林小玉':94})
# se5 = pd.Series({'王小明':70,'李小美':56,'陳大同':94,'林小玉':80})
# df = pd.DataFrame({'國文':se1, '英文':se2, '數學':se3, '自然':se4, '社會':se5}), print(df)

# # Test 5  concat --------------------------------------------------------
# import pandas as pd
# se1 = pd.Series({'王小明':65,'李小美':90,'陳大同':81,'林小玉':79})
# print(se1)
# se2 = pd.Series({'王小明':92,'李小美':72,'陳大同':85,'林小玉':53})
# se3 = pd.Series({'王小明':78,'李小美':76,'陳大同':91,'林小玉':47})
# se4 = pd.Series({'王小明':83,'李小美':93,'陳大同':89,'林小玉':94})
# se5 = pd.Series({'王小明':70,'李小美':56,'陳大同':94,'林小玉':80})
# df = pd.concat([se1,se2,se3,se4,se5], axis=1) # axis=1 水平合併。 axis =0 垂直合併
# df.columns=['國文','英文','數學','自然','社會']
# print(df)

# DataFrame 資料取值
# Test6 ----------------------------------------------
# import pandas as pd
# scores = {'國文':{'王小明':65,'李小美':90,'陳大同':81,'林小玉':79},
#           '英文':{'王小明':92,'李小美':72,'陳大同':85,'林小玉':53},
#           '數學':{'王小明':78,'李小美':76,'陳大同':91,'林小玉':47},
#           '自然':{'王小明':83,'李小美':93,'陳大同':89,'林小玉':94},
#           '社會':{'王小明':70,'李小美':56,'陳大同':94,'林小玉':80}}
# df = pd.DataFrame(scores)
# print(f'df["自然"] =\n {df["自然"]} ')
# print(f'df[["國文", "數學", "自然"]] =\n {df[["國文", "數學", "自然"]]}')
# print(f'df[df["國文"] >= 80] =  \n {df[df["國文"] >= 80]}')
# print('-----"df.values"----')
# print(df.values)
# print('-----"df.values[1]"----')
# print(df.values[1])
# print('-----"df.values[1][2]"----')
# print(df.values[1][2])
# print('-----df.columns----')
# print(df.columns)
# print('-----df.index----')
# print(df.index)

# Test7 以索引值及欄位取得資料 :loc ------------------------------------
# import pandas as pd
# scores = {'國文':{'王小明':65,'李小美':90,'陳大同':81,'林小玉':79},
#           '英文':{'王小明':92,'李小美':72,'陳大同':85,'林小玉':53},
#           '數學':{'王小明':78,'李小美':76,'陳大同':91,'林小玉':47},
#           '自然':{'王小明':83,'李小美':93,'陳大同':89,'林小玉':94},
#           '社會':{'王小明':70,'李小美':56,'陳大同':94,'林小玉':80}}
# df = pd.DataFrame(scores)
# print(df)
# print('-----(1)------')
# print(df.loc["林小玉", "社會"])
# print('-----(2)------')
# print(df.loc["王小明", ["國文","社會"]])
# print('-----(3)------')
# print(df.loc[["王小明", "李小美"], ["數學", "自然"]])
# print('-----(4)------')
# print(df.loc["王小明":"陳大同", "數學":"社會"])
# print('-----(5)------')
# print(df.loc["陳大同", :])  #陳大同 每科成績
# print('-----(6)------')
# print(df.loc[:"李小美", "數學":"社會"])  # 0 to 李小美 & "數學":"社會" 的index
# print('-----(7)------')
# print(df.loc["李小美":, "數學":"社會"])  # 李小美 to 最後， & "數學":"社會" 的index
# #
#
# # Test8 以索引及欄位編號取得資料 : iloc   與list 取值方式一樣 ----------------------
# import pandas as pd
# scores = {'國文':{'王小明':65,'李小美':90,'陳大同':81,'林小玉':79},
#           '英文':{'王小明':92,'李小美':72,'陳大同':85,'林小玉':53},
#           '數學':{'王小明':78,'李小美':76,'陳大同':91,'林小玉':47},
#           '自然':{'王小明':83,'李小美':93,'陳大同':89,'林小玉':94},
#           '社會':{'王小明':70,'李小美':56,'陳大同':94,'林小玉':80}}
# df = pd.DataFrame(scores)
# print(df)
# print('-----(1)------')
# print(df.iloc[0, [0, 4]] )# 0列 ， 0,3 colunm
# print('-----(2)------')
# print(df.iloc[[0, 1], [2, 3]]) # 0,1列 ， 2,3 colunm
# print('-----(3)------')
# print(df.iloc[0:3, 2:5])  # 0 to 2 row , 2 to 4 column
# print('-----(4)------')
# print(df.iloc[2, :])
# print('-----(5)------')
# print(df.iloc[:2, 2:5])
# print('-----(6)------')
# print(df.iloc[1:, 2:5])
# print('-----(7)------')
# print(df.head(2))  # 前兩筆資料，machine learning 分析資料用(成千上萬筆資料，看幾筆來分析)
# df.tail(2)         # 後兩筆資料，machine learning 分析資料用(成千上萬筆資料，看幾筆來分析)
# df.sample(3)       # 隨機取三筆

# # Test9 DataFrame Data 操作 -----------------------------------------------------------
# import pandas as pd
# scores = {'chinese':{'mika':65,'joe':90,'mary':81,'lin':79},
#           'english':{'mika':92,'joe':72,'mary':85,'lin':53},
#           'math':{'mika':78,'joe':76,'mary':91,'lin':47},
#           'neture':{'mika':83,'joe':93,'mary':89,'lin':94},
#           'society':{'mika':70,'joe':56,'mary':94,'lin':80}}
# df = pd.DataFrame(scores), print(df)

# #  1.依值排列 df.sort_value(by = "欄位", ascending =True or False)--------------------------
# print('sort_values by math')
# print(df.sort_values(by ="math", ascending = False))  # by 欄位ascending=False 遞減排列

# # 2.依索引排列 # df.sort_index(axis = 軸向編號，ascending = True ir False) ----------------
# print('sort_index axis=0')
# print(df.sort_index(axis=0)) # axis=0 以橫列 的index name 排序 預設遞增
# print(df.sort_index(axis = 1))   # axis = 1 以直欄 column name 排列

# # 3.DataFrame 資料修改
# df.loc['mika']['math'] = 99 , print(df)
# df.loc["mika":"lin"]["math"] = 100, print(df)

# # 4.DataFram 刪除資料  # ps : if要改掉 df 的值 inplace =True
# df1 = df.drop("mika") ,print(df1)
# df2 = df1.drop("math", axis =1), print(df2)
# df3 =df.drop(["math","neture"], axis=1) ,print(df3)
# df4 = df.drop(df.index[1:4]) , print(df4)
# df5 = df.drop(df.columns[1:4],axis =1), df5

# # Pandas Data Access ---------------------------------------------------------------------------
# # (1)pd.read_csv(*.csv)  (2)pd.read_excel(*.xlsx) (3)pd.read.sql(&=*.sqlite): 匯入SQLite Data
# # (4)read_json(*json)  (5)read_html(*.html)
# # pd.read_csv(檔案名稱[, header = 欄位列, index_col =索引欄,encoding = 編碼, sep = 分隔符號)

# # Test 9 --------------------------------------------------------------------
# import pandas as pd
# data = pd.read_csv("scores2.csv", header=0, index_col=0)
# print(data)
# print(type(data))
#
# # # Test10 pd.read_html(檔案名稱[, header=欄位列, index_col=索引欄,encoding = 編碼, keep_default_na = False)
# # # keep_default_na : 是否去除空白值(NaN)
# import pandas as pd
# url = 'https://www.tiobe.com/tiobe-index/'
# tables = pd.read_html(url, header=0, keep_default_na=False)
# print(tables[0])
# # Test 11使用 Pandas 儲存資料 ------------------------------------------------
# # (1)df.to_csv(*.csv) (2)to_excel()   (3)to_sql   (4)to_json   (5)to_html
# # pd.to_csv(檔案名稱[, header = 布林值, index_col =布林值,encoding = 編碼, sep = 分隔符號)
# # header,index_col : default value is True
# import pandas as pd
# scores = {'國文':{'王小明':65,'李小美':90,'陳大同':81,'林小玉':79},
#           '英文':{'王小明':92,'李小美':72,'陳大同':85,'林小玉':53},
#           '數學':{'王小明':78,'李小美':76,'陳大同':91,'林小玉':47},
#           '自然':{'王小明':83,'李小美':93,'陳大同':89,'林小玉':94},
#           '社會':{'王小明':70,'李小美':56,'陳大同':94,'林小玉':80}}
# df = pd.DataFrame(scores)
# df.to_csv('scores3.csv', encoding='utf-8-sig')

# # Test 12 Pandas module : 繪圖應用-----------------------------------------------
# # DataFrame.plot()
# # 參數 : (1)kind 設定繪圖模式 : 參數值: line(折線圖) ,hist,scatter,bar,bath,pie # (2)title (3)legend (4)grid (5)xlim (6)ylim  (7)xticks (8)yticks (9)x  (10)y (11)fontsize (12)figsize
# import pandas as pd
# import matplotlib.pyplot as plt  # 畫圖用
# # 設定中文字型及負號正確顯示
# plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" #也可設mingliu或DFKai-SB
# plt.rcParams["axes.unicode_minus"] = False
#
# df = pd.DataFrame([[250,320,300,312,280],
#                    [280,300,280,290,310],
#                    [220,280,250,305,250]],
#                    index=['北部','中部','南部'],
#                    columns=[2015,2016,2017,2018,2019])
# print(df)
#
# g1 = df.plot(kind='bar', title='長條圖',grid=True, figsize=[10,5])
# g2 = df.plot(kind='barh', title='橫條圖', figsize=[10,5])
# g3 = df.plot(kind='bar', stacked=True, title='堆疊圖', figsize=[10,5])
# plt.show()
# #
#
# # Test 13 line(折線圖)--------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
# 設定中文字型及負號正確顯示
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" #也可設mingliu或DFKai-SB
plt.rcParams["axes.unicode_minus"] = False

df = pd.DataFrame([[250,320,300,312,280],
                   [280,300,280,290,310],
                   [220,280,250,305,250]],
                   index=['北部','中部','南部'],
                   columns=[2015,2016,2017,2018,2019])

g1 = df.iloc[0].plot(kind='line', legend=True, xticks=range(2015,2020), title='公司分區年度銷售表', figsize=[10,5])
g1 = df.iloc[1].plot(kind='line', legend=True, xticks=range(2015,2020))
g1 = df.iloc[2].plot(kind='line', legend=True, xticks=range(2015,2020))
# Test 14 pie (圓餅圖)--------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
# 設定中文字型及負號正確顯示
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  #也可設mingliu或DFKai-SB
plt.rcParams["axes.unicode_minus"] = False

df = pd.DataFrame([[250,320,300,312,280],
                   [280,300,280,290,310],
                   [220,280,250,305,250]],
                   index=['北部','中部','南部'],
                   columns=[2015,2016,2017,2018,2019])
df.plot(kind='pie', subplots=True, figsize=[15,15])
plt.show()

