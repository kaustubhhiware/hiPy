from time import sleep
def min_max(t):
	return min(t),max(t)

sum = 0
def sumall(*args):
	"""sum(1,2,3) gives invalid o/p
	"""
	global sum
	for i in args:
		sum += i
	return sum


print 'Tuples are a seq of vals , indexed by integers ~ list'

t1 = 'a',
print 't1 = \'a\',',type(t1)
print 'The comma is important\n'

t2 = ('a')
print 't2 = (\'a\')',type(t2)

sleep(1)
t = tuple()
print t

t = tuple('lupins')
print t
sleep(1)

print '\nlist operations work on tuples as well like'
print 't[0] = ',t[0]
print 't[1:3] = ',t[1:3]
sleep(1)
print '\nHowever , t[0] = \'A\' gives a type error .\nYou could just do t = (\'A\',)+t[1:]'

print '\n to swap a and b , normally swap var is needed.Not here :P .Just do a,b = b,a'
a = 10
b = 5
print 'a = ',a,'b = ',b
a,b = b,a
print 'a = ',a,'b = ',b
sleep(1)
print 'Assigning is so easy! a,b = 7,11'
a,b = 7,11
print a,b

print '\nSplitting email address much easy'
addr = 'name@domain.com'
uname,domain = addr.split('@')

print addr,' : ',uname,' and ',domain
sleep(1)
print '\nReturning tuples : '
t = divmod(7,3)
print 'divmod(7,3) = ',t

numt = (1,-2,43,4)
kam,jyada = min_max(numt)

print kam,'to ',jyada
sleep(1)
print '\nTuple contains multiple type of args : use *'
print 'def func(*args):print args'

t = (7,3)
print 't = (7,3)'
print 'divmod(t) returns argument insufficient'
print 'do divmod(*t) : ',divmod(*t)

print 'sum tuple function for ',numt,' : ',sumall(*numt)