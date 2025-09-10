import random
def user_guess(count):
    user=input("guess a number from 0 to 100 : ")
    if (user).isdigit() :
        if int(user)>computer_guess :
            print("you number is greater ")
        elif int(user)<computer_guess:
            print("your number is lesser ")
        else:
            print("you got it")
            print(f"you guessed the number in {count} turns :)")
            quit()
    else:
        print("please enter a valid input ")



computer_guess = random.randint(0,100)
count=0
while True:
    count+=1
    user_guess(count)
    
    
