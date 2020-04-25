import numpy as np                # module for math arrays
import matplotlib.pyplot as plt   # module for plotting

import sys      # for accessing the command line parameters

data = np.loadtxt(sys.argv[1], usecols=[2,3])


# separate data
saxis = data[:,0] * 1000         # semi major axis in meter
torb  = data[:,1] * 24 * 60 * 60 # orbital period in 

# calculate the mass

# calculate the kepler constant for all moons
c = torb**2/saxis**3             # we can use the arrays directly

g = 6.67408e-11                  # the gravitational constant in m^3 kg^-1 s^-2

m = 4*(np.pi**2)/(g*c)           # calculate the mass for all moons

m = m / 1e26                     # downscale for printing
print('M =', m.mean(), ' +/-', m.std(), ' 10^26 kg')