# check if set/operation is a group -- this time with number systems!

import itertools as it


# Closure. For every two elements in our group, if we perform our operation on them, then a 'operation' b must be also in the group

def is_natural(n):
	if n >= 0 and isinstance(n, int) == True:
		return True

# determine if something is an integer: isinstance(n, int)

def is_rational(n)
	if isinstance(n, int) == True or isinstance(n, float) == True:
		return True

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


naturals = [0, 1, 2, 3, 10, 500, 121, 77, 3331]
integers = [0, 1, 2, 500, 121, 77, 3331, -1, -2, -500, -121, -75, -3631]
rationals = [0, 1, 2, 500, 77, 3331, -1, -2, -121, -3631, 1.5, 123.7, -5.822, -100.03]

closure(naturals, add)