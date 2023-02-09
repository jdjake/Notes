from random import *
from functools import *

squared_dist_memo = {}

def squared_dist(n,m):
	if n == m: return 0

	if (n,m) not in squared_dist_memo.keys():
		squared_dist_memo[(n,m)] = (n-m)*(n-m) + (n*n - m*m)*(n*n-m*m)

	return squared_dist_memo[(n,m)]

first = randint(1,80)
second = randint(1,80)
isosceles_free_set = [first,second]

while True:
	new_entry = randint(-80,80)

	has_isosceles = False
	for current_entry in isosceles_free_set:
		if has_isosceles: break

		for other_entry in isosceles_free_set:
			if abs(squared_dist(current_entry,other_entry) - squared_dist(current_entry,new_entry)) <= 10000:
				has_isosceles = True
				break

	if not has_isosceles:
		isosceles_free_set.append(new_entry)

		isosceles_free_set.sort()
		print(isosceles_free_set)
		print(len(isosceles_free_set))