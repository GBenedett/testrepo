"""# Packages, is what grouping modules
import ecommerce.shipping
ecommerce.shipping.calc_shipping()"""

import random #is a random model builted in python #random is a model

'''for i in range(3):
    # print(random.randint(10, 20))    #I create an object with is model
    print(random.random())


members = ['john','mary','bob', 'mosh']
leader = random.choice(members)
print(leader)'''

class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second #without bracket will return a taples


dice = Dice()
print(dice.roll())