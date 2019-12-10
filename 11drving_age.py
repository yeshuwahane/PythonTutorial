print("Enter your age to check if you can drive or not :  ")
age = int(input())

if age>7&age<80:
    print("You can drive ")

elif age<7:
    print("You are too small to drive")

else age>80:
    print("sorry you too old to drive")
    
