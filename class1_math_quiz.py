import time
import random

start_time = time.time()    

def start_quiz():
    mode = input("enter the mode *easy/moderate/hard : ")
    mode=mode.strip().lower()
    q=int(input("enter no of questions to solve : "))
    print("NOTE :- always round your values upto two decimal digits ")

    right=0
    wrong=0
    count=0
    for _ in range(q):
        if mode=="easy":
            x=random.randint(0,100)
            y=random.randint(0,100)
        elif mode=="moderate":
            x=random.randint(101,1000)
            y=random.randint(101,1000) 
        else:
            x=random.randint(1001,10000)
            y=random.randint(1001,10000)

        opr=["+","-","*","/"]
        opr_length=len(opr)
        random_value=random.randint(0,(opr_length-1))

        count+=1
        
        ans=input(f"Question #{count} : {x} {opr[random_value]} {y} = ")
        print("correct answer is : ",round(eval(str(x)+opr[random_value]+str(y)),2))
        if(round(float(ans),2)==round(eval(str(x)+opr[random_value]+str(y)),2)):

            right+=1
        else:
         wrong+=1
    print(f"you tried {count} question \ncorrect : {right} \nwrong : {wrong}")

start_quiz()

end_time= time.time()
total_time=end_time-start_time
print(f"total time taken : {round(total_time,2)}sec.")

