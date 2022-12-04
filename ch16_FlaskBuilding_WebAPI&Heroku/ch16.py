# 補充 Python 中使用 xml.etree.ElementTree 模組來讀取與寫入 XML 格式的資料與檔案。
# 1. ElementTree(tag)，其中tag表示根節點，初始化一個ElementTree對象。
# 2. Element(tag, attrib={}, **extra)函數用來構造XML的一個根節點，其中tag表示根節點的名稱，attrib是一個可選項，表示節點的屬性。
# 3. SubElement(parent, tag, attrib={}, **extra)用來構造一個已經存在的節點的子節點
# 4. Element.text和SubElement.text表示element對象的額外的內容屬性，Element.tag和Element.attrib分別表示element對象的標籤和屬性。
# 5. ElementTree.write(file, encoding='us-ascii', xml_declaration=None, default_namespace=None, method='xml')，函數新建一個XML文件，並且將節點數數據寫入XML文件中。
# #encoding=utf-8
# import xml.etree.ElementTree as ET
# #新建xml文件 1
# def buildNewsXmlFile():
#         #设置一个新节点，并设置其标签为root
#         root = ET.Element("root")
#
#         #在root下新建两个子节点,设置其名称分别为sina和chinabyte
#         sina = ET.SubElement(root, "sina")
#         chinabyte = ET.SubElement(root, "chinabyte")
#
#         #在sina下新建两个子节点，设置其节点名称分别为number和first
#         sina_number = ET.SubElement(sina, "number")
#         sina_number.text = "1"
#         sina_first = ET.SubElement(sina, "first")
#         sina_first.text = "http://roll.tech.sina.com.cn/internet_all/index_1.shtml"
#
#         #在chinabyte下新建两个子节点，设置其节点名称为number和first
#         chinabyte_number = ET.SubElement(chinabyte, "number")
#         chinabyte_number.text = "1"
#         chinabyte_first = ET.SubElement(chinabyte, "first")
#         chinabyte_first.text = "http://www.chinabyte.com/more/124566.shtml"
#
#         #将节点数信息保存在ElementTree中，并且保存为XML格式文件
#         tree = ET.ElementTree(root)
#         tree.write("urlfile1.xml")
#
# if __name__ == '__main__':
#     buildNewsXmlFile()
#---------------------------------------------------------------------------------
# #新建xml文件 2
# import xml.etree.ElementTree as ET
# def buildNewXmlFGile():
#         data = ET.Element("data")
#         #----------------------------------------------------
#         myattributes = {"name": "Liechtenstein"}
#         countryname = ET.SubElement(data,"country", attrib=myattributes)
#         # 1
#         rank = ET.SubElement(countryname,"rank")
#         rank.text ="1"
#         #2
#         year = ET.SubElement(countryname, "year")
#         year.text = "2008"
#         #3
#         gdppc = ET.SubElement(countryname, "gdppc")
#         gdppc.text = "141100"
#         #4
#         myattributes = {"direction": "E"}
#         neighborname = ET.SubElement(countryname,'neighbor name="Austria"', attrib=myattributes)
#
#         myattributes = {"direction": "W"}
#         neighborname = ET.SubElement(countryname, 'neighbor name="Switzerland"', attrib=myattributes)
#         #---------------------------------------------------------------------------------------------
#         myattributes = {"name": "Singapore"}
#         countryname = ET.SubElement(data, "country", attrib=myattributes)
#         # 1
#         rank = ET.SubElement(countryname, "rank")
#         rank.text = "4"
#         # 2
#         year = ET.SubElement(countryname, "year")
#         year.text = "2011"
#         # 3
#         gdppc = ET.SubElement(countryname, "gdppc")
#         gdppc.text = "59900"
#         # 4
#         myattributes = {"direction": "N"}
#         neighborname = ET.SubElement(countryname, 'neighbor name="Malaysia"', attrib=myattributes)
#         # --------------------------------------------------------------------------------------------
#         myattributes = {"name": "Panama"}
#         countryname = ET.SubElement(data, "country", attrib=myattributes)
#         # 1
#         rank = ET.SubElement(countryname, "rank")
#         rank.text = "68"
#         # 2
#         year = ET.SubElement(countryname, "year")
#         year.text = "2012"
#         # 3
#         gdppc = ET.SubElement(countryname, "gdppc")
#         gdppc.text = "13600"
#         # 4
#         myattributes = {"direction": "W"}
#         neighborname = ET.SubElement(countryname, 'neighbor name="Costa Rica"', attrib=myattributes)
#         myattributes = {"direction": "E"}
#         neighborname = ET.SubElement(countryname, 'neighbor name="Colombia"', attrib=myattributes)
#         #---------------------------------------------------------------------------------------------
#         tree = ET.ElementTree(data)
#         tree.write("urlfile.xml")
# if __name__ == "__main__":
#         buildNewXmlFGile()

