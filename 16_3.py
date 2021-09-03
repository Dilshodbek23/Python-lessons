dost={'ali':None,
      'vali':None,
      'soli':None}
for i in dost.keys():
    for j in range(3):
        if j==0:
            dost[i] = input(f"{i}ning {j+1}-kinosi1: ")
        elif type(dost[i]) == list:
            dost[i].append(input(f"{i}ning {j+1}-kinosi2: "))
        else:
            dost[i] = [dost[i], input(f"{i}ning {j+1}-kinosi3: ")]
for i in dost:
    print(f"{i.title()}ning kinolari:")
    l=dost[i]
    for k in l:
        print(k)     
