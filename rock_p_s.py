import random


count=0
win=0
draw=0
lose=0
while True:
    computer = random.randint(0,2)
    li = ["rock","paper","scissors"]

    user=input("choose rock/paper/scissors or 'Q to quit' : ")
    user = user.strip().lower()
    
    
    if(user=="q" or user=="quit"):
        print(f"you played {count} times and won {win} turns and draw {draw} times and lose {lose} times")
        quit()
    
    if user in li:
        count+=1
        if(user=="rock") and (li[computer]=="scissors"):
            print(f"computer choosed : {li[computer]} ")
            print("you won this turn!")
            win+=1
        elif (user=="paper") and (li[computer]=="rock"):
            print(f"computer choosed : {li[computer]} ")
            print("you won this turn!")
            win+=1
        elif (user=="scissors") and (li[computer]=="paper"):
            print(f"computer choosed : {li[computer]} ")
            print("you won this turn!")
            win+=1
        elif(user==li[computer]):
            print(f"computer choosed : {li[computer]} ")
            print("omg this is draw!")
            draw+=1
        else:
            print(f"computer choosed : {li[computer]} ")
            print("you lose this turn!")
            lose+=1
    else:
        print("enter a valid input")




