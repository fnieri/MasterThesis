import matplotlib.pyplot as plt
import numpy as np

from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

from scipy.stats import truncnorm

dMax = 6  
x = np.linspace(0, dMax + 5, 500) 

mean = 0
std_dev = 2

x = np.linspace(0, dMax + 3, 500)

a, b = (0 - mean) / std_dev, (dMax - mean) / std_dev
trunc_normal = truncnorm(a, b, loc=mean, scale=std_dev)

cdf_values = trunc_normal.cdf(x)
cdf_at_dMax = trunc_normal.cdf(dMax)
normalized_cdf = np.where(x <= dMax, 0.8 * cdf_values / cdf_at_dMax, 0.8)

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(x, normalized_cdf, label='ΔQ')
plt.axvline(x=dMax, color='red', linestyle='--', label='dMax')
plt.xlabel('Time Delay')
plt.ylabel('ΔQ(x)')
plt.ylim(0, 1)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

