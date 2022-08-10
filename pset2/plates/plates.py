def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # # Checking for plate limit
    if  len(s) > 6 or len(s) <  2:
        return False
    # # checking for first two letters are alphabets
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    if not checking_3(s):
        return False

    # checking for punctuation or special chars
    if not s.isalnum():
        return False


    return True


def checking_3(s):
    digit_starting = None
    for c in range(len(s)):
        if s[c].isdigit():
            if digit_starting == None:
                digit_starting = c
        if not digit_starting == None:
            if s[c].isalpha():
                return False

    if not digit_starting == None:
        if s[digit_starting] == "0":
            return False
    return True





main()