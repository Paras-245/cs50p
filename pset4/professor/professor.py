import random


def main():
    level = get_level()
    score = 0
    for i in range(1,11):
        first_no = generate_integer(level)
        second_no = generate_integer(level)
        correct = first_no + second_no
        for i in range(3):
            try:
                answer = int(input(f"{first_no} + {second_no} = "))
                if answer == correct:
                    score += 1
                    break
                else:
                    raise ValueError
            except ValueError:

                print("EEE")
                if i == 2:
                    print(f"{first_no} + {second_no} = {correct}")
                continue
    print(score)






def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1,2,3]:
                raise ValueError
            else:
                return level

        except ValueError :
            continue


def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    else:
        return random.randint(100,999)



if __name__ == "__main__":


    main()