import inflect
inf = inflect.engine()
names = []
while True:
    try:
        name = input("Name: ")
        if not len(name) == 0:
            names.append(name)


    except EOFError:
        print()
        break
mylst = inf.join(tuple(names))
print("Adieu, adieu, to",mylst)



