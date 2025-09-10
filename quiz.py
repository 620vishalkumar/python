while True:
    
    do_you=input("do you want to play this quiz : ")

    right=0
    wrong=0

    if((do_you.strip()).lower()!="yes"):
        quit()
    else:
        print("well done here is your quiz!")
    gpu=input("GPU stands for : ")
    if (gpu.strip()).lower() !="graphics processing unit":
        wrong+=1
        print(f"{wrong} wrong answers")
    else:
        right+=1
        print(f"{right} right answers!") 
    cpu=input("CPU stands for : ")
    if(cpu.strip()).lower() !="central processing unit":
        wrong+=1
        print(f"{wrong} wrong answers!")
    else:
        right+=1
        print(f"{right} right answers!")

    psu=input("PSU stands for : ")
    if(psu.strip()).lower() !="power supply unit":
        wrong+=1
        print(f"{wrong} wrong answers!")
    else:
        right+=1
        print(f"{right} right answers!")
    
    ram=input("RAM stands for : ")
    if(ram.strip()).lower() !="random access memory":
        wrong+=1
        print(f"{wrong} wrong answers!")
    else:
        right+=1
        print(f"{right} right answers!")
    os=input("OS stands for : ")
    if(os.strip()).lower() !="operating system":
        wrong+=1
        print(f"{wrong} wrong answers!")
    else:
        right+=1
        print(f"{right} right answers!")
    print(end='\n\n')
    print("hey buddy here is your result!",end='\n\n')
    print(f"total quiz you tried : {wrong+right}")
    print(f"total right answers : {right}")
    print(f"total wrong answers : {wrong}")
    print(end="\n\nq")

