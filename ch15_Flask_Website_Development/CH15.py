# 1. Flask 程式基本架構 pip install flask --------------------
# from flask import Flask
# app = Flask(__name__)
# 路由一
# 路由二
# ...
#
# if __name__ == '__main__':
#    app.run()

# 2. 建立路由(route)
# @app.route("網頁路徑")   # @ 稱為裝飾器(decorator) ，將本烈網頁位置與下一行Function 結合
# def functionName():     # 網頁路徑 : ex:http://127.0.0.1:5000/append
#    處理程式

# test1 step1 : hello.py-------------------------------------------
from flask import Flask

app = Flask(__name__)


@app.route("/hello")
def hello():
    return 'Welcome to Flask'


if __name__ == '__main__':
    app.run()
# step2: Hello.py (必須copy to D:/flask 目錄 ，python file name is hello)
# step3: in CMD 中，D:/flask 目錄執行 :  D:\flask>python hello.py
# step4: in browser 網址列輸入 : http://127.0.0.1:5000/hello
# --> you can see "Welcome to Flask" in browser

# test2 多網址對應相同Function (一般網頁首頁 is index or user 只輸入網址)-------------------
# @app.route("網頁路徑一")
# @app.route("網頁路徑二")
# def functionName():
#    處理程式
# index.py : 執行方式請參考test1
from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return '這是本網站首頁!'


if __name__ == '__main__':
    app.run()

# 3. app.run() 有3個參數 --------------------------------------------------------------------
# (1) host : flask servor default is 127.0.0.1 : if set 0.0.0.0 表所有位置都能連上(網站開發完成)
# (2) port: 埠號 default is 5000
# (3) debug : show error message ，default true ， 網站開發完成 set : false
# ex :　app.run(host='0.0.0.0',port=80,debug=false)

# 4.路由參數傳遞: ---------------------------------------------------------------------------
# @app.route(網頁路徑/<資料型態1:參數1>/<資料型態2:參數2>/...) : 路由傳參數給網頁
# 資料型態 : string,int,float,path(路徑名稱可包含/)
# test3  hello2.py 執行方式請參考test1-----------------------
from flask import Flask

app = Flask(__name__)


@app.route("/hello/<string:name>")
def hello(name):
    return '{},Welcome to Flask'.format(name)


if __name__ == '__main__':
    app.run()

# 5 use template : Flask 提供template 功能，可以直接顯示HTML file-------------------------
# from flask import render_template
# render_template('網頁檔案名稱')
# test4 template.py  執行方式請參考test1，記得templates 目錄要copy to D:/flask -----------
from flask import Flask

app = Flask(__name__)

from flask import render_template


@app.route('/hello')
def hello():
    return render_template('hello.html')


if __name__ == '__main__':
    app.run()

# 6.傳遞參數及變數給網頁檔:　---------------------------------------------------
# @app.route('/hello/<string:name>')
# render_template('網頁檔案名稱', **locals())  **locals() 傳送所有參數及區域變數
# test5 template2.py  執行方式請參考test1 ------------------------------------
from flask import Flask

app = Flask(__name__)

from flask import render_template
from datetime import datetime


@app.route('/hello/<string:name>')
def hello(name):
    now = datetime.now()
    return render_template('hello2.html', **locals())


if __name__ == '__main__':
    app.run()

# ps : browser 輸入 http://127.0.0.1:5000/hello/mika -------------------
# hello2.html : 網頁用 {{name}} 接收
< !DOCTYPE
html >
< html >
< head >
< meta
charset = 'utf-8' >
< title > 傳送參數模版 < / title >
< / head >
< body >
< h1 > Flask
網站 < / h1 >
< h2 > {{name}}，歡迎光臨！ < / h2 >
< h4 > 現在時刻：{{now}} < / h4 >
< / body >
< / html >

# 7.網頁檔使用靜態檔案 在網頁中使用<static> 資料夾中檔案語法--------------------------
# {{url_for('static',filename=靜態檔案名稱)}} :ex: {{url_for('static',filename='ball.png')}}

# test6  template3.py  執行方式請參考test1
from flask import Flask

app = Flask(__name__)

from flask import render_template
from datetime import datetime


@app.route('/hello/<string:name>')
def hello(name):
    now = datetime.now()
    return render_template('hello3.html', **locals())


if __name__ == '__main__':
    app.run()

# hello3.html ---------------
< !DOCTYPE
html >
< html >
< head >
< meta
charset = 'utf-8' >
< title > 使用靜態檔案模版 < / title >
< link
rel = "stylesheet"
href = "{{ url_for('static', filename='style1.css') }}" >
< / head >
< body >
< h1 > Flask
網站
< img
src = "{{ url_for('static', filename='ball.png') }}"
width = "32"
height = "32" / >
< / h1 >
< h2 > {{name}}，歡迎光臨！ < / h2 >
< h4 > 現在時刻：{{now}} < / h4 >
< / body >
< / html >

