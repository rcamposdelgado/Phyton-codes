# do not forget to put the following '%matplotlib inline'
# within Jupyter notebooks. If you forget it, external
# windows are opened for the plot but we would like to
# have the plots integrated in the notebooks
# The line only needs to be give ONCE per notebook!
%matplotlib inline
# Verification of scipys Bessel function implementation
# - asymptotic behaviour for large x

import scipy.special as ss
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# for nicer plots, make fonts larger and lines thicker
matplotlib.rcParams['font.size'] = 12
matplotlib.rcParams['axes.linewidth'] = 2.0

def jn_asym(n,x):
    """Asymptotic form of jn(x) for x>>n"""

    return np.sqrt(2.0 / np.pi / x) * \
           np.cos(x - (n * np.pi / 2.0 + np.pi / 4.0))

# We choose to plot between 0 and 50. We exclude 0 because the
# recursion relation contains a division by it.
x = np.linspace(0., 50, 500)

# plot J_0, J_1 and J_5.
for n in [0, 1, 5]:
    plt.plot(x, ss.jn(n, x), label='$J_%d$' % (n))

# and compute its asymptotic form (valid for x>>n, where n is the order).
# must first find the valid range of x where at least x>n.
x_asym = x[x > n]
plt.plot(x_asym, jn_asym(n, x_asym), linewidth = 2.0,
         label='$J_%d$ (asymptotic)' % n)

# Finish the plot and show it
plt.title('Bessel Functions')
plt.xlabel('x')
# note that you also can use LaTeX for plot labels!
plt.ylabel('$J_n(x)$')

# horizontal line at 0 to show x-axis, but after the legend
plt.legend()
plt.axhline(0)