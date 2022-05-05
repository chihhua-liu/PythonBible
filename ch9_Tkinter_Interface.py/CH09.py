# 1.Tkinter 圖形使用者介面模組
# import tkinter as tk  # Ctrl+alt+L
#
# win=tk.Tk()               # creat main from
# win.geometry("450x100")   #window widch * length geometry[dʒɪˋɑmətrɪ]
# win.title("This is main from")
# win.mainloop() # 等待觸發模式

# 法1 pack 將元件以矩形物件顯示
# # Test 1 : label --------------------------------------------------------------------
# # width , height , tex t , textariable(元件動態內容的文字變數), bg,fg, font, padx, pady
# # show 1 method : pack() 視為矩形物件顯示
# win=tk.Tk()  # creat main from
# win.geometry("450x100")  #window widch * length
# win.title("This is main from")
# label1=tk.Label(win,width=10,height=3,text="This is label",fg="red",bg='yellow',
#                 font=("新細明體",12),padx=0,pady=0)
# label1.pack();
# win.mainloop() # 等待觸發模式

# Test 2 : Button ----------------------------------------------------------------
# textvariable 3種型態
# (1) tk.StringVar() : 字串 (2) tk.IntVar() 整數 (3) tk.DoubleVar() 浮點數
# 文字變數有兩個方法 : .get()得到文字內容 , .set()設定文字內容
# width , height , text , textariable, bg,fg, font, padx, pady ### command
# import tkinter as tk
# b_check = False
# def click1():
#     global b_check       # 全域變數記得要在function 中加 global
#     if(b_check == True):
#         textvar.set("Button")
#         b_check = False
#     else:
#         textvar.set("我已經被按過了")
#         b_check = True
#
# win=tk.Tk()  # creat main from
# textvar = tk.StringVar()
# button1 = tk.Button(win, textvariable=textvar , command=click1)
# textvar.set("Button")
# button1.pack()
# win.mainloop()

# Test 3 -Label--------------------------------------------------------------------
# import tkinter as tk
# def clickme():
#     global count
#     count+=1
#     labeltext.set("you b me "+str(count)+" times!")
#     if(btntext.get() == "b me!"):
#         btntext.set("Restore original text")
#     else:
#         btntext.set("b me!")
# win = tk.Tk()
# labeltext = tk.StringVar()
# btntext = tk.StringVar()
# count = 0
# label1= tk.Label(win, fg="red", textvariable=labeltext)
# labeltext.set("welcome Tkinter!")
# label1.pack()
# button1= tk.Button(win,textvariable= btntext, command=clickme)
# btntext.set("B me!")
# button1.pack()
# win.mainloop()
# # Test 4 Text --------------------------------------------------------------------
# # width , height ,bg,fg, font, padx, pady,  #text.config : change paramater of seted
# # state (tk.NORMAL,tk.DISABLED), insert (加入狀態(tk.INSEST , tk.END)，字串) win = tk.Tk()
# import tkinter as tk
# win = tk.Tk()
# text = tk.Text(win)
# win.title("tk.INSERT")
# text.insert(tk.INSERT, "Tkinter module is Graphical user interface,\n")
# text.insert(tk.INSERT,"Its function is slightly simple!,\n")
# text.insert(tk.INSERT,"But enough,\n")
# text.insert(tk.END,"不須安裝即可使用")
# text.pack()
# # text.config(state=tk.DISABLED) # 內容不能改
# text.config(state=tk.NORMAL)     # 內容可改
# win.mainloop()
# # Test 5 : tk.Entry(容器，Pama1.Pama2,...) ----------------------------------------
# # width , height , textariable, bg,fg, font, padx, pady , state
# import tkinter as tk
# def checkPW():
#     if(pw.get() == "12345"):
#         msg.set("password is correct")
#     else:
#         msg.set("password is wrong")
# win = tk.Tk()
# pw = tk.StringVar()
# msg = tk.StringVar()
# label1=tk.Label(win, text="Plesae input password:")
# label1.pack()
# entry = tk.Entry(win,textvariable=pw)
# entry.pack()
# button =tk.Button(win,text="login",command=checkPW)
# button.pack()
# lalmsg = tk.Label(win, fg= "red",textvariable=msg)
# lalmsg.pack()
# win.mainloop()

