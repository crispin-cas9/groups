# is it a group??

import itertools as it

def closure(set, op):
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


def associativity(set, op):
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


def identity_inverse(set, op):
	
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
			in_group = 'false'
	
	if in_group == 'false':
		print 'not a group - fails identity test'

def test_it(set, op):
	closure(set, op)
	associativity(set, op)
	identity_inverse(set, op)

test_it([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'subtract')


