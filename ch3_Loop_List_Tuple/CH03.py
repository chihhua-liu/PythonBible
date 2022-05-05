
# 1.	List
# # test1 append-----------------------------------------------------------------
# x = [10, 'a', 'b', 10, 10, 'a']
# y = []
# for item in x:
#   y.append(item)     #y += [item]   # 也可以寫成y.append([item])
# print(y)
# x[0]=100
# print(y)
#
# # test 2 ----------------------------
# score = [85, 79, 93]
# print("Chinese is %d " % score[0])
# print("English is %d " % score[1])
# print("Mathematics is %d " % score[2])
#
# # test 3 -----------------------------
# list1 = [["joe","1234"],['mary',"abcd"],['david','5678']]
# print(list1[1])
# print(list1[1][1])
#
# # test 4 --------------------
# List2= [1,"banana",True] # List Index 從0開始
# print('List1_0 =',type(List2[0]))
# print('List1_1 =',type(List2[1]))
# print('List1_2 =',type(List2[2]))

# # test 5 ---------------------------------
# list4 = [1,2,3,4,5,6]
# x =[8,9]
# list41 = list4*2
# print("list4*2 = " ,list41)  # list4*2 =  [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
# list42  = list4[1:4]
# print("list4[1:4] = " ,list42)     # list1[1:4] =  [2, 3, 4]
# list43 = list4[1:4:2]
# print("list4[1:4:2] = " ,list43)   # list1[1:4:2] =  [2, 4]
#
# # # ----- del ---------------------
# list4 = [1,2,3,4,5,6]
# del list4[1:4]    #del
# list44=list4
# print("del list1[1:4] = " ,list44)  # del list1[1:4] =  [1, 5, 6]
# list4 = [1,2,3,4,5,6]
# del list4[1:4:2]
# list45=list4
# print("del list14[1:4:2] = " ,list45) # del list1[1:4:2] =  [1, 3, 5, 6]
#
# ## ----------len() --------------------
# list1 = [["joe","1234"],['mary',"abcd"],['david','5678']]
# print('len(list1) = ',len(list1))           # len(list1) =  3
# # ---min(),max() ----------------------
# list4 = [1,2,3,4,5,6]
# print('min(list1) = ',min(list1))    # min(list1) =  1
# print('max(list1) = ',max(list1))    # max(list1) =  6
# # list.index() -------------------------
# list4 = [1,2,3,4,5,6]
# n=list4.index(3)
# print('list4.index(3) = ',n)    # list1.index(3) =  2
# # list.count() -------------------------------------------------------
# list4 = [1,2,3,4,5,6]
# n=list4.count(3)
# print('list4.count(3) = ',n)    # list1.count(3) =  1  The number of occurrences
# # List.append() is important -------------------
# list4 = [1,2,3,4,5,6]
# list4.append(8)              # The append() method can only add one item at a time,
#                              # and it is added at the end of the data group
# print('list4 = ', list4)     # ist1 =  [1, 2, 3, 4, 5, 6, 8]
# ##--list.extend() -----------------------------------------------------------------------------
# list4 = [1,2,3,4,5,6]
# x=[8,9]
# list4.extend(x)           #The extend() method can add multiple data at the end of the original data at once,    # but these data must be placed in a List data group or Tuple data group.
# print('list4 = ', list4)  #list4 =  [1, 2, 3, 4, 5, 6, 8, 8, 9]
# ## list.insert()---------------------------------------------------------------------------
# list4=[1,2,3,4,5,6]
# list4.insert(3,8)        # The insert() method can insert a piece of data into the specified position,              # and the original data will automatically go back.
# print('list4 = ', list4) # list4 =  [1, 2, 3, 8, 4, 5, 6]
# # #list.pop() , list.remove() , list.reverse() list.sort() --------------------------
# list1=[1,2,3,4,5,6]
# y=list1.pop(2)                       # pop()
# print('list1 pop(2)= ', y,list1)     # list1 pop(2)=  3 [1, 2, 4, 5, 6] pop(index)
# # ## ------------------------------------------------------------------------
# list1=[1,2,3,4,5,6]
# list1.remove(3)                             # remove(index)
# print('list1 = ', list1)                    # list1 =  [1, 2, 4, 5, 6]
# # -------------------------------------------------------------------------
# list1=[1,2,3,4,5,6]
# list1.reverse()                             # reverse()
# print('list1 = ', list1)                    # list1 =  [6, 5, 4, 3, 2, 1]
# # ---------------------------------------------------------------------------------
# list1.sort()                                # sort()
# print('list1 = ', list1)                    # list1 =  [1, 2, 3, 4, 5, 6]
# # -------------------------------------------------------------------------------
# list1=[1,2,3,4,5,6]
# list1+=['John', -10]                        #It's like the extend() method
# print('list1+ = ', list1)                   # list1+ =  [1, 2, 3, 4, 5, 6, 'John', -10]
# # --------------------------------------------------------------------------------
# list1=[1,2,3,4,5,6]
# list1.clear()                               # clear()
# print(list1)                                # []
# # #
# # t5 ---------------------------------------------
my_favorite_colors = ['blue', 'yellow', 'purple']
color = 'purple'
if color in my_favorite_colors:
    print(color + '是我喜歡的顏色')
