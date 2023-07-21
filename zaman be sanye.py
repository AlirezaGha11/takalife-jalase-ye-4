hh=int(input("Plz enter hour (0<hour<24): "))                 # دریافت مقدار ساعت 
while hh>24 or hh<0:                                          # تا وقتی که مقدار ساعت غیر مجاز باشد مجددا مقدار ساعت را دریافت میکند
    print("Invalid hour! hour must be between 0 and 24")
    hh=int(input("Plz enter hour (0<hour<24): "))
mm=int(input("Plz enter minute (0<minute<60): "))             # دریافت مقدار دقیقه
while mm>60 or mm<0:                                          # تا وقتی مقدار دقیقه غیر مجاز هست دوباره مقدار دقیقه را دریافت میکند
    print("Invalid minute! minute must be between 0 and 60")  
    mm=int(input("Plz enter minute (0<minute<60): "))   
ss=int(input("Plz enter second (0<second<60): "))             # دریافت مقدار ثانیه 
while ss>60 or ss<0:                                          # تا وقتی مقدار ثانیه غیر مجاز هست دوباره مقدار ثانیه را دریافت میکند
    print("Invalid second! second must be between 0 and 60")
    ss=int(input("Plz enter second (0<second<60): "))
if hh<10:
    enteredtime="0"+str(hh)+":"
else: enteredtime=str(hh)+":"
if mm<10:
    enteredtime=enteredtime+"0"+str(mm)+":"
else: enteredtime=enteredtime+str(mm)+":"
if ss<10:
    enteredtime=enteredtime+"0"+str(ss)
else: enteredtime=enteredtime+str(ss)
print("The Time you entered is ===> "+enteredtime)             # چاپ زمان با فرمت ساعت
number=hh*3600+mm*60+ss                                        # تبدیل زمان به ثانیه
print("")
print("")
print("The time is equal to number in seconds: "+ str(number)) # چاپ ثانیه