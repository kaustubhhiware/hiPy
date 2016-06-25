def is_power(a,b):
	"""
	Check if a is a power of b
	"""
	if a==1:
		print 'power'
	elif a%b!=0:
		print 'NAh ,not a power'
	else:
		a = a/b
		is_power(a,b)

print "Check if a is a power of b"
a=raw_input("enter a : ")
b = raw_input("enter b : ")

is_power(int(a),int(b))