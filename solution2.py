def natural_numbers(n,i=1):
	#your code here
    if i > n:
        return

    else:
        print(i)
        natural_numbers(n,i+1)
natural_numbers(3)
#output: 1 2 3