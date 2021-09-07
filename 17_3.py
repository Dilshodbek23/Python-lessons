question ="A program that returns the root of the entered number.\n"
question += "Please enter a positive number "
question += "(type 'exit' to stop the program): "

while True:
    value = input(question)
    if value=='Exit':
        break
    if float(value)<0:
        continue
    else:
        root = float(value)**(0.5)
        print(f"{value} ning ildizi {root} ga teng")
