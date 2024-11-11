# messing with Scikit Learn
# Author: Andre

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data="iris.csv"

irisdf = pd.read_csv(data)

print(irisdf.head(3))

# Choosing the column names that we want to work on
colnames=["sepal length", "sepal width", "petal length", "petal width" ]
# choosing our X 
x = irisdf[colnames]
# choosing our Y
y = irisdf['class']

# Checking the correlation of x
print(x.corr())
sns.lineplot(x.corr())
plt.show()

# Pick a classifier
# importing Decision tree
from sklearn.tree import DecisionTreeClassifier
estimator = DecisionTreeClassifier()
# Use it
estimator.fit(x,y)
print(estimator.predict([[1.2,2.3,3.3,1.3]]))
print(estimator.score(x,y))

# importing kn
from sklearn.neighbors import KNeighborsClassifier
estimator = KNeighborsClassifier()
# use it
estimator.fit(x,y)
print(estimator.predict([[1.2,2.3,3.3,1.3]]))
print(estimator.score(x,y))

