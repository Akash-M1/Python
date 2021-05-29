small = None
i = [9,41,12,3,74,15]
for I in i :
    if small is None:
		small = I
	elif I<small :
	    small = I

print("Smallest is",small)	    
