# is it a group??

import itertools as it


# Closure. For every two elements in our group, if we perform our operation on them, then a 'operation' b must be also in the group

def closure(set, op):
	
	in_group = 0
	
	for elem1, elem2 in list(it.combinations(set, 2)):
	
		if op == 'add':
			output = elem1 + elem2
		if op == 'subtract':
			output = elem1 - elem2
		if op == 'multiply':
			output = elem1 * elem2
		if op == 'divide':
			output = float(elem1) / float(elem2)
		
		if output not in set:
			in_group = 'false'
	
	if in_group == 'false':
		print 'not a group - fails closure test'
	else:
		print 'passes closure test'


# Associativity.  For all a, b and c in our group this must hold (a 'operation' b) 'operation' c = a 'operation' (b 'operation' c)

def associativity(set, op):

	in_group = 0

	for x, y, z in list(it.combinations(set, 3)):
	
		if op == 'add':
			out1 = (x+y)+z
			out2 = x+(y+z)
		if op == 'subtract':
			out1 = (x-y)-z
			out2 = x-(y-z)
		if op == 'multiply':
			out1 = (x*y)*z
			out2 = x*(y*z)
		if op == 'divide':
			out1 = (float(x)/float(y))/float(z)
			out2 = float(x)+(float(y)+float(z))
		
		if out1 != out2:
			in_group = 'false'
	
	if in_group == 'false':
		print 'not a group - fails associativity test'
	else:
		print 'passes associativity test'


# Identity. In our group there is an element 'id' known as the identity element such that a 'operation' 'id' = a. In other words if we use the operation on an element and the identity, we will end up with the element.

# Inverse. In our group there is an element a-1 known as the inverse of a such that a 'operation' a-1 = 'id'. In other words if we use the operation on an element and its inverse, we will end up with the identity element, 'id'.


def identity_inverse(set, op):
	
	in_group = 0
	
	for n in set:
	
		if op == 'add':
			id = 0
			inverse = -n
		if op == 'subtract':
			id = 0
			inverse = n
		if op == 'multiply':
			id = 1
			inverse = 1.0/float(n)
		if op == 'divide':
			id = 1
			inverse = n
			
		if id not in set:
			in_group = 'id false'
		if inverse not in set:
			in_group = 'inv false'
	
	if in_group == 'id false':
		print 'not a group - fails identity test'
	else:
		print 'passes identity test'
	
	if in_group == 'inv false':
		print 'not a group - fails inverse test'
	else:
		print 'passes inverse test'

def test_it(set, op):
	closure(set, op)
	associativity(set, op)
	identity_inverse(set, op)

print ' '
print 'What set would you like to test? Please format it as a list of numbers with a space in between each number.'

set_input = raw_input('> ')
set_input = set_input.split(' ')
set = []

for n in set_input:
	set.append(int(n))

print ' '
print 'What operation is associated with the set? Options: add, subtract, multiply, divide'
op = raw_input('> ')
print ' '

test_it(set, op)

# test_it([0,1,2,3,4,5], 'divide')

