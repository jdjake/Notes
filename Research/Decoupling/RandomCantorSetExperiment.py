from random import randint
from matplotlib import pyplot as plt
import numpy as np

# Generate xi_I

def iterate_over_tree_nodes(tree):
	left_num = tree[0][0]
	left_tree = tree[0][1]

	right_num = tree[1][0]
	right_tree = tree[1][1]

	if left_tree == None and right_tree == None:
		yield (left_num,)
		yield (right_num,)

		return

	if left_tree == None or right_tree == None:
		print("BIG ERROR")
		return

	for a in iterate_over_tree_nodes(left_tree):
		yield (left_num,) + a

	for a in iterate_over_tree_nodes(right_tree):
		yield (right_num,) + a

def build_random_tree(scale):
	if (scale == 0):
		return None

	else:
		left = build_random_tree(scale - 1)
		right = build_random_tree(scale - 1)

		left_int = 1
		right_int = 1

		while (left_int == right_int):
			left_int = randint(0,2)
			right_int = randint(0,2)

		return [(left_int,left), (right_int,right)]

def generate_centers(scale):
	# Build a Tree of Random Numbers

	tree = build_random_tree(scale)
	list_of_nums = iterate_over_tree_nodes(tree)

	for num_list in list_of_nums:
		total = 0

		for i in range(scale):
			total += num_list[i] * 3**(-(i+2))

		yield total

def graph_oscillation(scale):
	# get a matrix whose centers consist of all 2^i centers
	# of a Cantor set discretized to a scale 1/3^i
	centers = np.matrix(list(generate_centers(scale)))

	# uncomment this to get a matrix whose centers
	# are uniformly distributed between [0,1]
	#centers = np.matrix(np.random.random(2**scale))

	print("finished calculating centers")

	# test exponential sum against all integer
	# values of x between -3^i and 3^i
	x_values = np.asmatrix(np.arange(- 3**scale, 3**scale))

	# build a matrix consisting of all values of
	# exp(2 pi i xi x), where x ranges over all x-values,
	# and xi ranges over all centers of the Cantor set.
	exponents = np.exp(2*np.pi*1j*np.transpose(centers)*x_values)

	print("finished calculating exponentials")

	# use matrix algebra to compute the exponential sums
	# sum_xi exp( 2 pi i xi x ) for each value x.
	y_ones = np.ones((1,2**scale))
	exponential_sums = y_ones*exponents

	print("finished calculating exponential sums")

	# get the y-values of the horizontal line y = 2^(i/2).
	cancellation_flat_line = (2**(0.5*scale))*np.ones(2*(3**scale))

	# get the y-values of the horizontal line y = 2^i.
	no_cancellation_flat_line = (2**scale)*np.ones(2*(3**scale))

	# get the values for the vertical lines x = -1
	negative_x_line = (-1.0)*np.ones(2**(scale + 1))
	positive_x_line = (+1.0)*np.ones(2**(scale + 1))
	all_y_values = np.arange(0, 2**(scale+1))

	# get values for y = 2**(i/2) 3**(i/2) / (|x| + 1)^{1/2}
	y_fit_line = (2**(0.5*scale))*(3**(0.5*scale))*np.power(np.absolute(x_values) + 1,-0.5)

	# get values for y = 2**(i/2) / (|x| + 1)
	y_fit_line_2 = (2**(0.5*scale))*np.power(1.0*np.absolute(x_values) + 1.0,-1)





	f1 = plt.figure(1)

	plt.title("Real Part of Exponential Sum")
	plt.axis([-3**scale, 3**scale, -2**scale, 2**scale])

	# Graph y = Re [ sum exp (2 pi i xi x) ]
	plt.plot(x_values.A1, exponential_sums.real.A1)

	# Graph y = 2^i
	plt.plot(x_values.A1, no_cancellation_flat_line, color="red", linewidth=2)

	# Graph y = 2^{i/2}
	plt.plot(x_values.A1, cancellation_flat_line, color="red", linewidth=2)

	# Graph x = -1
	plt.plot(negative_x_line, all_y_values, color="red", linewidth=2)

	# Graph x = +1
	plt.plot(positive_x_line, all_y_values, color = "red", linewidth=2)

	# Plot y = 2^{i/2} 3^{i/2} / <x>^{1/2}
	plt.plot(x_values.A1, y_fit_line.A1, color="red", linewidth=2)

	# Plot y = 2^{i/2} / <x>
	plt.plot(x_values.A1, y_fit_line_2.A1, color="green", linewidth=2)





	f2 = plt.figure(2)

	plt.title("Imaginary Part of Exponential Sum")
	plt.axis([-3**scale, 3**scale, -2**scale, 2**scale])

	# Graph y = Im [ sum exp (2 pi i xi x) ]
	plt.plot(x_values.A1, exponential_sums.imag.A1)

	# Graph y = 2^i
	plt.plot(x_values.A1, no_cancellation_flat_line, color="red", linewidth=2)

	# Graph y = 2^{i/2}
	plt.plot(x_values.A1, cancellation_flat_line, color="red", linewidth=2)

	# Graph x = -1
	plt.plot(negative_x_line, all_y_values, color="red", linewidth=2)

	# Graph x = +1
	plt.plot(positive_x_line, all_y_values, color = "red", linewidth=2)

	# Plot y = 2^{i/2} 3^{i/2} / <x>^{1/2}
	plt.plot(x_values.A1, y_fit_line.A1, color="red", linewidth=2)

	# Graph y = 2^{i/2} / <x>
	plt.plot(x_values.A1, y_fit_line_2.A1, color="green", linewidth=2)





	plt.show()

graph_oscillation(8)