else:
    print(color + '不是我喜歡的顏色')
# # # t6 Read the value of the list use for look --------------------
x = [10, 'a', 'b', 10, 10, 'a']
for item in x:
    print(item)
# # t7-------- y的內容也會改變，因為它們是「使用」同一個資料組
y=x          # y=[10, 'a', 'b', 10, 10, 'a']
print(y)
x[0]=100     # y=[100, 'a', 'b', 10, 10, 'a']
print(y)    #The content of y will also change because they "use" the same data group
# must use for look------
y = []
for item in x:
  y.append([item])     #y += [item]   # 也可以寫成y.append([item])
print(y)
#---------------------------------------------------------------------------------------------------
# List變數 = rang()
# t1 -----------------------
List1 =range(5)
for s in List1 :
   print(s,end=", ")    # 0, 1, 2, 3, 4,
print("")
print(List1)
# t2 -----------------------#
List2 =range(3,8)
for s in List2 :
   print(s,end=", ")    # 3, 4, 5, 6, 7,
print("")
print(List2)
# t3 -----------------------#
List3 =range(-6,-2)
for s in List3 :
   print(s,end=", ")    # -6, -5, -4, -3,
print("")
# t4 -----------------------#
List4 =range(3,8,1)
for s in List4 :
   print(s,end=", ")    # 3, 4, 5, 6, 7,
print("")
# t5 -----------------------#
List5 =range(3,8,2)
for s in List5 :
  print(s,end=", ")    #3, 5, 7,
print("")
# t6 -----------------------#
List6 =range(8,3,-1)
for s in List6 :
  print(s,end=", ")   #8, 7, 6, 5, 4,
print("")



# 2.For
# t1 --------------------------------------
for i in range(1,10):
   for j in range(1,10):
       product = i * j
       print("%d*%d=%-2d   " % (i, j, product), end="")
      print()
# t2 continue ----------------------------------------
n = int(input("請輸入大樓的樓層數："))
print("本大樓具有的樓層為：")
if(n > 3):
     n += 1
     for i in range(1, n+1):
       if(i==4):
         continue
      print(i, end=" ")
print()
# # t3 break -------------------------------------------
for i in range(1,11):
   if(i==6):
     break
  print(i,end=",")
  print()

# # t4 for..(break).. else--------------------------------
n = int(input("請輸入大於 1 的整數："))
if(n == 2):
   print("2 是質數！")
else:
   for i in range(2, n):
       if(n % i == 0):
           print("%d 不是質數！" % n)
           break
   else:
      print("%d 是質數！" % n)

3.	while
# t1 -----------------------
total = person = score = 0
while (score != -1):
     person += 1
     total += score
     score = int(input("請輸入第 %d 位學生的成績：" % person))
average = total / (person - 1)
print("本班總成績：%d 分，平均成績：%5.2f 分" % (total, average))
# t2 -----------------------
A=0
while A < 5:
    print('Hello!')
    A += 1
A=1
while True:
   print(A)
   if A==10:
       break
   A += 1
# t3 lab 4-1 -----------------------------
sum1 = 0
x = 1
while x < 101 :
 sum1 = sum1 + x
 x += 1
print("1+2+3+...+100=%-5d" % sum1)

4.	tuple
#  tuple : After the definition of the tuple content is completed, it cannot be modified
tuple1 = (1,2,3,4,5)
list1 = list(tuple1)
print(list1)
list1.append(8)
tuple1 =tuple(list1)
print(tuple1)

for i in tuple1:
    print("%d"%(i))
   # a=i
    print(i,type(i))


