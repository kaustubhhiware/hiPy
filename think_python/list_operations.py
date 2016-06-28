def length(listed):
	"""
		return length of list
	"""
	count = 0
	for item in listed:
		count += 1
	return count


def is_sorted(listed):
	"""
		Check if list is alphabetically sorted
	"""
	original=listed[:]
	listed.sort()
	for i in range(length(listed)):
		if original[i]!=listed[i]:
			return False
	return True

def is_it_there(char,listed):
	"""
		return first index of 
	"""


def is_anagram(s,t):
	"""
		Check if s and t are anagrams of each other 
		by cutting out each element of s from t
	"""
	t_o = t
	for i in s:
		if not i in t:
			return False
		else:
			index = t.find(i)
			str_t = t[:index]+t[index+1:]
			t = str_t
			#print 'i :',i,' t :',t

	#check vice-versa
	for i in t_o:
		if not i in s:
			return False
		else:
			index = s.find(i)
			str_s = s[:index]+s[index+1:]
			s = str_s
			#print 'i :',i,' s :',s
	return True


def has_duplicates(listed):
	"""
		check for duplicates
		Birthday paradox!
	"""
	for index in range(length(listed)):
		
		j = index+1
		while j!=length(listed):
			
			if listed[j]==listed[index]:
			#duplicate spotted!
				return True 
			j += 1
	return False


def remove_duplicates(listed):
	"""
		remove all duplicates
		
	"""
	duply = listed[:]
	duply.sort()
	for i in range(length(duply)-1):
		j = length(duply)-1-i

		if duply[j]==duply[j-1]:
			corrected_duply = duply
			corrected_duply.pop(j)
			#print 'step list : ',corrected_duply
			return remove_duplicates(corrected_duply)

	return duply#only in perfect case


print 'is_sorted([1,2,2]) : ',is_sorted([1,2,2])
print 'is_sorted([1,3,2]) : ',is_sorted([1,3,2])


s = raw_input("\nEnter first string to check for anagram : ")
t = raw_input("Enter second string : ")
print 'Are they anagrams? ',is_anagram(s,t)
#example : archana , rachana
#These arre the names of my English teacher , you creep

r = ['a','b','c','a','e','d','f','e','d','g']
print '\nhas_duplicates for ',r ,' : ',has_duplicates(r)

print 'remove duplicates : ',remove_duplicates(r)
