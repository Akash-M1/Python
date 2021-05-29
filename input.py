sum = 0
count = 0.0
while True :
	x=input("Enter a Number")
	if x == "exit" :
		break
	try :
    	fx= float(x)
	except:
    	print("Bad data input")
    	continue 	
    count = count+1
    sum = sum + fx
    avg = sum/count
print("Sum =",sum)
print("Count =",count)
print("Average =",avg)             