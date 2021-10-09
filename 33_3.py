with open('pi_million_digits.txt') as fayl:
    pi_million_digits = fayl.read()
 
pi_million_digits = pi_million_digits.replace('\n', '')
pi_million_digits = pi_million_digits.replace(' ', '')

print(type(pi_million_digits))
print(pi_million_digits.find('23011985'))

bdate = '23011985'
print(bdate in pi_million_digits)