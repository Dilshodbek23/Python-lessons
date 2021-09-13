def prime_num(a,b):
    numbers=[]
    for i in range(a, b+1):
        prime=True
        if i==1:
            prime=False    
        elif i==2:
            prime=True
        else:
            for k in range(2, i):
                if i%k==0:
                    prime=False
        if prime:
            numbers.append(i)
            
    return numbers

print(prime_num(1, 99))
