def text_t(a):
    b = []
    for i in a:
        b.append(i.title())
    return b
        
list = ['jkl', ';lkjh', 'yuioj']
print(text_t(list))
