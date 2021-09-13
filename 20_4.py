def inform(radius, pi=3.14159):
    infrom_circle={'radius':radius,
                   'diametr':2*radius,
                   'perimetr':2*pi*radius,
                   'area':pi*radius**2}
        
    return infrom_circle

print(inform(9))

