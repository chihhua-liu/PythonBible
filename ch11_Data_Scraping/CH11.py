# CH11 Data Scraping
#在網路有系統的自動收集資料，必須將網站的網頁內容或檔案擷取下來
#  一 requests requests 模組:
# (1) requeats.get()
# test 1: requests.get(url) ---------------------------------------------------
#get(url) 瀏覽器輸入網址-> 送出，指定網站伺服器接收到要求後回覆內容，可以在瀏覽器看到網頁內容，這個方式稱get
#回應內容包括: text(網頁source code) content(網站2進位檔案資料)status_code: HTTP 狀態碼
import requests

url = 'http://www.ehappy.tw/demo.htm'
r = requests.get(url)

if r.status_code == requests.codes.ok:
    print(r.text)
# # -------------------------------------------------------------------------
# # PS: url 可以帶網址+參數(查詢參數or 測試參數 :
# # ex: http://www.test.com/?x=value1&y=value2  # ? is 網址連結參數的符號，& is 參數連接符號
# # test 2: url + parameters ------------------------------------------------
import requests

payload = {'key1':'value1','key1':'value1'}
r =requests.get("http://httpbin.org/get",params=payload)
if r.status_code == requests.codes.ok:
    print(r.text)
#--------------------------------------------------------------------------
# PS: http://httpbin.org/ 是requests 的測試網站，回應json 格式
# http://httpbin.org/get  , http://httpbin.org/post
# (2) requeats.post(): post 請求是HTTP請求，網頁中有讓使用者填入資料的表單，常用post 請求進行傳送
# post 傳遞的參數要定義成字典資料型態
# test 3: ----------------------------------------------------------------
import requests
# 將查詢參數加入 POST 請求中
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)
#
# #(3) set HTTP Headers 偽裝瀏覽器
# # test 4:  --------------------------------------------------------------
import requests
url = 'https://irs.thsrc.com.tw/IMINT/'
# 自訂表頭
headers={
   'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
}
# # 將自訂表頭加入 GET 請求中
r = requests.get(url, headers=headers)
print(r)
# #(4) Session & Cookie
# # test 5  --------------------------------------------------------------
# # user used browser 訪問瀏覽器時，伺服器會發給用戶端一個憑證以供識別
# # # 這個憑證存在用戶端稱Cookie，產生在伺服器稱Session
import requests
url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
# 設定cookies的值
cookies = {'over18':'1'}
r = requests.get(url, cookies=cookies)
print(r.text)

# # (5) IP address 查詢器
# # test 6: --------------------------------------------------------------
import requests
# 設定查詢目前IP的api網址
url = 'https://api.ipify.org'
r = requests.get(url)
print('我目前的IP是：', r.text)

# 二 BeautifulSoup 模組: 網頁解析: get html 標籤後內容 & text(網頁source code)
# 1 取得網頁原始碼，用BeautifulSoup 模組 可以快速解析而準確地對網頁特定目標加以分析和擷取
# 2 pip install beautifulsoup4
# 3 必須了解網頁結構 html

# # test1 ----------------------------------------------------------------
import requests
from bs4 import BeautifulSoup
url = 'http://ehappy.tw/bsdemo1,htm'
html = requests.get(url)
html.encoding = 'UTF-8'
print(html.text)   # text : 傳回去除HTML 標籤後的文字內容
#
sp = BeautifulSoup(html.text,'html.parser') #parser n.語法分析程序 (解析HTML原始碼)
print(f'sp.title = {sp.title}')
print(f'sp.title.text = {sp.title.text}')
print(f'sp.h1 = {sp.h1}')
print(f'sp.p = {sp.p}')

