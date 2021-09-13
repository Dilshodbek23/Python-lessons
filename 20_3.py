def maxim(a,b,c):
    return max(a, b, c)
        


def maximum(a,b,c):
    m = a
    if a<b:
        m = b
    if c>m:
        m = c    
    return max(a, b, c)
        
    
b=maxim(31,93,6)
f=maximum(-10, 20, 5)
print(b)
print(f)
