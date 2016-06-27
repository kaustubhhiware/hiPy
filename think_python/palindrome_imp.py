string = raw_input("Enter string to check for palindrome :")

if string==string[::-1]:
	print ' It\'s a palindrome!'
else:
	print 'you are weak now , return later'

#improved version based on strings
"""
Something interesting : Collatz conjecture

Consider the following operation on an arbitrary positive integer:

    If the number is even, divide it by two.
    If the number is odd, triple it and add one.

    Our main man said that this eventually stops at 1
"""