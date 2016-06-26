import math

def within_epsilon(x,y,e):
	"""
		check if |x - y| < e
	"""
	if(abs(x-y) < e):
		return True
	else :
		return False



def sq_root(a,x,num_iter,e=0.00001):
	#use some default value
	"""
		estimate square root of a by formula - 
		y = (x+a/x)/2
		x = y
		...continue till x and y are within some epsilon range e
		x is some initial guess
		n is the number of iterations it took for accuracy
	"""
	y = (x + a/x)/2

	print 'working  ...iteration[',num_iter[0],'] , y = ',y
	if within_epsilon(x,y,e):
		print '\nThe estimated square root is : ',y

	else :
		x = y
		num_iter[0] = num_iter[0] + 1#increment iteration count
		sq_root(a,x,num_iter,e)#further iteration


a = raw_input("Enter the number for which square root is to be calculated : ")
x = raw_input("Some initial guess perhaps? : ")
e = raw_input("what epsilon range? : ")

num_iter = [0]
sq_root(float(a),float(x),num_iter,float(e))#0 is num_iter init
print 'The number of iterations required is : ',num_iter[0]