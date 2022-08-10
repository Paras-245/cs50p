months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
# first format = month/day/year
# second format = month day, year




while True:
    date = input("Date: ")
    # format 1 work
    if len(date.split("/")) == 3:
        try:
            month,day,year = date.split("/")
        except ValueError:
            continue
        if month in range(1,13) and day in range(1,32):
            print(f"{year:02}-{month:02}-{day:02}")
            break
        else:continue
    # format 2 work
    elif len(date.split()) == 3:

        month,day,year = date.split()
        if not day.endswith(","):
            continue
        try:
            day= int(day.removesuffix(','))
        except ValueError:
            continue

        if not month in months or not int(day) in range(1,32):continue

        else:
            print(f"{year}-{months.index(month) + 1:02}-{day:02}")
            break








