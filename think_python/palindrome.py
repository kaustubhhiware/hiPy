def first(word):
	return word[0]

def last(word):
	return word[-1]

def mid(word):
	return word[1:-1]

def isPalindrome(word):
	if first(word)!=last(word):
		return False
	elif len(mid(word))<2:
		return True
	else:
		return isPalindrome(mid(word))


str = raw_input('Enter string to check for palindrome : ')

if isPalindrome(str)==True:
	print ' It\'s a palindrome!'
else:
	print 'you are weak now , return later'