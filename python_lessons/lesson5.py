'''Weight = input('Weight: ')

K_L = input('(K)g or (L)bs? ')

if K_L.upper() == 'K': #convert everything in capital
    w = float(Weight)*2.2
    print(str(w) + ' Lbs')

elif K_L.upper() == 'L': #
    w = float(Weight)*0.45
    print(f"you are {w} Kg")
else:
    print("you have to chose between (K)g and (L)bs")'''

"""i = 1
while i <= 5:
    print('*'*i)
    i = i+1
print("done")"""



'''secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print("you won")
        break #to terminate loop'''

command = ""
started = False

while True: #until the block is true the command will be execute
    command = input('> ').lower() # to not repeat lower everytime
    if command == 'start':
        if started:
            print("car is already started")
        else:
            started = True
            print("Car started... Ready to go!")
    elif command == 'stop':
        if not started:
            print('Car is already stopped')
        else:
            started = False
            print("Car stopped")

    elif command == 'help':
        print('''
start - to start the car
stop - to stop the car
quit - to quit''')
    elif command == 'quit':
        break
    else:
       print("I don't understand that")
