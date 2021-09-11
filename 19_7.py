def division(a):
    for i in range(2, 11):
        if not(a%i):
            print(f"{a} is divisible by {i} without a remainder")
        
    
division(20)