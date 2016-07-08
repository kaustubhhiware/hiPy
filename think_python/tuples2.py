from time import sleep
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


def sort_length(words):
	t = []
	for word in words:
		t.append((len(word),word))#build tuple

	t.sort(reverse=True)

	res = []
	for length,word in t:
		res.append(word)

	return res


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
sleep(1)
print 'enumerating your string 1 :',
enumerated(str1)
sleep(1)

print '\nconvert dict to tuple'
d = {'a':'0','b':'1','c':'2'}
t = d.items()
sleep(1)
print t

print '\nWe can use tuples as key in dictionary - like last name , first name for phone dir'
print 'directory[last,first] = number'

print '\nComparing tuples : first element compared - if one is greater ,than touple is greater',
print '\nelse it moves to the next element'

print '(0,1,2) < (0,3,4) : ',(0,1,2) < (0,3,4)
print '(0,1,2000) < (1,2,3):',(0,1,2000) < (1,2,3)
sleep(1)
print '\n\nTo sort by length'
length_tup = ['ar','kar','chamatkar','chaarmindar','kirloskar','murtikar','aavishkar']
print length_tup
print '\nalphabetic order: '
print sorted(length_tup)#sorts anything
#there is also reverse like this
print '\n'
sorted_tup = sort_length(length_tup)
print sorted_tup
