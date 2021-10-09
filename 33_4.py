import pickle

with open('pi_million_digits.txt') as fayl:
    pi_million_digits = fayl.read()
 
pi_million_digits = pi_million_digits.replace('\n', '')
pi_million_digits = pi_million_digits.replace(' ', '')
pi_million_digits = float(pi_million_digits)

print(type(pi_million_digits))

with open('info', 'wb') as file:
    pickle.dump(pi_million_digits, file)