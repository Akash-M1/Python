while(True) :
    sum =0
    count = 0
    x=input("Enter a number")
    if(x==exit):
        break
    try:
        ix=int(x)
    except:
        print("Please Enter valid number")
        continue
    sum = sum + ix
    count = count+1
print("Sum of The numbers",sum)
print("Count of numbers",count)
print("Average of Numbers",sum/count)

                


