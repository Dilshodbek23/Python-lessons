question="Pleas make order: "
question+="(if order is over write 'quit' or 'complete'): "
orders=[]
while True:
    answer=input(question)
    if answer=='quit' or answer=='complete':
        break
    else:
        orders.append(answer)
