import math
import random

# All points have integer coordinates in [0,2^N-1] x [0,2^N-1]
N = 8

# Roughly speaking, decompose our points into sets C_m with
# 'Assoud dimension 1' and density constant 2^m, and where
# C_m is concentrated on a union of balls of radius 1/2^m.
#
# Roughly speaking, if we take any average of the wave equation
# on a set with Assoud dimension 1, then we can get L^2 bounds
# better than that obtained via
#
# The bound we prove should be equivalent to the fact that,
# for any measure mu with Assoud dimension 1 and Assoud constant C,
# and with mu(R^d) = 1,
#
# || W(x,r) ||_{L^2(mu)} << C^{1/(d-1)}

points = list()

# Add a set of points concentrated on a line of thickness 1
# Equation of line is y = x^2
print(N//2)
for x in range(2,2**N):
	if 3*x > 2**N:
		break

	for y in range(1,2):
		points.append((x, 3*x + 10 - random.randint(1,5)))

# Add a set of points concentrated on a line of thickness 4
# Equation of line is y = 2x - 3
for x in range(2,2**N):
	if 2*x-3 > 2**N:
		break
	for y in range(1,3):
		points.append((x, 2*x-3 - random.randint(1,7)))

# Add a set of points concentrated on a line of thickness 8
# Equation of line is y = 2
for x in range(2, 2**N):
	for y in range(1,5):
		points.append((x,2+random.randint(1,10)))

for x in range(2**(N-1)):
	points.append((random.randint(1,2**N-1), random.randint(1,2**N-1)))

# Radius r circle contains r^2 points, so has density type r
# so we want a radius 5 circle?
for x in range(1,2**N):
	for y in range(1,2**N):
		t = x + 50 - 2**N
		s = y + 50 - 2**N

		if t*t + s*s < 100:
			points.append((x,y))


#random_spread_out = [ (random.randint(1,2**N-1), random.randint(1,2**N-1)) for i in range(2**N) ]
#random_concentrated = [ ( 7 + random.randint(1, 2**(N-3)-1), 32 + random.randint(1, 2**(N-3)-1) ) for i in range(k//8)]
#random_concentrated_3 = [ ( 2**(N-1) + random.randint(1, 2**(N-2)-1), 32 + random.randint(1, 2**(N-2)-1) ) for i in range(k)]
#random_concentrated_2 = [ (2**(N-1) + random.randint(1, 3), random.randint(1, 2**N - 1)) for i in range(k) ]

#points = random_spread_out + random_concentrated + random_concentrated_2

import matplotlib.pyplot as plt
import numpy as np

a = list()
for i in range(1,2**N):
	a.append(list())

	for j in range(1,2**N):
		if (i,j) in points:
			a[i-1].append(1)
		else:
			a[i-1].append(0)
amatrix = np.matrix(a)
plt.imshow(a, cmap='Reds', interpolation='none')
plt.show()

print(amatrix)

def distance(p1, p2):
	x_dist = p1[0] - p2[0]
	y_dist = p1[1] - p2[1]

	d_squared = x_dist*x_dist + y_dist*y_dist

	return math.sqrt(d_squared)

#square_distances = { (p1, p2): square_distance(p1,p2) for p1 in points for p2 in points }

averages = {}
for cx in range(1,2**N):
	print(cx)
	for cy in range(1,2**N):
		center = (cx,cy)

		buckets = [ 0 for i in range(2*(2**N)) ]
		for p in points:
				buckets[math.ceil(distance(center,p))] += 1

		total = 0

		for r in range(1,2**N+1):
			total += buckets[i-1]

			averages[center,r] = total / r

def uncentered_maximal(a):
	max_so_far = 0

	for center_x in range(1,2**N):
		for center_y in range(1,2**N):
			center = (center_x,center_y)

			for r in range(1,math.ceil(distance(a,center)), 2**N-1):
				max_so_far = max(averages[center,r], max_so_far)

	print(a,max_so_far)
	return max_so_far

def maximal(point):
	buckets = [ 0 for i in range(2*(2**N)) ]

	for p in points:
		buckets[math.ceil(distance(point,p))] += 1

	total = 0
	max_so_far = 0

	for i in range(1,2*(2**N)):
		total += buckets[i-1]

		if total / i >= max_so_far:
			max_so_far = total / i

	return max_so_far

print(len(points))

maximal_function_dict = dict()
for p in points:
	print(p)
	maximal_function_dict[p] = uncentered_maximal(p)

#for p in points:
#	print(p,maximal_function_dict[p])

# We have a subset of points that lie in [1,2**N-1]
# and they have density type 2^l


for l in range(2,6):
	print("Density Type: ", l)

	a = list()

	for i in range(1,2**N):
		a.append(list())
		for j in range(1,2**N):
			if (i,j) in points and 2**l <= maximal_function_dict[(i,j)] and maximal_function_dict[(i,j)] <= 2**(l+1):
				a[i-1].append(1)
			else:
				a[i-1].append(0)

	amatrix = np.matrix(a)
	plt.imshow(a, cmap='Reds', interpolation='none')
	plt.show()