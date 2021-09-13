def num(a):
    list=[1]
    res1=0
    res2=1
    for i in range(a-1):
        res1, res2 = res2, res1+res2
        list.append(res2)
            
    return list

print(num(20))


def fibonacci(n):
    sonlar = []
    for x in range(n):
        if x==0 or x==1:
            sonlar.append(1)        
        else:
            sonlar.append(sonlar[x-1]+sonlar[x-2])
    return sonlar

print(fibonacci(20))