# XML 檔案 country_data.xml 內容如下：
# <?xml version="1.0"?>
# <data>
#     <country name="Liechtenstein">
#         <rank>1</rank>
#         <year>2008</year>
#         <gdppc>141100</gdppc>
#         <neighbor name="Austria" direction="E"/>
#         <neighbor name="Switzerland" direction="W"/>
#     </country>
#     <country name="Singapore">
#         <rank>4</rank>
#         <year>2011</year>
#         <gdppc>59900</gdppc>
#         <neighbor name="Malaysia" direction="N"/>
#     </country>
#     <country name="Panama">
#         <rank>68</rank>
#         <year>2011</year>
#         <gdppc>13600</gdppc>
#         <neighbor name="Costa Rica" direction="W"/>
#         <neighbor name="Colombia" direction="E"/>
#     </country>
# </data>
# 1. 解析xml文件的代碼----------------
# import xml.etree.ElementTree as ET
# tree = ET.parse('urlfile.xml')
# root = tree.getroot()
# print(root.tag)
# print(root.attrib)
# print(root[2][1].text)
#
# for neighbor in root.iter('neighbor'):
#     print(neighbor.attrib)
#
# print('---------------------------------------')
# for country in root.findall('country'):
#     rank = country.find('rank').text
#     name = country.get('name')
#     print(name, rank)
# print('---------------------------------------')
# for rank in root.iter('rank'):
#     new_rank = int(rank.text) + 1
#     rank.text = str(new_rank)
#     rank.set('updated', 'yes')
# tree.write('output.xml')
# print('----------------------------------------')
# for country in root.findall('country'):
#     # using root.findall() to avoid removal during traversal
#     rank = int(country.find('rank').text)
#     print(rank)
#     if rank > 50:
#         root.remove(country)
#
# tree.write('output.xml')
#------------------------------------------------------------------------

#------------------------------------------------------------------------
# Flask 非常適合開發Web API
# 1.縣市氣象公開資料
# Step1. https://pweb.cwb.gov.te/CWBMEMBER2  申請會員
# Step2. https://opendata.cwb.gov.tw/index 登入會員
# Step3. 登入後: 取得授權碼 ex: CWB-27FD8A8C-5A78-482A-BCBA-D2AE855B4215
# Demo 01 解析新北天氣 --------------------------------------------------------
# import requests
#
# try:
#     import xml.etree.cElementTree as et
# except ImportError:
#     import xml.etree.ElementTree as et      # 分析XML 結構模組
#
# user_key = "CWB-27FD8A8C-5A78-482A-BCBA-D2AE855B4215"
# doc_name = "F-C0032-001"
#
# api_link = "https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/%s?Authorization=%s&format=XML" % (doc_name, user_key)  # 氣象局Web API
# # api_link = "https://opendata.cwb.gov.tw/opendataapi?dataid=%s&authorizationkey=%s" % (doc_name,user_key)
# print(api_link)
# report = requests.get(api_link).text
# print(report)   # 天氣預測資料
# xml_namespace = "{urn:cwb:gov:tw:cwbcommon:0.1}"
# root = et.fromstring(report)
# print('root =',root)
# dataset = root.find(xml_namespace + 'dataset')
# locations_info = dataset.findall(xml_namespace + 'location')
# ## 取得 <location> Elements,每個 location 就表示一個縣市資料
# location = '新北市'
# target_idx = -1
# for idx,ele in enumerate(locations_info):
#    locationName = ele[0].text # 取得縣市名
#    if locationName == location:  #找到要查詢的縣市
#        target_idx = idx
#        break
# if target_idx != -1:
#    show = ''
#    tlist = ['天氣狀況', '最高溫', '最低溫', '舒適度', '降雨機率']
#    for i in range(5):
#        element = locations_info[target_idx][i+1]  #取得weatherElement
#        timeblock = element[1] # 取出目前時間點的資料
#        data = timeblock[2][0].text
#        show = show + tlist[i] + '：' + data + '\n'
#    print(show)
# else:
#    print('無此縣市資料！')
#----------------------------------
# from flask import Flask  #(page: 16.2 部屬web API 到Heroku)
# import xml.etree.ElementTree as ET
# app = Flask(__name__)
# import requests
#
# try:
#     import xml.etree.cElementTree as et
# except ImportError:
#     import xml.etree.ElementTree as et
#
#
# @app.route('/weather/<city>')
# def weather(city):
#     user_key = "CWB-27FD8A8C-5A78-482A-BCBA-D2AE855B4215"
#     doc_name = "F-C0032-001"
#
#     cities = ["臺北", "新北", "桃園", "臺中", "臺南", "高雄", "基隆", "新竹", "嘉義"]  # 市
#     counties = ["苗栗", "彰化", "南投", "雲林", "屏東", "宜蘭", "花蓮", "臺東", "澎湖", "金門", "連江"]  # 縣
#
#     showdata = ''
#     flagcity = False  # 檢查是否為縣市名稱
#     city = city.replace('台', '臺')  # 氣象局資料使用「臺」
#     if city in cities:  # 加上「市」
#         city += '市'
#         flagcity = True
#     elif city in counties:  # 加上「縣」
#         city += '縣'
#         flagcity = True
#
#     if flagcity:  # 是縣市名稱
#         api_link = "https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/%s?Authorization=%s&format=XML" % (doc_name, user_key)  # 氣象局Web API
#         report = requests.get(api_link).text
#         xml_namespace = "{urn:cwb:gov:tw:cwbcommon:0.1}"
#         root = et.fromstring(report)
#         print("root =",root)
#         dataset = root.find(xml_namespace + 'dataset')
#         locations_info = dataset.findall(xml_namespace + 'location')
#         target_idx = -1
#         # 取得 <location> Elements,每個 location 就表示一個縣市資料
#         for idx, ele in enumerate(locations_info):
#             locationName = ele[0].text  # 取得縣市名
#             if locationName == city:
#                 target_idx = idx
#                 break
#                 # 挑選出目前想要 location 的氣象資料
#         tlist = ['天氣狀況', '最高溫', '最低溫', '舒適度', '降雨機率']
#         showdata = '{'
#         for i in range(len(tlist)):
#             element = locations_info[target_idx][i + 1]  # 取出 Wx (氣象描述)
#             timeblock = element[1]  # 取出目前時間點的資料
#             data = timeblock[2][0].text
#             showdata = showdata + '"' + tlist[i] + '":"' + data + '", '
#         showdata = showdata[:-2] + "}"  # 移除最後一個換行
#     else:
#         showdata = '縣市名稱不存在！'
#     return showdata
# # #--------------------------------------
# # Demo 02 縣市天氣資料 Web API
# if __name__ == '__main__':
#    app.run()
#--------------------------------------------------------------------------
# Demo3 部屬Web API in google,microsoft Azure ， Amazom ，Heroku 提供 PaaS (platform as a Service)#
# Step1 install Git 版本管理軟體 : https://git-scm.com/
#------------------------------------------------------------------------------
# from tkinter import *
# from tkinter.ttk import *
#
# def selected(event):
#     labelVar.set(cbVar.get())
#
# win = Tk()
# win.title('最喜歡的運動')
# win.geometry('300x160')
#
# cbVar = StringVar()
# cb = Combobox(win, textvariable=cbVar)
# cb['value'] = ("籃球","排球","足球","其他")  #設定選項
# cb.current(0)  #預設第一個選項
# cb.bind('<<ComboboxSelected>>', selected)  #設定選取選項後執行的程式
# cb.place(x=70, y=15)
#
# labelVar = StringVar()
# labelShow = Label(win, textvariable=labelVar)
# labelVar.set(cbVar.get())
# labelShow.place(x=80, y=120)
#
# win.mainloop()

