import pandas
import pylab as plt

data = pandas.read_csv("dataploter.txt")
data.plot(x='x', y='y', kind='scatter')
plt.show()