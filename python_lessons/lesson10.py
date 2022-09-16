# Classes

#class EmailClient #I have to capitalize the first letter of every word, "Pascal naming convention"

'''class Point: #I define everything which belongs to this class down
    def move(self):
        print('move')

    def draw(self): #method can have also attribute
        print('draw')

    def __init__(self, x, y): # init = initialize, x and y are extra parameters. This method is used to construct or create an object
        self.x = x # the same of putting point.x = 10 for example
        self.y = y

#point1 = Point() # I'm creating a new object and I store inside Point
#point1.x = 10 #this are attributes
#point1.y = 20
#print(point1.x)
#point1.draw()
#point2 = Point()
#point2.x = 1 
#print(point2.x)

point3 = Point(10,20) #if I use self.x and self.y I have to put inside Point() the values of x and y
point3.x = 11 # I change the point
print(point3.x)'''

class Person:
    def __init__(self, name): #constructor parameter
        self.name = name

    def talk(self): #self is the first parameter of every method
        print(f'Hi,I am {self.name}')

#I create a person object

john = Person("john smith")
john.talk()

bob = Person("bob smith")
bob.talk()

########################################################################################################

class Mammal: #to not repeat a def
    def walk(self):
        print("walk")

class Dog(Mammal):
    def bark(self) :
        print('barkm ')

class Cat(Mammal):
    pass #it use to add this to 'make python happy' because it ask top put under something


dog1 = Dog()
dog1.walk()

