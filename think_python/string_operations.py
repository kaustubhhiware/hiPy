def find(word,letter):
	"""
	find letter in word , return first occurence
	"""

	index=0
	while index < len(word):
		if word[index]==letter:
			#print word,' ',word[index],' ',letter,' ',index,' waht'
			return index
		index = index  + 1
	return -1

inp_str = raw_input("Enter string for analysis : ")

print "\n0th index based , str[1] is second letter : ",inp_str[1]

print "\nLength of str by len(str): ",len(inp_str)

print "\nTraversal using for "
for char in inp_str:
	print char

print "\nReverse traversal with While "

index = len(inp_str)-1
while index > -1:
	letter = inp_str[index]
	print letter
	index = index - 1 

"""
some examples here : 

>>s = 'Monty Python'
>>print s[0:5]
Monty
>>print s[6:12]
Python

>>>fruit='banana'
>>>fruit[3:]
ana
>>>fruit[:3]
ban

fruit[0:5:2] => 2 means scan size

fruit[::-1] => reverse


"""

print 'New strings from old ones'
greeting = 'Hello , World!'
print greeting

new_greeting='J'+greeting[1:]
print new_greeting


print '\nFinding a in input string ...'
leter = 'a'

if find(inp_str,leter)==-1:
	print 'Not found :('
else:
	print 'a at index ',find(inp_str,leter) 

print '\ninput capitalised : ',inp_str.upper()


"""
default find function

string.find('a') =>first occurence
.find('substring')
.find(str,start_from)
.find(str,start_from,end_at)

"""

print '\nIs a in input ? ','a' in inp_str

#check alphabetical order
if inp_str < 'banana':
	print '\ninput comes before banana'
else:
	print '\ninput comes after banana'

#continue to rot13.py