import numpy as np
import matplotlib.pyplot as plt

t0 = 10

# Define the function to be transformed
def f(x,t): return np.exp(-100*(x/L)*(x/L))*np.exp(1j*t*np.abs(x))
    # np.ones(x.shape)

def expi(x): return np.exp(2.0*np.pi*1j*x)

# Domain of f that we are isolating
#   We only study the behaviour of f on for inputs in [-L,L]
#   Sampled at n points spaced out by dx
L = 40.0
n = 2**11
dx = 2*L/n
x = np.arange(-L, L, dx)

# dfft is the discrete inverse Fourier transform of the
#   n samples of f. The kth value in f_hat will thus be equal to
#       sum_{m = 0}^{n-1} f(-L + m dx) exp ( - 2 pi i k m / n )
#   This should be a good approximation of
#       (1 / dx) int_{-L}^L f(x) exp ( - 2 pi i k (x + L) / n dx ) 
#   This is equal to
#       (1 / dx) e^{ - 2 pi i (k / 2) } f^( k / 2 L )
#   This makes sense, since we treated f as a function on [-L,L]
#   so it's Fourier transform can only be observed at integer
#   multiples of 1/2L. Since we are treating f as locally constant
#   at the scale dx, we can only access the frequencies of f up
#   to (1 / dx).
dfft = np.fft.ifft(f(x,t0))

# Normalizing dfft gives the Fourier transform
# The kth value of this array is equal to f^( k / 2L )
f_hat = dx*expi(0.5*np.arange(0,n))*dfft

f_hat_copy = f_hat[::-1]

double_sided_f_hat = np.concatenate((f_hat_copy, f_hat))
print(len(double_sided_f_hat))

double_sided_range = np.arange(-1/dx, 1/dx, 1.0/n/dx)

print(len(double_sided_range))

# Plot the results
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))

ax1.plot(x, np.real(f(x,t0)))
ax1.set_title('f(x)')
ax1.set_xlabel('x')
ax1.set_ylabel('f(x)')

ax2.plot(double_sided_range, double_sided_f_hat)
ax2.set_title('Inverse Fourier Transform of f(x)')
ax2.set_xlabel('x')
ax2.set_ylabel('f_inv(x)')

plt.show()



"""

# Define the range of the Fourier transform

# We look at the Fourier coefficients on [-T, T]
# We sample the Fourier transform at frequencies spaced out by dt.

T = 4.0
m = 512
dt = 2*T/m
t = np.arange(-T, T, dt)

# Compute the Fourier coefficients using the FFT algorithm
#

F = np.fft.fftshift(np.fft.fft(f(x,1)))

F = np.zeros((m, n), dtype=complex)

for j in range(m):
    F[j,:] = np.fft.fftshift(np.fft.fft(f(x, 1)))

# Compute the frequencies associated with each coefficient
w = 2*np.pi*np.fft.fftfreq(n, dx)

# Plot the function and its Fourier transform
fig, ax = plt.subplots(2, 1, figsize=(8, 8))

ax[0].plot(x, np.real(f(x, 20)), 'k-')
ax[0].set_xlabel('x')
ax[0].set_ylabel('Re(f(x, 1))')

ax[1].imshow(np.abs(F), aspect='auto', extent=[-L, L, -np.max(w), np.max(w)])
ax[1].set_xlabel('x')
ax[1].set_ylabel('w')
plt.show()

"""