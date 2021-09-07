question="enter age: "
answer=0
age=0
while True:
    answer=input(question)
    if answer=='exit' or answer=='quit':
        break
    age=int(answer)
    if age<7:
        print('price for you 2000 soums')
    elif age<18:
        print('price for you 3000 soums')
    elif age<65:
        print('price for you 10000 soums')
    else:
        print('free for you')
    