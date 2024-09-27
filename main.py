'''
1 for snake
-1 for water
0 for gun
'''


computer = -1
youStr = input("Enter a number of your choice: ")
youDict = {"Snake" : 1,
           "Water" : -1,
           "Gun" : 0}
reverseDict = {1 : "Snake",
           -1 : "Water",
           0 : "Gun"}

you = youDict[youStr]

print(f"you chose {reverseDict[you]}\n Computer chose {reverseDict[computer]}")

if computer == you:
    print("Its a draw")
else:
    
    if computer == -1 and youStr == 1:
        print("You win!!")
    elif computer == -1 and youStr == 0:
        print("You lose!!")
    elif computer == 1 and youStr == -1:
        print("You lose!!")
    elif computer == 1 and youStr == 0:
        print("You win!!")
    elif computer == 0 and youStr == -1:
        print("You lose!!")
    elif computer == 0 and youStr == 1:
        print("You Win!!")
    elif computer == -1 and youStr == 0:
        print("You lose!!")
    else:
        print("Something went wrong")