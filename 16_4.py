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
for i,j in davlatlar.items():
    if i == "aqsh":
        i=i.upper()
    else:
        i=i.title()
    print(f"\n{i}ning poytaxti {j['poytaxt'].title()}"
          f"\nHududi: {j['maydon']} kv.km"
          f"\nAholisi: {j['aholi']} "
          f"\nPul birligi: {j['pul birligi']}")
