from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

iris = datasets.load_iris()  # 匯入鳶尾花的資料
# 定義特徵資料
iris_data = iris.data
iris_label = iris.target
# 可以印出前三筆資料：
print(iris_data[0:3])
print(iris_label[0:3])
# 資料分成兩個部分：訓練資料與測試資料 : train_test_split
train_data , test_data , train_label , test_label = \
    train_test_split(iris_data,iris_label,test_size=0.2) # test_size=0.2 : training 80%，test 20%
#使用KNeighbors分類法，直接使用sklearn的KNeighborsClassifier()
knn = KNeighborsClassifier()
knn.fit(train_data,train_label) # 將資料做訓練
print(knn.predict(test_data))   # 預測我們剛剛切分出來的test_data資料
print(test_label) # 正確答案

