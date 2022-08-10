dic = {}
while True:
    try:
        item = input().upper()
        if dic.get(item,0) == 0:
            dic[item] = 1
        else:
            dic[item] += 1
    except EOFError:
        print()
        break
    except KeyError:
        continue
for i in sorted(dic.keys()):
    print(dic[i],i)
