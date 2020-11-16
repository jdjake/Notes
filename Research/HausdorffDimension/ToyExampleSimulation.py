import random
import itertools

# r = K^{-1/\beta}
# Cardinality is 

n = 3

K = 1000
N = K**(n-1)

cardinality = N

# Fix some set E in [N]^n. Try and compute the probability that
# there is some k_1,...,k_n such that (X_{k_1},...,X_{k_n}) in E
# Hopefully proportional to #(E) times a quantity, perhaps K^n?

# Generates random list of K integers in [1,N]
def generate_random_quantities(K):
	generated_quantities = frozenset(random.randint(1,N) for x in range(K))

#	generated_quantities.sort()
	return generated_quantities

# Generates a random set E containing each element of [N]^n with
# probability p of containing each element.
def generate_random_E(cardinality):
	E = [tuple(random.randint(1,N+1) for j in range(n)) for i in range(cardinality)]
	#print(E)

	return E

X = [generate_random_quantities(K) for i in range(n)]
for i in range(n):
	print(K,len(X[i]))

print("Here")
E = generate_random_E(cardinality)
print("Here2")

# Count the number of points in E contained in X
count = 0
for a in E:
	is_in_product = True
	for i in range(n):
		if a[i] not in X[i]: is_in_product = False

	if is_in_product:
		count = count + 1
print(cardinality,count, float(count) / float(cardinality) )