
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import mlab

r=np.arange(-5, 5, 0.01)
mu = 0
sigma = 1
plt.plot(r, mlab.normpdf(r, mu, sigma), color='b')

plt.annotate(r'$\sigma=1$', xy=(1, mlab.normpdf(1,mu,sigma)), xytext=(+10,+30), textcoords='offset points', fontsize=16, arrowprops=dict(arrowstyle='->'))

plt.show()