def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    # return f"Leave ${tip:.2f}"
    print("Leave $"+ '%.2f' % tip)


def dollars_to_float(d):
    # TODO
    d = d.replace("$","")
    return float(d)



def percent_to_float(p):
    # TODO
    p = p.replace("%","")
    return float(p)/100




main()