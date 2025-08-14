import random
color = ["red","blue","green","yellow"]
guess = input("enter thr color: ")
rd = random.randint(0,4)
p = color[rd]
for i in color :
    if guess == p:
        print("correct")
    else:
        print("try again")
    