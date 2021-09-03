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
shaxslar=[shaxs1,shaxs2,shaxs3]
for i in shaxslar:
    print(f"{i['ismi'].title()} {i['tugy']}-yilda {i['yash']}da tugilgan")
    print(f"hozir u {int(i['hozir'])-int(i['tugy'])}-yoshda")
