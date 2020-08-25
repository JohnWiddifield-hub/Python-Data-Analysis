# Author: James Biondi
# DATA VISUALIZATION on the Iris Data Set
# 8/22/2020

import csv
import numpy as np
import matplotlib.pyplot as plt
import pylab
import scipy.stats as stats
import pandas as pd

arr = []  # Holds list of each row from the csv file
with open("data/iris.csv") as csv_file:
    csv_read = csv.reader(csv_file, delimiter=",")
    i = 0
    for row in csv_read:
        if i != 0:
            arr.append(row)
        i += 1

# sorting each feature into its own list
sepal_len = []
sepal_wid = []
petal_len = []
petal_wid = []
for x in arr:
    sepal_len.append(float(x[0]))
    sepal_wid.append(float(x[1]))
    petal_len.append(float(x[2]))
    petal_wid.append(float(x[3]))

# Organizing by class attribute
# Setosa: Red, Versicolour: Blue, Virginica: Green
sl_setosa = sepal_len[0:49]
sl_versi = sepal_len[50:99]
sl_virg = sepal_len[100:149]

sw_setosa = sepal_wid[0:49]
sw_versi = sepal_wid[50:99]
sw_virg = sepal_wid[100:149]

pw_setosa = petal_wid[0:49]
pw_versi = petal_wid[50:99]
pw_virg = petal_wid[100:149]


#  Compute mean, median, standard deviation, range, 25 50 and 75th percentile sepal length
print "Mean Sepal Length: ", np.mean(sepal_len)
print "Median Sepal Length: ", np.median(sepal_len)
print "Standard Deviation of Sepal Length: ", np.std(sepal_len)
print "Sepal Length Range: ", np.max(sepal_len) - np.min(sepal_len)
print "25th Percentile Sepal Length: ", np.percentile(sepal_len, 25)
print "50th Percentile Sepal Length: ", np.percentile(sepal_len, 50)
print "75th Percentile Sepal Length: ", np.percentile(sepal_len, 75)
print ""

#  Compute mean, median, standard deviation, range, 25 50 and 75th percentile sepal width
print "Mean Sepal Width: ", np.mean(sepal_wid)
print "Median Sepal Width: ", np.median(sepal_wid)
print "Standard Deviation of Sepal Width: ", np.std(sepal_wid)
print "Sepal Width Range: ", np.max(sepal_wid) - np.min(sepal_wid)
print "25th Percentile Sepal Width: ", np.percentile(sepal_wid, 25)
print "50th Percentile Sepal Width: ", np.percentile(sepal_wid, 50)
print "75th Percentile Sepal Width: ", np.percentile(sepal_wid, 75)
print ""

#  Compute mean, median, standard deviation, range, 25 50 and 75th percentile petal length
print "Mean Petal Length: ", np.mean(petal_len)
print "Median Petal Length: ", np.median(petal_len)
print "Standard Deviation of Petal Length: ", np.std(petal_len)
print "Petal Length Range: ", np.max(petal_len) - np.min(petal_len)
print "25th Percentile Petal Length: ", np.percentile(petal_len, 25)
print "50th Percentile Petal Length: ", np.percentile(petal_len, 50)
print "75th Percentile Petal Length: ", np.percentile(petal_len, 75)
print ""

#  Compute mean, median, standard deviation, range, 25 50 and 75th percentile petal width
print "Mean Petal Width: ", np.mean(petal_wid)
print "Median Petal Width: ", np.median(petal_wid)
print "Standard Deviation of Petal Width: ", np.std(petal_wid)
print "Petal Width Range: ", np.max(petal_wid) - np.min(petal_wid)
print "25th Percentile Petal Width: ", np.percentile(petal_wid, 25)
print "50th Percentile Petal Width: ", np.percentile(petal_wid, 50)
print "75th Percentile Petal Width: ", np.percentile(petal_wid, 75)

# Creating a box-and-whisker plot
# Resource used to learn matplotlib: https://www.geeksforgeeks.org/box-plot-in-python-using-matplotlib/
box_data = [sepal_len, sepal_wid, petal_len, petal_wid]
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111)
bp = ax.boxplot(box_data, patch_artist=True, notch="True", vert=0)
plt.title("Sepal and Petal Lengths and Widths")
ax.set_yticklabels(["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"])
plt.show(bp)

# Creating histogram comparing sepal width and petal length
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
ax.hist([sepal_wid, petal_len], bins=8)
ax.set_xlim(0, 7.5)
ax.set_ylabel("Count")
ax.set_xlabel("Size (in cm)")
plt.tight_layout()
plt.title("Sepal Width vs. Petal Length")
plt.show()

# Creating data scatter matrix
df = pd.DataFrame(
    {
        "Sepal Length": sepal_len,
        "Sepal Width": sepal_wid,
        "Petal Length": petal_len,
        "Petal Width": petal_wid,
    }
)

df.head()
pd.plotting.scatter_matrix(df, diagonal="kde")

# Creating a 3D Scatter plot of sepal length, sepal width, and petal width
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")
ax.scatter(sl_setosa, sw_setosa, pw_setosa, c="r", marker="o")
ax.scatter(sl_versi, sw_versi, pw_versi, c="b", marker="o")
ax.scatter(sl_virg, sw_virg, pw_virg, c="g", marker="o")
ax.set_xlabel("Sepal Length")
ax.set_ylabel("Sepal Width")
ax.set_zlabel("Petal Width")
plt.title("Sepal Length vs. Sepal Width vs. Petal Width")
plt.show()

# Creating quantile-quantile plot for sepal length and petal length
stats.probplot(sepal_len, dist="norm", plot=pylab)
pylab.show()
stats.probplot(petal_len, dist="norm", plot=pylab)
pylab.show()