# 運用16.2 部屬好的API 將天氣資料顯示在標籤員簡忠

from tkinter import *
from tkinter.ttk import *
import requests

def showWeather(event):  #下拉選單選取選項後執行的程式
    city = cbVar.get()  #使用者選取的選項
    if city != '請選擇：':  #選擇縣市
        report = requests.get('https://weathflaskmika.herokuapp.com/weather/' + city).text  #取得Web API資料
        print(report)
        print("------------------------------")
        jsondata = eval(report)  #轉換為字典
        showdata = city + ' 天氣資料：\n'
        showdata += '天氣狀況：' + jsondata['天氣狀況'] + '\n'
        showdata += '最高溫：' + jsondata['最高溫'] + '\n'
        showdata += '最低溫：' + jsondata['最低溫'] + '\n'
        showdata += '舒適度：' + jsondata['舒適度'] + '\n'
        showdata += '降雨機率：' + jsondata['降雨機率'] + '\n'
        labelVar.set(showdata)
    else:
        labelVar.set('請選擇縣市！')

win = Tk()
win.title('縣市天氣資料')
win.geometry('300x350')

cbVar = StringVar()
cb = Combobox(win, textvariable=cbVar)  #下拉選單元件
cb['value'] = ("請選擇：","臺北","新北","桃園","臺中","臺南","高雄","基隆","新竹","嘉義","苗栗","彰化","南投","雲林","嘉義","屏東","宜蘭","花蓮","臺東","澎湖","金門","連江" )  #設定選項
cb.current(0)  #預設第一個選項
cb.bind('<<ComboboxSelected>>', showWeather)  #設定選取選項後執行的程式
cb.place(x=70, y=15)

labelVar = StringVar()
labelShow = Label(win, foreground='red', justify='left', textvariable=labelVar)  #標籤元件
labelVar.set('尚未選擇縣市！')
labelShow.place(x=80, y=220)

win.mainloop()

