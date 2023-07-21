import random                                       # random فراخوانی کتابخانه
input("Plz touch ENTER key to start the game")      # برای شروع بازی Enter دریافت
number=random.randint(1,6)                          # تولید یک عدد تصادفی بین 1 و 6
dice=str(number)                       
while number==6:                                    # تا وقتی عدد 6 باشد بازی ادامه دارد
    print("Congradulation! you win a 6.")
    input("Plz touch ENTER again")
    number=random.randint(1,6)
    dice=dice+" => "+str(number)
print("")
print("Oooops! the number is: "+str(number))        # اولین عدد غیر از 6 بازی را تمام می کند
print("Game is over")
if len(dice)>1:
    print("Your number trail was: "+dice)

