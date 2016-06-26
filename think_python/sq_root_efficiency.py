import math
#this file is used to check the efficiency of our estimate method in sq_root_estimate
#number of iterations in invalid here


eps = 0.00001# defining standard , not changing
def within_epsilon(x,y,eps):
	"""
		check if |x - y| < eps
	"""
	if(abs(x-y) < eps):
		return True
	else :
		return False


def sq_root_est(a,x):
	#use some default value
	"""
		estimate square root of a by formula - 
		y = (x+a/x)/2
		x = y
		...continue till x and y are within some epsilon range e
		x is some initial guess
	"""
	y = (x + a/x)/2

	if within_epsilon(x,y,eps):
		return y
	else :
		x = y
		return sq_root_est(a,x)#further iteration


lim = raw_input("Enter top limit : ")
lim = int(lim)

print "Conducting analysis for sq_root method from 1 to lim..."
print "i \t estimate \t sqrt \t difference"
for i in range(lim):
	i = i+1 # avoid 0 
	a = float(i)
	x = a# initial guess
	y = sq_root_est(a,x)

	diff = y - math.sqrt(a)
	print a,"\t",y,"\t",math.sqrt(a),"\t",diff