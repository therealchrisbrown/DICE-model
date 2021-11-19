import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt

# x = np.linspace(0, 1, 100)
# plot = plt.plot(x, np.exp(x))
# pts = np.random.uniform(0,1,(100, 2))
# pts[:, 1] *= np.e
# plot = plt.scatter(pts[:, 0], pts[:, 1])
# plot = plt.xlim([0,1])
# plot = plt.ylim([0, np.e])

# print(plot)



rs = npr.beta(a=0.5, b=0.5, size=1000)
graph = plt.hist(rs, bins=20, histtype='step', normed=True, linewidth=1)

print(graph)




# def rng(m=2**32, a=1103515245, c=12345):
#     rng.current = (a*rng.current + c) % m
#     return rng.current/m

# # setting the seed
# rng.current = 1

# array_df = [rng() for i in range(10)]

# print(array_df)