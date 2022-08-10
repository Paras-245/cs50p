# function get the indexes which are in capital
def indexes(camel):
    index = []
    for c in range(len(camel)):
         if camel[c].isupper():
            index.append(c)
    return index

# convert the string to snake case
def camel_case(index,text):
    camel = []
    for c in range(len(text)):
        if c in index:
            camel.append("_")
            camel.append(text[c])
        else:
            camel.append(text[c])
    return camel

# main
def main():
    # text got from the user
    text = input("camelCase: ")
    # function return the index of capital
    index = indexes(text)
    text = text.lower()
    camel = camel_case(index,text)
    # print the list given from the function
    for c in camel:
        print(c,end = "")
    print()

main()


