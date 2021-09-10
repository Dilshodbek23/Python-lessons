def even_and_odd(number):
    """Function for detecting even and odd numbers."""
    if number%2:
        print(f"{number} is odd number.")
    else:
        print(f"{number} is even number.")
    
    
even_and_odd(int(input("Please enter a number: ")))
