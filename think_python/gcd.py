def gcd(a,b):
	"""
	 return gcd of a and b
	"""
	#assume a always greater than b , if not swap
	if b > a:
		swap = a
		a = b
		b = swap

	if b==0:
		return a
	else:
		return gcd(a%b,b)


print "Compute gcd of a and b"
a=raw_input("enter a : ")
b = raw_input("enter b : ")

print "gcd : ",gcd(int(a),int(b))


