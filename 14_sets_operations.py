# Sets 2
# Intergers 1 - 10
odds = set([1, 3, 5, 7, 9])
evens = set([2, 4, 6, 8, 10])
primes = set([2, 3, 5, 7])
composites = set([4, 6, 8, 9, 10])

odds.union(evens)
evens.union(odds)
odds.intersection(primes)
primes.intersection(evens)
primes.union(composites)

#2 in primes """ Returns True"""
#6 in odds """Returns False"""
