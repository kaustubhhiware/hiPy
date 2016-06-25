
def factorial(n):
	if not isinstance(n,int):
		print 'Factorials are for numbers , stupid'
	elif n < 0:
		print 'Why so negative?',' mate'
	elif n==0:
		return 1
	else :
		prev=factorial(n-1)
		result=prev*n
		return result