# 8 Template 語言: Template 組成---------------------------------
# (1)變量 :{{username}}
#   *字典:{{dict1.name}} vs dict1[name](python)
#   *方法:{{obj1.show()}} vs obj1.show()(python)
#   *串列:{{list1.0}} vs list1[0]
# (2)標籤 : {%if found %} ， {%for item in items %}
# (3)單行註解: {# 註解文字 #}
# (4)文字 HTML 標籤與文字

# test7 : variable.py 執行方式請參考test1 for 字典,串列-------------------
from flask import Flask

app = Flask(__name__)

from flask import render_template


@app.route('/variable')
def variable():
    student = {'學號': '874523', '姓名': '張三', '性別': '男'}
    fruit = ['蘋果', '香蕉', '芭樂', '百香果']
    return render_template('variable.html', **locals())


if __name__ == '__main__':
    app.run()

# variable.html ------------
< !DOCTYPE
html >
< html >
< head >
< meta
charset = 'utf-8' >
< title > 第一個模版 < / title >
< / head >
< body >
< h4 > 姓名：{{student.姓名}} < / h4 >
< h4 > 最喜歡的水果：{{fruit
.1}} < / h4 >
< / body >
< / html >

# test8 : if:{% if score>=90 %} for:{% for person in persons%} : show.py
rom
flask
import Flask

app = Flask(__name__)

from flask import render_template


@app.route('/show')
def show():
    person1 = {"name": "Amy", "phone": "049-1234567", "age": 20}
    person2 = {"name": "Jack", "phone": "02-4455666", "age": 25}
    person3 = {"name": "Nacy", "phone": "04-9876543", "age": 17}
    persons = [person1, person2, person3]
    return render_template('show.html', **locals())


if __name__ == '__main__':
    app.run()

# show.html --------------------------
< !DOCTYPE
html >
< html >
< head >
< meta
charset = 'utf-8' >
< title > 基本資料 < / title >
< / head >
< body >
< h3 >
{ %
for person in persons %}
< ul >
< li > 姓名：{{person.name}} < / li >
< li > 手機：{{person.phone}} < / li >
< li > 年齡：{{person.age}} < / li >
< / ul >
{ % endfor %}
< / h3 >
< / body >
< / html >

# 9 以GET & POST 傳送資料 use request module : from flask import request
#  (1) GET 傳送的語法: 網址?參數1=值1& 參數2=值2& 參數3=值3 ...
#       ex : http://127.0.0.1:5000/test?name=david&tel=0936701738
#  (2) @app.route('/網頁路徑', methods=['GET'])
#  (3) use request module : from flask import request ->request.args.get('參數名稱')
#  (4) GET 是將要傳輸的參數置於網址後面(顯示參數)
#  (5) POST 方式傳輸的資料不會顯示於網址列(不顯示參數)
# test9 : GET get1.py  ---------------------
from flask import Flask
from flask import request

app = Flask(__name__)

from flask import render_template


@app.route('/get1', methods=['GET'])
def get1():
    name = request.args.get('name')
    city = request.args.get('city')
    return render_template('get1.html', **locals())


if __name__ == '__main__':
    app.run()

# # get1.html ---------------------------
< !DOCTYPE
html >
< html >
< head >
< meta
charset = 'utf-8' >
< title > 傳送
GET
參數 < / title >
< / head >
< body >
< h1 > Flask
網站 < / h1 >
< h2 > 歡迎來自
{{city}}
的
{{name}}
光臨本網站！ < / h2 >
< / body >
< / html >

# test10 : POST ，post1.py ---------------------------
from flask import Flask
from flask import request

app = Flask(__name__)

from flask import render_template


@app.route('/post1')
def post1():
    return render_template('post1.html')


@app.route('/submit', methods=['POST'])
def submit():
    username = request.values['username'] \
            password = request.values['password']
    if username == 'david' and password == '1234':
        return '歡迎光臨本網站！'
    else:
        return '帳號或密碼錯誤！'


if __name__ == '__main__':
    app.run()

# post1.html ------------------------------
< !DOCTYPE
html >
< html >
< head >
< meta
charset = 'utf-8' >
< title > 傳送
POST
參數 < / title >
< / head >
< body >
< h1 > Flask
網站 < / h1 >
< form
method = 'post'
action = "{{ url_for('submit') }}" >
< p > 帳號： < input
type = 'text'
name = 'username' / > < / p >
< p > 密碼： < input
type = 'text'
name = 'password' / > < / p >
< p > < button
type = 'submit' > 確定 < / button > < / p >
< / form >
< / body >
< / html >
