import random as r
print("Let's play to find the number you think about.")
answer=1
while answer:
    num_com = r.randint(1, 10)
    print("I came up with a number from 1 to 10. Can you find it?:")
    i=0
    while True:
        num=int(input('>>'))
        if num>num_com:
            print("Error. My number is less than you wrote. Try again: ")
            i+=1
        elif num<num_com:
            print("Error. My number is greater than you wrote.Try again: ")
            i+=1
        elif num==num_com:
            i+=1
            print(f"Found! I thought about number {num_com}. You found after {i} try. Congratulations.")
            break
    print("Think of a number from 1 to 10. I'll try to find it.")
    x=input("If you think of a number, press any button.")
    a=1
    b=10
    
    k=0
    while True:
        ran_num = r.randint(a, b)
        user_number=input(f"You thought about the number {ran_num}: true (T), my number is greater (+), my number is less (-)")
        if user_number=='+':
            k+=1
            a=ran_num+1
        elif user_number=='-':
            k+=1
            b=ran_num-1
        elif user_number=="T":
            k+=1
            print(f"I found your number after {k} tries.")    
            break
    if i<k:
        print(f"You found after {i} try and win!")
    elif i>k:
        print(f"You found after {i} try and lost!")
        
    elif i==k:
        print(f"Draw! We both found after {i} tries.")
    answer=int(input("Will you play again? yes(1)/no(0): "))
print("game over")
