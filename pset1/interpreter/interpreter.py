exp = input("Expression: ").split()
x = int(exp[0])
y = exp[1]
z = int(exp[2])

if y == "+":
    print(float(x + z))

if y == "-":
    print(float(x - z))

if y == "/":
    print(float(x / z))

if y == "*":
    print(float(x * z))


