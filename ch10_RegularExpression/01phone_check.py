def isTaiwanPhone(str):
    if len(str) != 11:
          return False
    for i in range(0, 11):
          if i==4:
             if str[4] != '-':
                 return False
          else:
             if str[i].isdecimal() == False:
                 return False
    return True

print("0937-123456 is taiwan cell phone",isTaiwanPhone('0937-123456'))
print("02-12345678 is taiwan cell phone",isTaiwanPhone('02-12345678'))

# used regular expression : in "http://pythex.org" 可以測試正規表達式結果是否正確
# (1) [0123456789]+  = [0.9]+  = [\d]+ : 表示數字所組成的集合
# (2) a.c 表示a, c 中間有一個字
# (3) ^ab 表示輸入列是以ab 開頭
# (4) 23$ 表示輸入列以23結束
# (5) ac* 表示前一項目c 出現0次或無限多次
# (6) ac+ 表示前一項目c 可以出現1次或無限多次
# (7) ac? 表示前一項目?c 可以出現0次或1次
# (8) [abc] 表示符合a or b or c 的任何字元
# (9) [a~z]
# (10) \ 代表後面的字當一般字元處理: a\+ ='a+'
# (11) {m} 表示前一項目出現m 次 : a{2} a出現2次
# (12) {m,} 表示前一項目最少出現m 次,最多無限次
# (13) {m,n} 表示前一項目最少出現m 次,最多n次
# (14) \d  = [0123456789] =[0-9]
# (15) [^a-d] 除了a,b,c,d 以外的其他所有字元
# (16) \D 非數字字元 = [^0-9]
# (17) \n 換列字元
# (18) \r 回列首
# (19) \t tab 字元
# (20) \s =[\r\t\n\f] \f換頁
# (21) \S =[^\r\t\n\f]
# (22) \w =[0-9a-zA-Z]
# (23) \W =[^0-9a-zA-Z]\