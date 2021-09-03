menu = {
        'osh':20000,
        "lag'mon":22000,
        'non':4000,
        'choy':5000,
        'shashlik':12000,
        'somsa':6000,
        'tabaka':15000
        }
taom=[]
k=0
for i in range(3):
    taom.append(input(f"{i+1} taomni kiriting: ").lower())
for i in taom:
    narx=menu.get(i)
    if narx==None:
        print(f"bizda {i} taomi yo'q")
    else:
        print(f"{i}ning narxi {narx} so\'m")
        k += narx
print(f"jami {k} so\'m bo\'ladi")
