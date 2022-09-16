'''a = max(1, 4, 6, 7)
b = min(1, 4, 6, 7)
print(a)
print(b)

print(len("aaaaaaaaaaaaaaaaaaaaaa"))


pw = "Sagapo"

guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = (input('insert pw: '))
    guess_count += 1    
    if guess == pw:
        print('access permitted')
        break
else:
    print("acces denied")

a = int(input('Write a number: '))
if a > 10:
    print('Good')
else:
    print("how can you do that?")'''

from audioop import avg


V = list(map(int, input().split()))
sumofV = sum(V)
count = len(V)
M = sumofV/count
print(f"the avarage is {M}")
if M<5:
    print('bocciato')
elif M > 5 and M < 7:
    print ('quite good')
else:
    print('bravo')

    