def max_number(a, b):
    if a>b:
        print(f"\n{a} is a large number")
    elif b>a:
        print(f"\n{b} is a large number")
    else:
        print("\nThe numbers are the same")
        
num_1=input("Please enter first number: ")
num_2=input("Please enter second number: ")
max_number(num_1, num_2)
