#Tuples
#they can't be modifyed

from operator import xor


'''numbers = (1, 2, 3,3) #with () is a tuples
print(numbers[0])
print(numbers.count(3))

coordinates = (1, 2, 3)
#x = coordinates[0] 
#y = coordinates[1]
#z = coordinates[2]

x, y, z = coordinates #the same above, it can be used also for list '''

#Dictionaries

'''customer = {
    'name': 'Giacomo',
    'age': 24,
    'is verified': True
} #every item has to be unique
customer['name'] ='Jack' #change the name
customer["birthdate"] = "may 28 1998" #add information
print(customer['name'])
print(customer['birthdate'])

phone_number = input('Phone: ')

digits_mapping = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four'
        }
output = ''
for ch in phone_number:
    output += digits_mapping.get(ch, '!') + ' ' #to get things from the dictionarie
print(output)'''

message =input('>')
words = message.split(' ')#every space is a criteria of separation
print(words)