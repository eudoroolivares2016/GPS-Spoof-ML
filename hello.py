from sklearn import tree
#import keras
features = [[140,20],[130,11],[180,0],[190,0],[300,0]]
labels = ["Type 1","Type 1","Type 2","Type 2","Type 2"]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)
print(clf.predict([[200,0]]))
#machine learning algorithm that takes two features and finds a 
#pattern between them takes in two features
# features 