ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
ans = ans.casefold().strip()
if ans == "42" or ans == "forty-two" or ans == "forty two":
    print("Yes")
else:
    print("No")