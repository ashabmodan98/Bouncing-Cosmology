
import numpy as np
import matplotlib.pyplot as plt
import math  # from math import exp and using exp() insted of math.exp() is better if only one function is required
#csfont = {'fontname':'Times New Roman'}
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = "Computer Modern Roman"

def g(p, phi, b_g):
    return 2 / (math.exp(-1 * math.sqrt(2 / p) * phi) + math.exp(b_g * math.sqrt(2 / p) * phi))


def V(q, phi, b_V):
    return -2 / (math.exp(-1 * math.sqrt(2 / q) * phi) + math.exp(b_V * math.sqrt(2 / q) * phi))


V_0 = 10**(-7)
g_0 = 1.1
b_g = 0.5
b_V = 5
p = 0.01
q = 0.1

n1 = 700
phi = np.linspace(-2, 3, n1)
g1 = np.empty(n1)
V1 = np.empty(n1)
g2 = np.empty(n1)
V2 = np.empty(n1)

for i in range(n1-1):  # <-----------!!!!WRONG HERE!!!
    g1[i] = g(p, phi[i], b_g)
    V1[i] = V(q, phi[i], b_V)
    g2[i] = g1[i] * g_0
    V2[i] = -V1[i] * V_0

fig, (ax) = plt.subplots(nrows=1)
ax.plot(phi, g1, 'b', phi, V1, 'k--')
ax.set_xlabel('$\phi$')
ax.set_xlim([-1.5, 1])
ax.set_ylim([-1.5, 1.5])
plt.text(0.0927, -0.527, '$V(\phi)/V_0$')
plt.text(0.198, 0.730, '$g(\phi)/g_0$')

ax.set_yticklabels([])
ax.set_xticklabels([])
ax.spines['left'].set_position('zero')   #sets the y axis at zero
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.show()

#plt.text(0.0927, -0.527, 'V(\u03D5)/V\u2080')
#plt.text(0.198, 0.730, 'g(\u03D5)/g\u2080')


#plt.plot(phi, g2, 'b', phi, V2, 'k--')
# plt.ylim([10**(-38), 1]) #<----max(g2) > 1
#plt.xlim([-2, 3])  # Not needed as phi is from -2 to 3 any way.
#plt.show()

#plt.plot(phi, V2)
#plt.show()

V2 *= 10**7
#plt.plot(phi, g2, 'b', phi, V2, 'k--')
#plt.xlim([-2, 3])
#plt.show()
