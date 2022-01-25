"""This file contains a code example related to
Think Python, 2nd Edition, Chapter 5, Exercise 5-4
by Allen Downey
    Written by Mustafa Ali.
"""


def recurse(n, s):
	if n == 0:
		print(s)
	else:
		recurse(n-1, n+s)


recurse(3, 0)


stack_diagram:
	__main__ 

	recurse	 --> n -> 3
		     s -> 0

	recurse  --> n -> 2
		     s -> 3

	recurse  --> n -> 1
		     s -> 5

	recurse  --> n -> 0
		     s -> 6

This function prints the sum of all the integers from 1 to n, given an integer n.

1) The program does not terminate. It exits with a runtime error since the maximum recursion
	depth is reached.
2) """This function takes an integer 'n', that is greater than or equals to zero and
	returns the sum of all natural numbers from 1 to 'n'"""