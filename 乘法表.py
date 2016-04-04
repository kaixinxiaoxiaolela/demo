for j in range(1,10):
	for i in range(1,10):
		formula='{0:1}*{1:1}={2:<2}'.format(j,i,j*i)
		if j>i:
			print(end='       ')
		if j<=i:
			print(formula,end=' ')
	print()

	