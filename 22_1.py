def numbers(*x):
    multiplication=1
    for i in x:
        multiplication*=i
    return multiplication


result=numbers(2,3,4,5)
print(result)
