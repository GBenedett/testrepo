'''Birth_year = input('Birth year: ')
print(type(Birth_year))
age = 2022 - int(Birth_year)
print(type(age))
print(age)'''

'''weigh_kg = input('weigh: ')
print('your weigh in kg is ' + weigh_kg)

weigh_lbs = float(weigh_kg)*2.204623
print('your weigh in lbs is ' + str(weigh_lbs))'''

'''course = 'Python'
print(course[0:3])'''

first = 'Giacomo'
last = 'Benedetti'
message = first + ' [' + last + '] is a coder'
msg = f'{first} [{last}] is a coder' #dinamic string is better than the one above

print(msg)
print(len(msg)) #tell string's lenght, len is a function
print(msg.upper()) # .method add a method != function
print(msg)
print(msg.find('Giac'))
print(msg.replace('Giacomo','Alessandro'))
print(msg.replace('G','J'))
print('Giacomo' in msg) #return boolean because of in

