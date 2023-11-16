# Two simple function, one generates computer's choice (p = paper, r = rock, s = scissors).
# Second one is a test function in which we can see how often do we get certain results.

import random
def random_choice():
    list1 = ['r', 'p', 's']
    return random.choice(list1)


def test():
    counter = 0
    p = 0
    r = 0
    s = 0
    for i in range(1000):
        counter+=1
        result = random_choice()
        if result == 'p': p+=1
        elif result == 's': s+=1
        else: r+=1
    print(f"Rock {round(r/counter*100,2)}%\n")
    print(f"Paper {round(p/counter*100,2)}%\n")
    print(f"Scissors {round(s/counter*100,2)}%\n")

test()