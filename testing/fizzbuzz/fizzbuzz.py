# simple fizbuzz program, feed the method an integer and it outputs
# a string based on the input
def fizzbuzz(n):
	if n % 3 == 0 and n % 5 == 0:
		return 'Fizz Buzz'
	if n % 3 == 0:
		return 'Fizz'
	if n % 5 == 0:
		return 'Buzz'
	return n