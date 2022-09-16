'''matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#matrix[0][1] = 20
print(matrix)
#print(matrix[0][1])
for row in matrix:
    for item in row:
        print(item)'''

'''numbers = [5, 2, 1,  7, 4, 5, 5]
numbers2 = numbers.copy() #do a copy of the first list
numbers.append(20) #to add a number at the end
numbers.insert(0, 10) #in this case we add a number in a certain index(first number)
numbers.remove(5)
# numbers.clear() to remove everything
# numbers.pop() remove the last number of the list
print(numbers)
print(numbers.index(10)) #to check if a number exist, tell me the position
#print(numbers.index(50))
print(50 in numbers)
print(numbers.count(5)) #conta quanti numeri ci sono
numbers.sort() #to sort a list
print(numbers)
numbers.reverse() #to sort a list reverse
print(numbers)
print(numbers2) #changing don't affect the second list because is indipendent

#creo una lista di numeri unici, non duplicati
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)'''