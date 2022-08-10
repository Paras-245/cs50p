amount = 50
while amount > 0:
    print("Amount Due:",amount)
    x = int(input("Insert Coin: "))
    if x != 5 and x != 25 and x!= 10:
        continue
    else:
        amount -= x

print("Change Owed:",abs(amount))
