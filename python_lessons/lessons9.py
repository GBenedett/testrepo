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

def square(number):
    return number * number 

result = square(3)  
print(result)
#also
print(square(3))