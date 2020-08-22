import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# commands to type before running: pip install numpy
# next command: python -m pip install -U matplotlib
# next command: pip install pandas

df = pd.read_csv("parkinsons.csv")

fig, ax = plt.subplots()
scatPlot = ax.scatter(
    df["HNR"],
    df["NHR"],
    s=1
)

ax.set_xlabel("HNR")
ax.set_ylabel("NHR")
ax.set_title("HNR and NHR data")


dataArr = df.to_numpy()[:, [16, 15]]
NHRmean = np.mean(dataArr[:, 1])
HNRmean = np.mean(dataArr[:, 0])
P = (HNRmean, NHRmean)
print(f"Data point P = {P}")

euclDistances  = []
manhatBlockDistances = []
minkowDistances = []
chebyDistances = []
cosineDistances = []

euclMins = []
manhatMins = []
minkowMins = []
chebyMins = []
cosineMins = []


for rowInd in range(0, 195):
    euclDist = np.linalg.norm(P - dataArr[rowInd])
    euclDistances.append(euclDist)

    manhatBlockDistances.append((abs(P[0] - dataArr[rowInd][0]) + abs(P[1] - dataArr[rowInd][1])))

    minkowDistances.append((abs(dataArr[rowInd][0] - P[0])**6 + abs(dataArr[rowInd][1] - P[1])**6)**(1/6))

    chebyDistances.append(max(abs(P[0] - dataArr[rowInd][0]), abs(P[1] - dataArr[rowInd][1])))

    dotProd = (P[0] * dataArr[rowInd][0]) + (P[1] * dataArr[rowInd][1])
    d1 = ((P[0] * P[0]) + (P[1] * P[1]))**0.5
    d2 = ((dataArr[rowInd][0] * dataArr[rowInd][0]) + (dataArr[rowInd][1] * dataArr[rowInd][1]))**0.5
    cosineDistances.append(dotProd / (d1 * d2))

euclMins = np.argpartition(euclDistances, 5)
manhatMins = np.argpartition(manhatBlockDistances, 5)
minkowMins = np.argpartition(minkowDistances, 5)
chebyMins = np.argpartition(chebyDistances, 5)
cosineMins = np.argpartition(cosineDistances, 5)


print("Points with minimum Euclidean distance from P:")
for index in range(0, 5):
    print("\t(", np.round(dataArr[euclMins[index]][0], 5), ",",
          np.round(dataArr[euclMins[index]][1], 5), ")")

print("Points with minimum Manhattan block distance from P:")
for index in range(0, 5):
    print("\t(", np.round(dataArr[manhatMins[index]][0], 5), ",",
          np.round(dataArr[manhatMins[index]][1], 5), ")")

print("Points with minimum Minkowski distances with a power of 6 from P:")
for index in range(0, 5):
    print("\t(", np.round(dataArr[minkowMins[index]][0], 5), ",",
          np.round(dataArr[minkowMins[index]][1], 5), ")")

print("Points with minimum Chebyshev distance from P:")
for index in range(0, 5):
    print("\t(", np.round(dataArr[chebyMins[index]][0], 5), ",",
          np.round(dataArr[chebyMins[index]][1], 5), ")")

print("Points with minimum Cosine distance from P:")
for index in range(0, 5):
    print("\t(", np.round(dataArr[cosineMins[index]][0], 5), ",",
          np.round(dataArr[cosineMins[index]][1], 5), ")")

euclMins = np.argpartition(euclDistances, 10)
manhatMins = np.argpartition(manhatBlockDistances, 10)
minkowMins = np.argpartition(minkowDistances, 10)
chebyMins = np.argpartition(chebyDistances, 10)
cosineMins = np.argpartition(cosineDistances, 10)

plt.figure()
plt.xlabel("HNR")
plt.ylabel("NHR")
plt.title("Points Closest Using Euclidean Measure")
plt.scatter(P[0], P[1], s=5, c='red')

x = []
y = []
for point in range(0, 10):
    x.append(np.round(dataArr[euclMins[point]][0], 5))
    y.append(np.round(dataArr[euclMins[point]][1], 5))
plt.scatter(x, y, s=5, c='blue')

x = []
y = []
plt.figure()
plt.xlabel("HNR")
plt.ylabel("NHR")
plt.title("Points Closest Using Manhattan block Measure")
plt.scatter(P[0], P[1], s=5, c='red')
for point in range(0, 10):
    x.append(np.round(dataArr[manhatMins[point]][0], 5))
    y.append(np.round(dataArr[manhatMins[point]][1], 5))
plt.scatter(x, y, s=5, c='purple')

x = []
y = []
plt.figure()
plt.xlabel("HNR")
plt.ylabel("NHR")
plt.title("Points Closest Using Minkowski Measure W/ Power=6")
plt.scatter(P[0], P[1], s=5, c='red')
for point in range(0, 10):
    x.append(np.round(dataArr[minkowMins[point]][0], 5))
    y.append(np.round(dataArr[minkowMins[point]][1], 5))
plt.scatter(x, y, s=5, c='black')

x = []
y = []
plt.figure()
plt.xlabel("HNR")
plt.ylabel("NHR")
plt.title("Points Closest Using Chebyshev Measure")
plt.scatter(P[0], P[1], s=5, c='red')
for point in range(0, 10):
    x.append(np.round(dataArr[chebyMins[point]][0], 5))
    y.append(np.round(dataArr[chebyMins[point]][1], 5))
plt.scatter(x, y, s=5, c='orange')

x = []
y = []
plt.figure()
plt.xlabel("HNR")
plt.ylabel("NHR")
plt.title("Points Closest Using Cosine Measure")
plt.scatter(P[0], P[1], s=5, c='red')
for point in range(0, 10):
    x.append(np.round(dataArr[cosineMins[point]][0], 5))
    y.append(np.round(dataArr[cosineMins[point]][1], 5))
plt.scatter(x, y, s=5, c='orange')
plt.show()
print(dataArr[0])