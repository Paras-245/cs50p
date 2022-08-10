def main():
    time = input("What time is it?: ")
    # time = "7:54"
    c_time = convert(time)
    if c_time >= 7.0 and c_time <= 8.0:
        print("breakfast time")

    elif c_time >= 12.0 and c_time <= 13.0:
        print("lunch time")

    elif c_time >= 18.0 and c_time <= 19.0:
        print("dinner time")


def convert(time):
    hours,minutes = map(int,time.split(":",1))
    time = hours+minutes/60

    return time



if __name__ == "__main__":
    main()