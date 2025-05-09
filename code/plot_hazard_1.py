
# Re-import libraries after code execution environment reset
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import truncnorm
import random

random.seed("sossio")


# Parameters
mean = 5
std_dev = 2
dMax = 10
x = np.linspace(0, dMax + 5, 500)

# Truncated normal distribution
a, b = (0 - mean) / std_dev, (dMax - mean) / std_dev

# Two versions of the truncated normal with slightly different means
means = [4, 6]  # left-shifted and right-shifted versions

# Step function
step_y = np.array([0.25, 0.5, 0.75, 0.95])



means = [2.5, 5.3]  # Further adjust for stronger separation and better intersection

# Plotting
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

for i, m in enumerate(means):
    trunc_normal = truncnorm((0 - m) / std_dev, (dMax - m) / std_dev, loc=m, scale=std_dev)
    cdf = trunc_normal.cdf(x)
    cdf_max = trunc_normal.cdf(dMax)
    normalized_cdf = np.where(x <= dMax, 0.8 * cdf / cdf_max, 0.8)

    # Use fixed step_y and x values based on central mean for comparison
    central_mean = 5
    central_trunc = truncnorm((0 - central_mean) / std_dev, (dMax - central_mean) / std_dev, loc=central_mean, scale=std_dev)
    step_x = central_trunc.ppf(step_y * central_trunc.cdf(dMax) / 0.8)
    step_function = np.zeros_like(x)
    for xi, yi in zip(step_x, step_y):
        step_function[x >= xi] = yi

    axs[i].plot(x, normalized_cdf, 'k-', label='Truncated Normal CDF')
    axs[i].plot(x, step_function, 'r-', label='Step Function')
    axs[i].set_xlabel('Time Delay')
    axs[i].set_ylabel('CDF')
    axs[i].set_ylim(0, 1)
    axs[i].legend()
    axs[i].grid(True)

axs[0].set_title('CDF Left of Step Function')
axs[1].set_title('CDF Intersecting Step Function')

plt.tight_layout()
plt.show()

