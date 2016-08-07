#!/usr/bin/python2.4 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises


# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.



def verbing(s):
	# +++your code here+++
	lst = list()
	if len(s) >= 3:
		
		for i in s:
			lst.append(i)
		if (lst[-1] == 'g' and lst [-2] == 'n' and lst [-3] == 'i'):
			lst.append ('l')
			lst.append ('y')
			s = ''.join(lst)		
			return s
		else :
			s = s + "ing"
			return s
	
	else:
		return s


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
	# +++your code here+++
	nott = s.find("not")
	bad= s.find("bad")
	bad1 = s.find("bad") + 3
	if nott < bad :
		s1 = s[:nott]
		s2 = s[bad1:]
		s3 = "good"
		s = s1 + s3 + s2
	return(s)


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back

def front_back(a,b):
	# +++your code here+++
	if len(a)%2 == 0:
		n = int(len(a)/2)
		for i in range (0,n,n):
			a_front = a[i:i+n]
		for i in range (0,len(a),n):
			a_back = a[i:i+n]

	
	else:
		n = int(len(a)/2 +1) 
		for i in range (0,n,n):
			a_front = a[i:i+n]
		for i in range (0,len(a),n):
			a_back = a[i:i+n]

	if len(b)%2 == 0:
		n = int(len(b)/2)
		for i in range (0,n,n):
			b_front = b[i:i+n]
		for i in range (0,len(b),n):
			b_back = b[i:i+n]

	
	else:
		n = int(len(b)/2 +1) 
		for i in range (0,n,n):
			b_front = b[i:i+n]
		for i in range (0,len(b),n):
			b_back = b[i:i+n]

	return(a_front + b_front + a_back + b_back)

# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
	if got == expected:
		prefix = ' OK '
	else:
		prefix = '	X '
	print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
	print('verbing')
	verbing("swim")
  
	test(verbing('hail'), 'hailing')
	test(verbing('swiming'), 'swimingly')
	test(verbing('do'), 'do')

	print()
	print('not_bad')
	test(not_bad('This movie is not so bad'), 'This movie is good')
	test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
	test(not_bad('This tea is not hot'), 'This tea is not hot')
	test(not_bad("It's bad yet not"), "It's bad yet not")

	
	print('front_back')
	test(front_back('abcd', 'xy'), 'abxcdy')
	test(front_back('abcde', 'xyz'), 'abcxydez')
	test(front_back('Kitten', 'Donut'), 'KitDontenut')
	
if __name__ == '__main__':
	main()
