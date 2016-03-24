# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 22:05:13 2016

@author: Rohan Koodli
"""

from Bio import SeqIO

# importing 3861 sequences
new = list(SeqIO.parse('file.fasta','fasta'))
print type(records)
X0 = []

#adding to X and y

for i in range(0,len(records)-1):
    X0.append(records[i].seq)
    
print len(X0)

y0 = []
for j in range(1,len(records)):
    y0.append(records[i].seq)

print len(y0)


X = []

from Encoding import *

for k in range(len(X0)):
    encoded_X = encode_bases(X0[k])
    X.append(encoded_X)
    
y = []
for l in range(len(y0)):
    encoded_y = encode_bases(y0[l])
    y.append(encoded_y)

#print (X)
#print (y)

import numpy as np

from sklearn import cross_validation
from sklearn import tree
dtr = tree.DecisionTreeRegressor()
X_train,X_test,y_train,y_test = cross_validation.train_test_split(X,y,test_size=0.5,random_state=5)

dtr.fit(X_train,y_train)
print dtr.score(X_test,y_test)

#predicting

#cv = cross_validation.ShuffleSplit(n_iter=3,test_size=0.3,random_state=0)

dtr = tree.DecisionTreeRegressor()
dtr.fit(X,y)
scores = cross_validation.cross_val_score(dtr,X,y,cv=3)
print 'scores: ',scores


'''
from sklearn import ensemble

rfr = ensemble.RandomForestRegressor()
rfr.fit(X,y)
print cross_validation.cross_val_score(rfr,X,y,cv=5)
'''

'''
from sklearn import datasets
import numpy as np

iris = datasets.load_iris()
X,y = iris.data,iris.target

from sklearn.tree import DecisionTreeClassifier
dtc = DecisionTreeClassifier()

dtc.fit(X,y)
print dtc.score(X,y)

print X.shape
print type(y)




[[111],[111],[111]]
a = np.matrix([[1,2,3],[4,5,6]])
aa = np.matrix([[1,1,1],[2,2,2]])
b = np.matrix([[3]])
bb = np.matrix([[6]])
X = [a,aa]
y = [b,bb]

dtc.fit(X,y)
'''