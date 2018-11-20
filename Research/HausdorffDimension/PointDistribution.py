from matplotlib import pyplot as plt
from scipy.stats import gaussian_kde
import numpy as np
from collections import Counter
from math import log

M = 10
N = 5000

def producePoints(N,M,a,b):
    # S = NMk + 2N(b-a)m + m^2: 0 <= k, m <= N } subset of [N^2(3M+1)]

    # Test case: N = 2, M = 2, b - a = 1 should return
    # [ 0  4  8]
    # [ 5  9 13]
    # [12 16 20]

    X = np.indices([N+1,N+1,1])
    X[2] += 1

    # Now X[a][i][j][k] returns the a'th index of (i,j,k)

    A = np.array([[0,0,N*M/2], [0,1,N*(b-a)], [N*M/2,N*(b-a),0]])

    # The values can be expressed as the output of a quadratic form
    #            |0      0      (NM/2)| |k|
    #  |k  m  1| |0      1      N(b-a)| |m|
    #            |(NM/2) N(b-a) 0     | |1|
   
    # The correct output would be
    # B[i][j] = sum(X[a,i,j,0]*A[a,b]*X[b,i,j,0], a,b)
    # The sum, done pointwise, is very slow, so we express it via
    # matrix operations which are optimized.

    return (X.T.dot(A)*X.T).sum(axis=3).sum(axis=0)

    # This alternative calculation also works, but will be VERY slow
    #B = np.zeros([N,N], dtype=np.int64)
    #for i in range(0,N):
    #   for j in range(0,N):
    #       B[i][j] = sum(X[a][i][j][0]*A[a][b]*X[b][i][j][0] for a in range(0,3) for b in range(0,3))
    #   return B

a = 1
b = 2

for a in range(M/2,M/2+1):
    for b in range(a,M):
        S = producePoints(N,M,a,b)

        print("DONE POINT PRODUCTION")

        # A and B now index over all choices of k and m.
        [A,B] = np.meshgrid(np.arange(0,N+1), np.arange(0,N+1))

        # Now we form a list of all (k,m) tuples, and use it to form
        # the floating point values.
        A = A.ravel()
        B = B.ravel()

        # Proper locations
        T = S[A,B] + a*N*N*M + N*N*M*(b-a)*(b-a)
        U = list(T.astype(float)/N/M/N/M)
        #U.sort()
        #print("DONE SORTING")

        Udistinct = list(set(U))
        print(N,M,a,b,len(Udistinct), log(len(Udistinct))/log(N))

        #counter = Counter(U)
        #print(len(list(counter.elements())))
        #print(counter.most_common(20000))

        # Plot the values of the function as a temperature plot. This
        # is just a check to see how the distributions look.
        #plt.scatter(A.astype(np.float)/N/M,B.astype(np.float)/N/M, c=T.astype(np.float)/N/M)
        #plt.show()

        # The average distance between adjacent points in the list
        #print(sum((U[i+1] - U[i])^2 for i in range(0,(N+1)*(N+1)-1))/(N+1)/(N+1))

        # Print all the points we've found, along with the
        # values of k which define them.

        #for i in range(0,N+1):
        #    for j in range(0,N+1):
        #        print(float(T[i][j])/N/M)
        #        print("%d, %f, %f" % (A[i][j], B[i][j], float(T[i][j])/N/M))

        # Plot all the points on a single axis. Use the zoom in function
        # to see their distribution.
        #plt.scatter(np.arange(0,(N+1)*(N+1)),T)
        #plt.scatter(T, np.zeros((N+1)*(N+1)))
        #plt.show()

        # Make a frequency distribution, counting points over intervals of length N?

        #print(U)
        #density = gaussian_kde(U)
        #xs = np.linspace(0,1,300)
        #density.covariance_factor = lambda : .25
        #density._compute_covariance()
        #plt.plot(xs,density(xs))

        # Last thing was a smoothing of frequency distribution, now make a histogram?
        #Tlist = list(T)
        #plt.hist(Tlist, N*M*M*M)
#        NumGroupings = dict()
#        for i in range(N*M*M*M): NumGroupings[i] = 0
#        for t in Tlist: 
#            print(t)
#            NumGroupings[t/N] += 1
#        BIGGERLIST = []
#        for t in sorted(NumGroupings.keys()):
#            print(t)
#            BIGGERLIST.append(NumGroupings[t])
        # Plot NumGroupings?
        #print(NumGroupings)

#        plt.hist(BIGGERLIST)
#        plt.show()
