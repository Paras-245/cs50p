greet = input("Greeting: ").lower().strip().split()[0]

if greet.startswith("hello"):
    print("$0")

elif greet[0] == "h":
    print("$20")

else:
    print("$100")