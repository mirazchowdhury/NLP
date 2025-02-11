day = input("Enter the day : ").strip()
time = int(input("Enter the time in 24-hour format (HH:MM): ").strip())


weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
weekends = ["Saturday","Sunday"]



if day in weekdays:
    if(time>=0 and time<17):
        print("There is no discount")
    elif(time>=17 and time<24):
        print(f"10% discount")
    else:
        print("Time error")
elif day in weekends:
    if(time>=0 and time<15):
        print(f"There is 5% discount")
    elif(time>=15 and time<24):
        print(f"There is 7% discount")
    else:
        print("Time error")
else:
    print("Invalid day entered")
