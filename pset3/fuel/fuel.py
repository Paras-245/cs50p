while True:
    try:
        X,Y = map(int,input("Fraction: ").split("/"))
        if not X > Y:
            fuel = round(X/Y * 100)
            break
    except (ValueError,ZeroDivisionError):
        continue
if fuel <= 1:
    print("E")
elif fuel >= 99:
    print("F")
else:
    print(str(fuel) + "%")
