# My notation G_n^k is degree k, orthogonal to (1 - t^2)^{n/2 - 1}
# n/2 - 1 = alpha - 1/2
# alpha = (n-1)/2

#for n in range(R/8,8*R):
#	normalization_constant = 1 + float(n)/alpha
	# Each thing we add is O(n^{d-1}), so total must be O((2R)^d)
	# exp(- (x/R - 1)^2)

#	partial_summation_polynomial += np.exp(-(float(n)/R - 1)*(float(n)/R - 1))*normalization_constant*special.gegenbauer(n, alpha, monic = False)

# We should have that dim(H_n) = (d + n choose d) - ( d + n - 2 choose d ) = O(n^{d-1})
# Use Stirling's Formula

# Should be proportional to n^{d-1}.
# So each zonal polynomial has magnitude O(n^{d-1}) at each endpoint.
# As we sum up, the right endpoint should have magnitude O(R^d)
# whereas the left endpoint should see cancellation, and have magnitude O(R^{d-1}).

# Does this still imply local constancy? Probably
# Also graph y = R^d x^{2R}

import numpy as np
from scipy import special
import matplotlib.pyplot as plt

R = 20
d = 3
alpha = (float(d) - 1)/2

partial_summation_polynomial = np.poly1d([0])

x = np.linspace(-1, 1, 800)
y1 = np.zeros(x.size)
y2 = np.zeros(x.size)

# Dirichlet Summation
for n in range(R/2,2*R):
	normalization_constant = 1 + float(n)/alpha
	y1 +=  normalization_constant*special.gegenbauer(n, alpha, monic = False)(x)

# Smoothed Summation
for n in range(R/8,8*R):
	normalization_constant = 1 + float(n)/alpha
	y2 += np.exp(-(float(n)/R - 1)*(float(n)/R - 1))*normalization_constant*special.gegenbauer(n, alpha, monic = False)(x)

fig, ax = plt.subplots()
ax.plot(x, y1)
ax.plot(x, y2)

ax.set_title("Summation of Gegenbauer Polynomials With R = " + str(R))
plt.show()