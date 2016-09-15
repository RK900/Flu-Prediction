# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 19:43:52 2016

@author: rohankoodli
"""

from Bio import SeqIO

new = list(SeqIO.parse('file.fasta','fasta'))

new = []

for i in range(len(records)):
    if len(records[i].seq) == 1701:
        new.append(records[i])
X0 = []

#adding to X and y

for i in range(0,len(new)-1):
    X0.append(new[i].seq)
    
#print len(X0)

y0 = []
for j in range(1,len(new)):
    y0.append(new[i].seq)

#print len(y0)


X1 = []

from Encoding_v2 import *

for k in range(len(X0)):
    encoded_X = encode_bases_np(X0[k])
    X1.append(encoded_X)
    
y1 = []
for l in range(len(y0)):
    encoded_y = encode_bases_np(y0[l])
    y1.append(encoded_y)

#print (X1[0])
#print len(y1)


X2 = []
y2 = []
for i in range(len(X0)):
    encoded_X = encode_bases_5(X0[i])
    X2.append(encoded_X)

for i in range(len(y0)):
    encoded_y = encode_bases_5(X0[i])
    y2.append(encoded_y)
    
#print type(X2[0]),type(X1[0]),type(y2[0]),type(y1[0])

#print X2[0]
#print y2[0]
#y2 = [[10,0,0,1,1],[10,0,0,1,1],[10,0,0,1,1],[10,0,0,1,1],[10,0,0,1,1],[10,0,0,1,1],[10,0,0,1,1],[10,0,0,1,1],[10,0,0,1,1],[10,0,0,1,1],[10,0,0,1,1],[10,0,0,1,1],[10,0,0,1,1],[10,0,0,1,1]]

import numpy as np

a = np.array(X2)
b = np.array(y2)

test = encode_bases_5(records[0].seq)

from sklearn import tree
dtr = tree.DecisionTreeRegressor()
dtr.fit(X2,y2)
a = dtr.predict(test)
known = encode_bases_5(records[1].seq)



from sklearn import cross_validation

dtrscores = cross_validation.cross_val_score(dtr,X2,y2)
print 'decision trees',dtrscores

from sklearn import ensemble
rfr = ensemble.RandomForestRegressor()
rfr.fit(X2,y2)

rfrscores = cross_validation.cross_val_score(rfr,X2,y2)
print 'random forests: ',rfrscores


#This is a simulation of the different X and y for the algorithm
#Tto test what model will work with the flu strains

Xt = [[12323213,32423423,2342342],[23423424,234234,67567567],[23947287,298742,2987420]]
yt = [[29872983,55993938,3876453],[87928473,246421,66426969],[83919381,987833,5432222]]



from sklearn import neighbors
knr = neighbors.KNeighborsRegressor(algorithm='ball_tree')
knr.fit(X2,y2)
knrscores = cross_validation.cross_val_score(knr,X2,y2,cv=3)
print 'Kneighbors: ',knrscores

X_train,X_test,y_train,y_test = cross_validation.train_test_split(X2,y2,test_size=0.9,random_state=5)

dtr2 = tree.DecisionTreeRegressor()
dtr2.fit(X_train,y_train)
print 'DTR cvtts scores', dtr.score(X_test,y_test)

print a
print known
print(str.format('{0:.3f}', a[0][1]))
print(str.format('{0:.3f}', known[1]))




#Tested: GaussianNB,SVR,SVC,knn(brute force,kd tree, ball tree)
'''
X_train,X_test,y_train,y_test = cross_validation.train_test_split(X2,y2,test_size=0.6)
dtr.fit(X_train,y_train)
print dtr.score(X_test,y_test)



value error:
the lists are of different lengths
like lengths 1701, 1654, 1734 cause different lengths of the lists

give genotype as X and phenotype as y - to be done
'''


    