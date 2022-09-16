#function
# def = define

'''def greet_user(name, surname): #everytime we put : we are defining a block. Name is a PARAMETRE, if there is one, I have to declare an argument
    print(f'hi {name} {surname}') #parametre are positional depending
    print('welcome aboard')

print("start")
greet_user("jack","benedetti") #show message upper, I called the function
greet_user(surname='benelli', name='john') #in this case there are keyword so they are indipendent by the order
#calc_cost(total = 50, shipping = 5, discount = 0.1) #more readable
print("finish")

#key argument must be put after positional argument'''

'''def square(number):
    return number * number #if I don't put return none it will be the answer

result = square(3)  
print(result)
#also
print(square(3))

try:
    age = int(input('age: '))
    income = 20000
    risk = income/age
    print(age)
    print(risk)
except ValueError:
    print('invalid value') #instead crashing print this line
except ZeroDivisionError:
    print('invalid value')'''

