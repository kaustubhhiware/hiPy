def printlist(listed):
	for num in listed:
		print num


def add_all(listed):
	tots = 0
	for x in listed:
		tots +=  x
	return tots


def all_caps_on_me(t):
	out=[]
	for s in t:
		out.append(s.capitalize())
	return out

list2 = [1,2,3,4]

print 'first element',list2[0]

print 'last element',list2[-1]

print 'search 42 in list',42 in list2

print '\nall elements'
printlist(list2)

print 'doubling all identities'
for i in range(len(list2)):
	list2[i] = list2[i]*2

print '\n'

list3 = [100,99,98,97]

print 'joining 2 lists'
new_list = list2 + list3
#printlist(new_list)
print new_list

print 'list3 repeated once'
print list3*2
	
print '\n'

alpha = ['a','b','c','d','e','f']
print 'operating on :',alpha
print 'also known as alpha[:]'

print 'alpha [1:3] = ',alpha[1:3]

print 'alpha[:4] = ',alpha[:4]

print 'alpha[3:] = ',alpha[3:]

print 'replace b,c by g,h'
alpha[1:3]=['g','h']
print alpha

print '\n'

beta=['a','b','c']
print beta
print 'append new data'
beta.append('d')
print beta

ceta = ['e','f']
print 'append another list'
beta.extend(ceta)
print beta

print '\n'

arbit = ['f','j','a','k','e','x','t','u']
print 'arbit list : ',arbit
arbit.sort()					#NEVER do t=t.sort() - returns None
print 'sorted list : ',arbit
print 'capitalized : ',all_caps_on_me(arbit)

"""
	this is a map - map a function onto each element of sequence

	filter - selects some elements and ignores others
	e.g: Print only capitalized letters in a sequence
"""
print '\n'

print 'going back to new_list : ',new_list
#adding
print 'Adds up to ',add_all(new_list)
#built in
print 'LAme! just do sum(t) ',sum(new_list)