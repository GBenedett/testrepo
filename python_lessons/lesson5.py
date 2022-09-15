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



secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print("you won")
        break #to terminate loop