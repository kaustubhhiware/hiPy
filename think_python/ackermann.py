import time

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

known = {}
#memoisation
def ackermann_memo(m,n):
	if m==0:
		return n+1
	if n==0:
		return ackermann_memo(m-1,1)
	try :
		return known[m,n]
	except KeyError:
		known[m, n] = ackermann_memo(m-1, ackermann_memo(m, n-1))
        return known[m, n]

if __name__=='__main__':

	print 'M1'
	start = time.time()
	print 'ackermann(3,4) = ',ackermann(3,4)
	elapsed = time.time() - start
	print 'time : ',elapsed

	print 'M2'
	start = time.time()
	print 'ackermann(3,4) = ',ackermann_memo(3,4)
	elapsed = time.time() - start
	print 'time : ',elapsed

	print 'o/p should be 125'
	#note : ack(4,7) runs out of depth for 4,7