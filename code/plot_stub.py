import matplotlib.pyplot as plt
import pandas as pd


def remove_outliers(series):
    Q1 = series.quantile(0.05)
    Q3 = series.quantile(0.85)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return series[(series >= lower_bound) & (series <= upper_bound)]


filenames = ["start_span.csv", "with_span.csv", "fail_span.csv"]
labels = []
cleaned_data = []
names = ["start/end{_span}", "with_span", "start/fail{_span}"]
for file, name in zip(filenames, names):
    df = pd.read_csv(file)
    cleaned_series = remove_outliers(df["Time(micros)"])
    cleaned_data.append(cleaned_series)
    labels.append(name)

plt.boxplot(cleaned_data, labels=labels)
plt.title("Execution time for adapter (25000 requests)")
plt.ylabel("Time (µs)")
plt.grid(True)

plt.show()