# # #------------------------------------------------------
# # BeautifulSoup 常用的方法:
# (1) find() :尋找第一個符合條件的標籤，以字串回傳
# (2) findall(): 尋找全部符合條件的標籤，以List回傳
# (3) select: 尋找指定CSS 選擇器: ex: id or class ，以List回傳 (#id_name)or select(.classname)
# # example :datas = sp.find_all("img",width=20) #(標籤名稱，屬性名稱=屬性內容)
# #          datas = sp.find_all("p", class_ = 'red') # 屬性是class 類別 用 class_
# #          datas = sp.find_all("img",{"width" : "20"})
# # test2 : find , findful -------------------------------------------------------
from bs4 import BeautifulSoup
html = '''
<html>
  <head><meta charset="UTF-8"><title>我是網頁標題</title></head>
  <body>
      <p id="p1">我是段落一</p>
      <p id="p2" class='red'>我是段落二</p>
  </body>
</html>
'''
sp = BeautifulSoup(html, 'html.parser') # html.parser:Python內建的，解析html原始碼
print(sp.find('p'))
print(sp.find_all('p'))
print(sp.find('p', {'id':'p2', 'class':'red'}))
print(sp.find('p', id='p2', class_= 'red'))
# #------------------------------------------------------
# # test3 : css used select()
# example : datas = sp.select("title")
#           datas = sp.select("#id_name")
#           datas = sp.select(".class_name")
#           datas = sp.select("html head title") # 逐層尋找
# # test4 select get 標籤的屬性名稱 ---------------------------------------
from bs4 import BeautifulSoup
html = '''
<html>
  <head><meta charset="UTF-8"><title>我是網頁標題</title></head>
  <body>
      <img src="http://www.ehappy.tw/python.png">
      <a href="http://www.e-happy.com.tw">超連結</a>
  </body>
</html>
'''
sp = BeautifulSoup(html, 'html.parser')
print(sp.select('img')[0].get('src'))
print(sp.select('a')[0].get('href'))
print(sp.select('img')[0]['src'])
print(sp.select('a')[0]['href'])

# # test5 get 公益彩卷網站最新威力彩中獎號碼c -------------------------------
import requests
from bs4 import BeautifulSoup
url = 'https://www.taiwanlottery.com.tw/'
r = requests.get(url)
sp = BeautifulSoup(r.text, 'html.parser')
# 找到威力彩的區塊
datas = sp.find('div', class_='contents_box02')
# 開獎期數
title = datas.find('span', 'font_black15').text
print('威力彩期數：', title)
# 開獎號碼
nums = datas.find_all('div', class_='ball_tx ball_green')
# 開出順序
print('開出順序：', end=' ')
for i in range(0,6):
    print(nums[i].text, end=' ')
# 大小順序
print('\n大小順序：', end=' ')
for i in range(6,12):
    print(nums[i].text, end=' ')
# 第二區
num = datas.find('div', class_='ball_red').text
print('\n第二區：', num)

# #三 Selenium 模組，瀏覽器自動化操作
# # 有些網頁內容需要在瀏覽器上操作才會的到想要的結果，Selenium 模組就是為了解決這個問題
# # 1. pip install selenium [səˋlinɪəm]
# # 2. 下載 Chrome WebDriver for Create google chrome瀏覽器物件
# #    下載網址 : https://sites.google.com/a/chromium.org/chromedriver/downloads
# #    將chromedriver.exe copy to程式目錄(請Check  chromedriver.exe 與  Chrome使用的版本需一致
# # 3. 匯入selenium can use chrome 瀏覽器物件
# #    from selenium import webdriver
# #    driver = webdriver.Chrome()
# # 4. Selenium Webdriver 的屬性和方法
# #    (1)current_url : 目前網址
# #    (2)page_source : 讀取網頁原始碼
# #    (3)text : 讀取元素內容
# #    (4)size : 元素大小:ex:{'width':250,'height':30}
# #    (5)get_window_position() : get視窗左上角位置
# #    (6)set_window_position() : set視窗左上角位置
# #    (7)maximize_size() : 視窗最大化
# #    (8)get_window_size() : 取得視窗的高度愈寬度
# #    (9)set_window_size() : set視窗的高度愈寬度
# #    (10)click()  : 按單擊紐
# #    (11)close()  : 關閉browser
# #    (12)get(url) : 連結url網址
# #    (13)refresh() : 重新整理畫面
# #    (14)back() : 回上頁
# #    (15)forward() : 下一頁
# #    (16)clear()   : 清除輸入內容
# #    (17)send_keys() : 以鍵盤輸入
# #    (18)submit(): 提交
# #    (19)quit(): close browser & 退出驅動程序
# #
# test1--------------------------------------------------
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('http://www.google.com')
time.sleep( 5000 )
driver.guit()

