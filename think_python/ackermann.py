def ackermann(m,n):
	if not isinstance(m,int):
 		print 'm needs to be int'
 	elif not isinstance(n,int):
 		print 'n needs to be int as well'
 	elif m==0:
 		return n+1
 	elif m>0 and n==0:
 		return ackermann(m-1,1)
 	elif m>0 and n>0:
 		return ackermann(m-1,ackermann(m,n-1))

print 'ackermann(3,4) = ',ackermann(3,4)
print 'should be 125'
