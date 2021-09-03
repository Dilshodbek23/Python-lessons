shaxs1={'ismi':'navoi',
        'tugy':1982,
        'hozir':2021,
        'yash':'tosh'
        }
shaxs2={'ismi':'bobur',
        'tugy':1980,
        'hozir':2021,
        'yash':'shosh'
        }
shaxs3={'ismi':'darvesh',
        'tugy':1992,
        'hozir':2021,
        'yash':'bosh'
        }
shaxs1['asarlar']=['xamsa','xamsa2']
shaxs2['asarlar']=['boburnoma','boburnoma2']
shaxs3['asarlar']=['kitob','kitob2']
    
shaxslar=[shaxs1,shaxs2,shaxs3]
for i in shaxslar:
    print(f"{i['ismi'].title()}ning asarlari:")
    for k in i['asarlar']:
        print(k)
    print()

