import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the formatted CSV
df = pd.read_csv("formatted.csv")

# Step 2: Group by 'type' and 'obs'
grouped = df.groupby(['type', 'obs'])['time'].agg(['mean', 'std']).reset_index()

# Step 3: Split into comp and gui
comp = grouped[grouped['type'] == 'comp']
gui = grouped[grouped['type'] == 'gui']

# Ensure both have the same obs values
merged = pd.merge(comp, gui, on='obs', suffixes=('_comp', '_gui'))

# Step 4: Compute the sum of the means
merged['sum_mean'] = merged['mean_comp'] + merged['mean_gui']

# Step 5: Plotting
plt.figure(figsize=(12, 7))

# Plot comp with error bars
plt.errorbar(merged['obs'], merged['mean_comp'], yerr=merged['std_comp'],
             fmt='o-', label='Computing QPointFs', capsize=5)

# Plot gui with error bars
plt.errorbar(merged['obs'], merged['mean_gui'], yerr=merged['std_gui'],
             fmt='s--', label='Updating GUI', capsize=5)

# Plot sum of means
plt.plot(merged['obs'], merged['sum_mean'], 'k-.', label='Sum of two means')

# Customize plot
plt.title("Mean time of computing vectors of QPointF and displaying observed ΔQ series")
plt.xlabel("Bins")
plt.ylabel("Time(µs)")
plt.xticks([50, 100, 200, 300, 400, 500, 600, 700, 800, 800, 900, 1000])
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()
