from sklearn.datasets import load_iris
iris = load_iris()
print(iris.feature_names)
print(iris.target_names)
print(iris.data[0]) #this is the measurments for the first flower
print(iris.target[0]) 