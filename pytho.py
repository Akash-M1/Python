def pay(days,rate):
	total = days*rate
	return total
day=input("Enter number of days")
rates = input("Enter rate to be paid")
try:
    iday = float(day)
    irate = float(rates)
    print("Total pay is :",pay(iday,irate))
except:
    print("Enter valid numbers")	