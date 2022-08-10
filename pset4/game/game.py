import random
n = -1
while n <= 0:
    try:
        n = int(input("Level: "))
    except ValueError:
        continue
number = random.randint(1,n)
num = -1
while  num != number:
    try:
        num = int(input("Guess: "))
    except ValueError:
        continue
    if num < 1 :
        continue
    if num == number:
        print("Just right!")
    elif num < number:
        print("Too small!")
    else:
        print("Too Large!")