# 5.尋找網頁元素
# (1) find_element_by_id(id) :            以id尋找符合的元素
# (2) find_element_by_class_name(name)    以class尋找符合的元素
# (3) find_element_by_tag_name(tagname) : 以HTML 標籤尋找符合的元素
# (4) find_element_by_name(name) :        以名稱尋找符合的元素
# (5) find_element_by_link_text(text)   : 以連結文字尋找符合的元素
# (6) find_element_by_partial_link_text(text) : 以部分連結文字尋找符合的元素
# (7) find_element_by_css_selector(selector) : 以CSS 選擇器尋找符合的元素
# (8) find_element_by_xpath() : 以xml的路徑查詢，利用DOM節點找符合的元素
#
# # --------------------------------------------------------------------
# html = '''
# <html>
#    <body>
#         <h1>Welcome</h1>
#         <form id="loginform">
#           <p class="content">Areyousure you want to do this?</p>
#           <a href="continue.html">Continue</a>
#           <a href="cancel,html">Cancel</a>
#           <input name = "username" type="text" />
#           <input name = "password" type="password" />
#          <input name = "continue" type="submit" value="Login"/>
#           <input name = "continue" type="button" value="Clear"/>
#      <\form>
#   </body>
# </html>
# ,,,

#
# # Example
# # (1) heading1 =driver.find_element_by_tag_name('h1')        #1
# # (2) login_form = driver.find_element_by_id('loginform')    #2 to #10
# # (3) content = driver.find_element_by_class_name('content') #3
# # (4) username = driver.find_element_by_name('username')     #6
# # (5) password = driver.find_element_by_name('password')     #7
# # (6) continue_link = driver.find_element_by_link_text('continue')  #4
# # (7) continue_link = driver.find_element_by_partial_link_text('conti') #4
# # (8) use xpath : 1.絕對路徑:[/home]開始 :ex:/home/body/h1 , /home/h1/p ,/home/div/p[2] ([2]指同層地2個p)
# #                 2.相對路徑: 找一個單一獨立的節點，: //h1/div/p , //h1 , //input[@id ='username']
# #                                               //input[@id ='passwd'],input[@class ='rbtn']
# # login_form = driver,find_element_by_xpath("//from[@id='loginform']")
# # username = driver,find_element_by_xpath("//input[@name='username']")
# # PS: Chrome 開發人員工具 : step1.選取要找尋的節點後，滑鼠右鍵 : 選 copy/copy XPth (相對位置) ,copy/copy full XPth (絕對位置)
# # (9) find_element_by_css_selector
# # ex: content = driver.find_element_by_css_selector('.content') # class
# #      content = driver.find_element_by_css_selector('#loginForm')
#
# # ---------------------------------------------------------------------
from selenium import webdriver
# 設定facebook登入資訊
url = 'https://www.facebook.com/'
email='mikaliu5810@gmail.com'
password='chihhualiu'
# 建立瀏覽器物件
driver = webdriver.Chrome()
# 最大化視窗後開啟facebook網站
driver.maximize_window()
driver.get(url)
# 執行自動登入動作
driver.find_element_by_id('email').send_keys(email) #輸入郵件
driver.find_element_by_id('pass').send_keys(password)#輸入密碼
driver.find_element_by_name('login').click()    # 按登入鈕