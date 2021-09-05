davlatlar = {
    "o'zbekiston":{'poytaxt':"toshkent",
                   'maydon':448978,
                   'aholi':33_000_000,
                   'pul birligi':"so'm"
                   },
    "rossiya":{'poytaxt':"moskva",
                   'maydon':17_098_246,
                   'aholi':144_000_000,
                   'pul birligi':"rubl"
                   },
    "aqsh":{'poytaxt':"vashington",
                   'maydon':9_631_418,
                   'aholi':327_000_000,
                   'pul birligi':"dollar"},
    "malayziya":{'poytaxt':"kuala-lumpur",
                   'maydon':329750,
                   'aholi':25_000_000,
                   'pul birligi':"rinngit"}
    }

k=input("davlatni kiriting: ".lower())
if k not in davlatlar:
    print("Bizda bu davlat haqida ma'lumot yo'q")
else:
    j=davlatlar[k]
    if k == "aqsh":
        k=k.upper()
    else:
        k=k.title()
    print(f"\n{k}ning poytaxti {j['poytaxt'].title()}"
          f"\nHududi: {j['maydon']} kv.km"
          f"\nAholisi: {j['aholi']} "
          f"\nPul birligi: {j['pul birligi']}")
