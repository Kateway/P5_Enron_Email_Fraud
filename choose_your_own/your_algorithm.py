#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from sklearn.metrics import accuracy_score
from sklearn.neighbors.nearest_centroid import NearestCentroid
from time import time

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

# Choose a smaller dataset
features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]

clf = NearestCentroid()
t0 = time()
clf = clf.fit(features_train, labels_train)
print "Training time:", round(time() - t0, 2), "s"

accurary = clf.score(features_test, labels_test)
t1 = time()
pred = clf.predict(features_test)
print "Predicting time:", round(time() - t1, 2), "s"

acc = accuracy_score(pred, labels_test)
print "Accuracy:", acc








try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
