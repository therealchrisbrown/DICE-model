import numpy.random as npr
import matplotlib.pyplot as plt
import pandas as pd

rs = npr.normal(loc=0.0, scale=0.5, size=10000)
#graph = plt.hist(rs, bins=20, histtype='step', normed=True, linewidth=1)
rs_df = pd.DataFrame(rs)

rs_df.to_csv('./results_monte-carlo/monte-carlo.csv', index=False)

print(rs_df)