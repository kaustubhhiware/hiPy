def has_match(str1,str2):
	tup1 = tuple(str1)
	tup2 = tuple(str2)

	indices = []
	upto = len(min(tup1,tup2))
	for i in range(upto):
		indices.append(i+1)

	is_common = False
	for index,x,y in zip(indices,tup1,tup2):
		if x==y:
			print x,' is common at ',index
			is_common = True

	if not is_common:
		print 'No match !'


def enumerated(str):
	
	for index,element in enumerate(str):
		print index,element


print '\nzip combines two lists into a tuple with key as first , val as second : '
s = 'abc'
t = [0,1,2]
k = zip(s,t)

print k
print 'Fancie print by tuple :'
for char , num in k:
	print char, num

print '\nif zip gets two lists of diff length , the shorter one gets through'


print 'Check if two strings have the same letter at the same position :'
str1 = raw_input("string 1 : ")
str2 = raw_input("string 2 : ")
has_match(str1,str2)

print 'enumerating your string 1 :',
enumerated(str1)
