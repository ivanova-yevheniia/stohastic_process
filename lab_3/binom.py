import scipy
import pandas as pd
import matplotlib.pyplot as plt
n = 6
p = 0.45

dist_class = scipy.stats.binom(n=6, p = 0.45)

#теоретичні ймовірності
values = [i for i in range(n+1)]
theor_probs = [ round(dist_class.pmf(i), 5) for i in values ]
theor_ser = pd.Series(data = theor_probs, index = values)
#print(theor_ser)

sample = [2, 3, 4, 2, 2, 5, 3, 2, 3, 5, 3, 4, 1, 2, 1, 3, 4, 2, 4, 1, 2, 4, 4, 1, 4, 2, 2, 2, 2, 1, 3, 2, 3, 3, 3, 2, 2,
 1, 2, 5, 3, 2, 1, 5, 2, 2, 5, 1, 3, 3]
#sample = dist_class.rvs(size = 50)
sample_ser = pd.value_counts(sample)/len(sample)
print(sample)
print(sample_ser)

united = pd.concat([theor_ser, sample_ser], axis='columns').fillna(0).rename({0:'theor_prob',\
                                                                             1:"sample_prob"}, axis='columns')

print(united)
import seaborn as sns
sns.barplot(united, x = united.index, y = 'theor_prob', color='blue', alpha=1)
sns.barplot(united, x = united.index, y = 'sample_prob', color='skyblue', alpha=0.8)

plt.show()