# Test6 Radiobutton & Checkbutton -----------------------------------------------------
# # width , height , text , variable, bg,fg, font, padx, pady , value , command , select
# def choose():
#     msg.set("your favorite ball games :" + choice.get())
# import tkinter as tk
# win = tk.Tk()
# choice = tk.StringVar()
# msg = tk.StringVar()
# label1 = tk.Label(win, text="Select the best report:")
# label1.pack()
# # variable is link textvariable(動態設定元件值的變數)
# # variable 參數指定相同變數明成，則這些選項視為同一組
# item1 = tk.Radiobutton(win,text="football", value="football",variable=choice,command=choose )
# item1.pack()
# item2 = tk.Radiobutton(win,text="basketball", value="basketball",variable=choice,command=choose )
# item2.pack()
# item3 = tk.Radiobutton(win,text="baseball", value="baseball",variable=choice,command=choose )
# item3.pack()
# lalmsg=tk.Label(win,fg="red",textvariable=msg)
# lalmsg.pack()
# item1.select()
# choose()
# win.mainloop()
#
# #  Test7 Checkbutton ----------------------------------------------------------------
# import tkinter as tk
# def choose():
#     str = "你喜歡的球類運動："
#     for i in range(0, len(choice)):
#         if(choice[i].get() == 1):
#             str = str + ball[i] + " "
#     msg.set(str)
#
# win = tk.Tk()
# choice = []
# ball = ["足球", "籃球", "棒球"]
# msg = tk.StringVar()
# label = tk.Label(win, text="選擇喜歡的球類運動：")
# label.pack()
# for i in range(0, len(ball)):
#     tem = tk.IntVar()
#     choice.append(tem)
#     item = tk.Checkbutton(win, text=ball[i], variable=choice[i], command=choose)
#     item.pack()
# lblmsg = tk.Label(win, fg="red", textvariable=msg)
# lblmsg.pack()
# win.mainloop()
#
# 2. Typography : 三種方法 -----------------------------------------
# 法(1) pack: 矩形物件顯示
# import tkinter as tk
# win = tk.Tk()
# button1 = tk.Button(win, text="這是按鈕一", width=20)
# button1.pack()
# button2 = tk.Button(win, text="這是按鈕二", width=20)
# button2.pack()
# button3 = tk.Button(win, text="這是按鈕三", width=20)
# button3.pack()
# button4 = tk.Button(win, text="這是按鈕四", width=20)
# button4.pack()
# win.mainloop()
# #--------------------------------------------------
# import tkinter as tk
# win = tk.Tk()
# button1 = tk.Button(win, text="這是按鈕一", width=20)
# button1.pack(padx=20, pady=5)  # padx & pady 是與容器(win) 的間距
# button2 = tk.Button(win, text="這是按鈕二", width=20)
# button2.pack(padx=20, pady=5)
# button3 = tk.Button(win, text="這是按鈕三", width=20)
# button3.pack(padx=20, pady=5)
# button4 = tk.Button(win, text="這是按鈕四", width=20)
# button4.pack(padx=20, pady=5)
# win.mainloop()
# #---------------------------------------------------
# import tkinter as tk
# win = tk.Tk()
# button1 = tk.Button(win, text="這是按鈕一", width=20)
# button1.pack(padx=20, pady=5, side="right") # side 容器排列位置
# button2 = tk.Button(win, text="這是按鈕二", width=20)
# button2.pack(padx=20, pady=5, side="left")
# button3 = tk.Button(win, text="這是按鈕三", width=20)
# button3.pack(padx=20, pady=5, side="bottom")
# button4 = tk.Button(win, text="這是按鈕四", width=20)
# button4.pack(padx=20, pady=5)
# win.mainloop()
#
# # 法(2)grid : 表格方式安排元件的位置 ------------------------------
# # row,column,padx,pady,rowspan,columnspan,
# # sticky("e"靠右排列，"w"靠左排列,"n"靠上排列,"s"靠下排列)
# import tkinter as tk
# win = tk.Tk()
# button1 = tk.Button(win, text="這是按鈕一", width=20)
# button1.grid(row=0, column=0, padx=5, pady=5)
# button2 = tk.Button(win, text="這是按鈕二", width=20)
# button2.grid(row=0, column=1, padx=5, pady=5)
# button3 = tk.Button(win, text="這是按鈕三", width=20)
# button3.grid(row=0, column=2, padx=5, pady=5)
# button4 = tk.Button(win, text="這是按鈕四", width=20)
# button4.grid(row=1, column=0, padx=5, pady=5)
# button5 = tk.Button(win, text="這是按鈕五", width=20)
# button5.grid(row=1, column=1, padx=5, pady=5)
# button6 = tk.Button(win, text="這是按鈕六", width=20)
# button6.grid(row=1, column=2, padx=5, pady=5)
# win.mainloop()
# #---------------------------------------------------
# import tkinter as tk
# win = tk.Tk()
# button1 = tk.Button(win, text="這是按鈕一", width=20)
# button1.grid(row=0, column=0, padx=5, pady=5)
# button2 = tk.Button(win, text="這是按鈕二", width=20)
# button2.grid(row=0, column=1, padx=5, pady=5, columnspan=2,sticky="e") #columnspan=2 橫跨2個columns
# button3 = tk.Button(win, text="這是按鈕三", width=20)
# button3.grid(row=0, column=3, padx=5, pady=5)
# button4 = tk.Button(win, text="這是按鈕四", width=20)
# button4.grid(row=1, column=0, padx=5, pady=5)
# button5 = tk.Button(win, text="這是按鈕五", width=20)
# button5.grid(row=1, column=1, padx=5, pady=5)
# button6 = tk.Button(win, text="這是按鈕六", width=20)
# button6.grid(row=1, column=2, padx=5, pady=5)
# win.mainloop()

