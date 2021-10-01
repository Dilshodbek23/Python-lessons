class Auto:
    def __init__(self, model, color, transmission, price):
        self.model=model
        self.color=color
        self.transmission=transmission
        self.print=price
        self.mileage=0
        
    def get_info(self):
        return f"{self.color} {self.model} with {self.transmission} transmission  and with {self.mileage} km mileage, for {self.print} USD"
    
    def update_km(self,km):
        self.mileage=km
        
class Auto_showroom:
    def __init__(self, name, adress):
        self.name=name
        self.adress=adress
        self.number_autos=0
        self.autos=[]
        
    def add_autos(self, auto):
        self.autos.append(auto)
        self.number_autos += 1
        
    def get_autos(self):
        return [auto.get_info() for auto in self.autos]
        
    
showroom = Auto_showroom("sunrise", "Tashkent")
auto1 = Auto("BMW", "black", "automatic", 20000)
auto2 = Auto("Audi", "white", "automatic", 18000)
auto3 = Auto("Ravon", "green", "manual", 12000)

showroom.add_autos(auto1)
showroom.add_autos(auto2)
showroom.add_autos(auto3)
        
print(showroom.number_autos)
showroom_autos = showroom.get_autos()
print(showroom_autos)
        
        
        
        
        
        