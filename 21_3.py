def title(text):
    grades={}
    for i in range(len(text)):
        grade=input(f"Enter grade for {text[i].title()}: ")
        grades[text[i].title()]=grade
    return grades   
        

list=['ali', 'vali', 'hasan', 'husan']
result=title(list[:])
print(list)
print(result)