# # 法(3) place : 以x,y 參數設定元件位置，最常用
import tkinter as tk
#x,y,relx,relx,rely,
# anthor(元件位置基準點:9種:center，ne:右上角.nw:左上角,se右下角,sw左下角,n上方中間,s下方中間,e右方中間,w左方中間
import tkinter as tk
win = tk.Tk()
win.geometry("300x100")
label1=tk.Label(win, text="輸入成績：")
label1.place(x=20, y=20)
score = tk.StringVar()
entryUrl = tk.Entry(win, textvariable=score)
entryUrl.place(x=90, y=20)
btnDown = tk.Button(win, text="計算成績")
btnDown.place(x=80, y=50)
win.mainloop()
# -----------------------------------------------------------
import tkinter as tk
win = tk.Tk()
win.geometry("400x150")
button1 = tk.Button(win, text="這是按鈕一", width=20)
button1.place(relx=0.5, rely=0.5, anchor="center")  #relx&rely is整個視窗比例位置左上角0，右下角1
button2 = tk.Button(win, text="這是按鈕二", width=20)
button2.place(relx=0.0, rely=0.0, anchor="nw")
button3 = tk.Button(win, text="這是按鈕三", width=20)
button3.place(relx=0.3, rely=0.3, anchor="w")
win.mainloop()
#
# 3. 視窗區塊(Form)
# import tkinter as tk
# win = tk.Tk()
# frame1 = tk.Frame(win,width=200,height=200)
# frame1.pack()
# label1=tk.Label(frame1, text="標籤一：")
# entry1 = tk.Entry(frame1)
# label1.grid(row=0, column=0)
# entry1.grid(row=0, column=1)
# frame2 = tk.Frame(win)
# frame2.pack()
# button1 = tk.Button(frame2, text="確定")
# button2 = tk.Button(frame2, text="取消")
# button1.grid(row=0, column=0)
# button2.grid(row=0, column=1)
# win.mainloop()
# #----------------------------------------------
# def First():  # 首頁
#     global page
#     page = 0
#     disp_data()
# def Prev():  # 上一頁
#     global page
#     if page > 0:
#         page -= 1
#         disp_data()
# def Next():  # 下一頁
#     global page
#     if page < pagesize:
#         page += 1
#         disp_data()
# def Bottom():  # 最後頁
#     global page
#     page = pagesize
#     disp_data()
# def disp_data():
#   if datas != None:
#       sep1 = tk.Label(frameShow, text="\t", fg="white", width="20", font=("新細明體", 10))
#       label1 = tk.Label(frameShow, text="單字".ljust(30), fg="white", bg="black", width=30, font=("新細明體", 10))
#       label2 = tk.Label(frameShow, text="中文翻譯".ljust(175), fg="white", bg="black", width=80, font=("新細明體", 10))
#       sep1.grid(row=0, column=0, sticky="w")  # 加第一列空白，讓版面美觀些
#       label1.grid(row=1, column=0, sticky="w")
#         label2.grid(row=1, column=1, sticky="w")
#         n = 0  # 資料從索引 0 開始
#         row = 2  # 資料從第二列開始
#         start = page * pagesize + row
#         for eword, cword in datas.items():
#             # 顯示目前 page頁的資料
#             if n >= start and n < start + pagesize:
#                 label1 = tk.Label(frameShow, text="\t" + '{0:30}'.format(eword), fg="blue", font=("新細明體", 10))
#                 label2 = tk.Label(frameShow, text='{0:30}'.format(cword), fg="blue", font=("新細明體", 10))
#                 label1.grid(row=row, column=0, sticky="w")
#                 label2.grid(row=row, column=1, sticky="w")
#                 row += 1
#             n += 1
# # ### 主程式從這裡開始 ###
# import tkinter as tk
# import math
#
# win = tk.Tk()
# win.geometry("500x300")
# win.title("英文單字王")
#
# page, pagesize = 0, 10
# datas = dict()
#
# with open('eword.txt', 'r', encoding='UTF-8-sig') as f:  # 記得” encoding='UTF-8-sig”
#     for line in f:
#         eword, cword = line.rstrip('\n').split(',')
#         datas[eword] = cword
# print("轉換完畢!")
#
# datasize = len(datas)  # 資料筆數
# totpage = math.ceil(datasize / pagesize)  # 總頁數 : math.ceil : get 整數:用完全進位法
#
# # 單字顯示區
# frameShow = tk.Frame(win)
# frameShow.pack()
# labelwords = tk.Label(win, text="")
# labelwords.pack()
#
# frameCommand = tk.Frame(win)  # 翻頁按鈕容器
# frameCommand.pack()
# btnFirst = tk.Button(frameCommand, text="第一頁", width=8, command=First)
# btnPrev = tk.Button(frameCommand, text="上一頁", width=8, command=Prev)
# btnNext = tk.Button(frameCommand, text="下一頁", width=8, command=Next)
# btnBottom = tk.Button(frameCommand, text="最末頁", width=8, command=Bottom)
# btnFirst.grid(row=0, column=0, padx=5, pady=5)
# btnPrev.grid(row=0, column=1, padx=5, pady=5)
# btnNext.grid(row=0, column=2, padx=5, pady=5)
# btnBottom.grid(row=0, column=3, padx=5, pady=5)
#
# First()
# win.mainloop()
#
