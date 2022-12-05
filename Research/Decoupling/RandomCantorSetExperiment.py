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
	# Graph up to 1/3^i
	centers = np.matrix(list(generate_centers(scale)))
#	centers = np.asmatrix(list(generate_centers(scale)), float))

	print("calculate centers")

	x_values = np.asmatrix(np.arange(- 3**scale, 3**scale))

#	print(np.shape(np.transpose(centers)))

	exponents = np.exp(2*np.pi*1j*np.transpose(centers)*x_values)
#	print(np.shape(exponents))

	print("computed exponents")

	y_ones = np.ones((1,2**scale))
#	print(np.shape(y_ones))

	y_values = y_ones*exponents

#	print(x_values.A1)
#	print(y_values.A1)

	# Plot the square root on y axis
	y_flat_line = (2**(0.5*scale))*np.ones(2*(3**scale))
	y_big_line = (2**scale)*np.ones(2*(3**scale))

	plt.title("Test")

	f1 = plt.figure(1)
#	plt.axis([-100,100, 0, 2**scale])
	plt.axis([-3**scale, 3**scale, 0, 2**scale])

	plt.plot(x_values.A1,y_values.real.A1)
	plt.plot(x_values.A1, y_flat_line, color="red", linewidth=2)
	plt.plot(x_values.A1, y_big_line, color="red", linewidth=2)

	all_y_values = np.arange(0, 2**(scale+1))
	plt.plot(-(1.5**scale)*np.ones(2**(scale+1)), all_y_values, color="red", linewidth=2)
	plt.plot(+(1.5**scale)*np.ones(2**(scale+1)), all_y_values, color = "red", linewidth=2)

	# Plot y = 2^{i/2} 3^{i/2} / x^{1/2}
	y_fit_line = (2**(0.5*scale))*(3**(0.5*scale))*np.power(np.absolute(x_values) + 1,-0.5)
	plt.plot(x_values.A1,y_fit_line.A1, color="red", linewidth=2)

	# H <= 2^{i/2} 3^{i/2} / X^{1/2}

	f2 = plt.figure(2)
#	plt.axis([-100,100, 0, 2**scale])
	plt.axis([-3**scale, 3**scale, 0, 2**scale])

	plt.plot(x_values.A1,y_values.imag.A1)
	plt.plot(x_values.A1, y_flat_line, color="red", linewidth=2)
	plt.plot(x_values.A1, y_big_line, color="red", linewidth=2)

	all_y_values = np.arange(0, 2**(scale+1))
	plt.plot(-(1.5**scale)*np.ones(2**(scale+1)), all_y_values, color="red", linewidth=2)
	plt.plot(+(1.5**scale)*np.ones(2**(scale+1)), all_y_values, color = "red", linewidth=2)

	# Plot y = 2^{i/2} 3^{i/2} / x^{1/2}
	# So should reach y = 2^{i/2} when x = 3^i
	plt.plot(x_values.A1,y_fit_line.A1, color="red", linewidth=2)

	plt.show()

graph_oscillation(10)