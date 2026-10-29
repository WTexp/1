import numpy as np
import matplotlib.pyplot as plt

X = np.array([[1,1], [2,1], [8,8], [9,8]])
W = np.array([[1.,1.], [8.,8.]])
clusters = [[], []]
alpha = 0.5

for i, x in enumerate(X):
    d = np.sqrt(((W-x)**2).sum(axis=1))
    bmu = np.argmin(d)
    clusters[bmu].append(chr(65+i))
    W[bmu] += alpha * (x-W[bmu])

print("Final weights:", W)
print("Cluster 1:", clusters[0])
print("Cluster 2:", clusters[1])

for c in range(2):
    p = X[[ord(n)-65 for n in clusters[c]]]
    plt.scatter(p[:,0], p[:,1], label=f"Cluster {c+1}")
    for n, (x,y) in zip(clusters[c], p):
        plt.text(x, y, n)

plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.grid()
plt.show()