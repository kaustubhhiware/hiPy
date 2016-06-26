string = '0'

pause = 'done'

while True:
	string = raw_input("Enter str to evaluate : ")

	if string!=pause:
		print eval(string)
	#elif isinstance(string,str):
	#	print 'what a string !'
	else:
		break

print 'all done !'