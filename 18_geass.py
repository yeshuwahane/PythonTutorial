n=13
i=1
print("Number of guesses is  4 : ")
while(i<=4):
    gessnum = int(input("Gess the number :"))
    if gessnum<13: print("your gess is smaller")
    elif gessnum>13: print("you gess is bigger ")
    else:
        print("you won")
        break
    print(4-i,"gess left")
    i = i + 1

if(i>4): print("Game Over")
