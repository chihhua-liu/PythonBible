



# from flask import Flask,request, jsonify
# from flask_cors import CORS # 存取跨網域伺服器的資源
# import numpy as np
# import model1
#
# # pip install Flask
# # pip install flask_cors
#
# app = Flask(__name__)  # create Falsk 物件
# CORS(app)
#
# @app.route('/')     # '/' 首頁 路由 : @app.route('網路路徑') : 網路路徑ex: http://127.0.0.1:5000/append
# def index():        # 函式名稱
#     return 'hello'  # 處理程式
#
# @app.route('/predict', methods=['POST'])
# def postInput():
#     # 取得前端傳過來的數值
#     insertValues = request.get_json()
#     x1 = insertValues['sepalLengthCm']
#     x2 = insertValues['sepalWidthCm']
#     x3 = insertValues['petalLengthCm']
#     x4 = insertValues['petalWidthCm']
#     input = np.array([[x1, x2, x3, x4]])
#     #print(input)
#     result = model1.predict(input)
#
#     return jsonify({'return': str(result)})
#
#
#
# if __name__ == '__main__':  # 執行本Flask 程式
#     # debug =True 表示可以直接 realtime 修改程式，API 不用ctrl +C 中斷
#     app.run(host='0.0.0.0', port=3000, debug=True)

# import cv2
# #print( cv2.__version__ )
#
# img = cv2.imread("01.jpg")
# cv2.imshow("MyPicture", img)