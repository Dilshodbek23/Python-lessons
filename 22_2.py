def stdents_info(name,surname,**info):
    info['name']=name
    info['surname']=surname
    return info

result=stdents_info('ali','valiev',age=23,ID=23435,faculty='IT')
print(result)
