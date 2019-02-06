import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()
test_idx = [0,50,100] # remove one of each type of flower so that they can be used for testing

train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx,axis = 0)

test_target = iris.target[test_idx]

test_data = iris.data[test_idx] 

clf = tree.DecisionTreeClassifier()
clf.fit(train_data,train_target)


print(test_target) # will prin three values each correspond to a type of flower
print(test_data) #this prints out an array of arrays of the 0th 50th and 100th indexes
print (clf.predict(test_data))
