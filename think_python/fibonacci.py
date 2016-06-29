import time

def fibonacci(n):
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		return fibonacci(n-1)+fibonacci(n-2)


#using memoisation
known ={0:0, 1:1}
def fib_imp(n):
	if n in known:
		return known[n]
	
	res = fib_imp(n-1)+fib_imp(n-2)
	known[n] = res
	return res

if __name__=='__main__':

	n = raw_input("enter n for which fib(n) is needed :")
	n = int(n)

	start_time = time.time()
	print 'M1 : ',fibonacci(n)
	elapsed_time = time.time() - start_time
	print 'elapsed_time :',elapsed_time,'s'

	start_time = time.time()
	print 'M2 : ',fib_imp(n)
	elapsed_time = time.time() - start_time
	print 'elapsed_time :',elapsed_time,'s'

# results - n = 34
# M1 2.30215406418 s
# M2 3.09944152832e-05 s
