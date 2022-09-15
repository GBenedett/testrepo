'''for item in 'python':
    print(item)

for item in ['giacomo', 'sara', 'paul']:
    print(item)

for item in range(5, 10, 2): #third number is the step
    print(item)

prices = [10, 20, 30]
total =0
for price in prices:
    total += price
print(f'Total {total} CHF')

for x in range(4): #for annidato
    for y in range(3):
        print(f'({x},{y})')'''

numbers = [5, 2, 5, 2, 2]

for item in numbers:
    print(item*"x")

#or

for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)
    
    