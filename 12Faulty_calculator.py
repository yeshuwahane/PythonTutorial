print("Welcome to calculation machine ")
print("Select \n 1.Addition \n 2.Subtraction \n 3.Divide \n 4.Multiply")
ch = input()

if ch=="1":
    print("Enter a number to add :")
    add= int (input())
    #print("Enter second number to add   :")
    #add1 = int (input())
    if add==56:
        print("Enter second number")
        add1= int(input())
        if add1==9:
            print("Answer is 77")
        else:
            print(add+add1)
    elif add==9:
        print("Enter second number to add")
        add1= int(input())
        if add1==56:
            print("Answer is 77")
        else:
            print(add+add1)
    else:
        print("Enter second number to add")
        add1= int(input())
        print(add+add1)
elif ch=="2":
    print("Enter a number to subtract :")
    sub = int(input())
    print("Enter a second number to subtract ")
    sub1 = int(input())
    print(sub-sub1)
elif ch=="3":
    print("Enter a number to divide :")
    div= int(input())
    if div==56:
        print("Enter second number to divide :")
        div1= int(input())
        if div1==6:
            print("Answer is 4")
        else:
            print(div/div1)
    else:
        print("Enter second number to divide : ")
        div1= int(input())
        print(div/div1)
elif ch=="4":
    print("Enter a number to multiply : ")
    mul= int(input())
    if mul==45:
        print("Enter second number to multiply : ")
        mul1= int(input())
        if mul1==3:
            print("Answer is : 555")
        else:
            print(mul*mul1)
    elif mul==3:
        print("Enter second number to multiply : ")
        mul1= int(input())
        if mul1==45:
            print("Answer is :  555")
        else:
            print(mul*mul1)
    else:
        print("Enter second number :")
        mul1= int(input())
        print(mul*mul1)
else:
    print("invalid")
