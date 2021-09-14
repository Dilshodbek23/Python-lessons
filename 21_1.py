def title(text):
    for i in range(len(text)):
        text[i]=text[i].title()
    return text   
        

list=['ali', 'vali', 'hasan', 'husan']
title(list)
print(list)
