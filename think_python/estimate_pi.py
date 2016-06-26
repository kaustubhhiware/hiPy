from factorial import * #factorial.py se uthaya hai
from math import *

#estimate pi - the formula derived from the man who knew oo
eps = 1e-15

def term(k):
	"""
		compute   (4k)!(1103+26390k)
				______________________

					(k!)^4 * 396 ^ 4k
	"""
	numerator = factorial(4*k) * (1103 + 26390 * k) * 1.0
	denominator = pow(factorial(k),4) * pow (396 , 4*k)

	y = numerator/denominator
	return y

def summation():
	"""
		 1		 2 root(2)	*	sum from 0 to lim( term(k) )
		___  =  ___________
		 pi			9801

		 lim is that val for which term(lim) < eps

	"""

	sum = 0.0
	k = 0

	while term(k) > eps:
		sum = sum+term(k)
		k = k + 1

	pi_inv = 2*sqrt(2)*sum/9801

	pi_var = 1/pi_inv
	#separate from math.pi
	return pi_var


print 'Estimation of pi as given by S.Ramanujan : ',summation()
print 'Pi value from lib : \t\t',pi


