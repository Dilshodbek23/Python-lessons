def year_of_birth(name, age):
    """Function to detect year of birth"""
    print(f"{name.title()} was born in {2021-age}.")
    
a=input("What is your name? ")
b=int(input("How old are you? "))
year_of_birth(a, b)
