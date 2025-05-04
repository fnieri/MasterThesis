import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("../data/results.csv")


# Filter to only equal sizes
df = df[df["lhs_size"] == df["rhs_size"]].copy()

# Group stats
stats = df.groupby("lhs_size").agg({
    "naive_time_us": ["mean", "std"],
    "fft_time_us": ["mean", "std"]
}).reset_index()

# Plot setup
plt.figure(figsize=(10, 6))
sizes = stats["lhs_size"]
x = np.arange(len(sizes))

# --- Naive Method ---
naive_mean = stats[("naive_time_us", "mean")]
naive_std = stats[("naive_time_us", "std")]
plt.plot(x, naive_mean,
         label="Naive",
         color="blue",
         linestyle="--",  # Dashed line
         marker="o",      # Circle markers
         linewidth=2)
plt.fill_between(x,
                 naive_mean - naive_std,
                 naive_mean + naive_std,
                 color="blue",
                 alpha=0.2)  # Semi-transparent

# --- FFT Method ---
fft_mean = stats[("fft_time_us", "mean")]
fft_std = stats[("fft_time_us", "std")]
plt.plot(x, fft_mean,
         label="FFT",
         color="red",
         linestyle=":",  # Dotted line
         marker="s",     # Square markers
         linewidth=2)
plt.fill_between(x,
                 fft_mean - fft_std,
                 fft_mean + fft_std,
                 color="red",
                 alpha=0.2)

# --- Accessibility & Styling ---
plt.xticks(x, sizes)
plt.xlabel("Number of bins", fontsize=12)
plt.ylabel("Time (μs)", fontsize=12)
plt.title("Naive vs FFT Convolution Performance on 2 ΔQs (Mean ± Std Dev)", fontsize=14, pad=20)

plt.yticks([i * 500 for i in range(24)])  # 10 ticks from 0 to max

# Grid and legend
plt.grid(True, linestyle="--", alpha=0.4)
plt.legend(fontsize=12)

# Axes start at 0
plt.xlim(-0.5, len(sizes) - 0.5)
plt.ylim(0, 12000)

# Annotate max points (optional)
max_naive_idx = np.argmax(naive_mean)
max_fft_idx = np.argmax(fft_mean)
plt.annotate(f"Max: {naive_mean[max_naive_idx]:.0f}μs",
             (x[max_naive_idx], naive_mean[max_naive_idx]),
             textcoords="offset points",
             xytext=(0,10), ha="center")
plt.annotate(f"Max: {fft_mean[max_fft_idx]:.0f}μs",
             (x[max_fft_idx], fft_mean[max_fft_idx]),
             textcoords="offset points",
             xytext=(0,-15), ha="center")

plt.tight_layout()
plt.savefig("performance_plot.png", dpi=300, bbox_inches="tight")
plt.show()
