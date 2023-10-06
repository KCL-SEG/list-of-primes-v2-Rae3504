"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def primes(number_of_primes):
	if number_of_primes <= 0:
		raise ValueError

	list = []
    
	num = 2
	while len(list) < number_of_primes:
		if is_prime(num):
			list.append(num)
		num += 1

	return list
