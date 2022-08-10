def vowel_checker(c):
    c = c.lower()
    vowels = ["a","e","i","o","u"]
    for v in vowels:
        if c == v:
            return True
    return False
text = input("Input: ")
for c in text:
    if vowel_checker(c):
        continue
    else:
        print(c,end="")
print()