days = input("Enter Number of days")
rate = input("Enter the rate to be paid")
try :
    idays = float(days)
    irate = float(rate)
except :
    idays = -1
    irate = -1
if irate > 0 :
    if idays > 0:
        total = idays*irate
        print("Total pay",total)
else :
    print("Please enter numeric input")