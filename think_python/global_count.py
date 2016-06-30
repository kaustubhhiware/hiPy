count = 1

def counter(n):
	#learn how to change global var
	global count
	while count!=n:
		print count
		count += 1

print 'global handling'
counter(10)