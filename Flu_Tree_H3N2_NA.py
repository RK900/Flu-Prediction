# -*- coding: utf-8 -*-
"""
Created on Sun Mar 06 13:46:30 2016

@author: Rohan Koodli
"""

'''
H3N2
NA
'''

from Bio import SeqIO

new = list(SeqIO.parse('file-NAprotein-H3N2.fasta','fasta'))


#print len(new[13])
X0 = []

#adding to X and y

for i in range(0,len(new)-1):
    X0.append(new[i].seq)
    
#print len(X0)

y0 = []
for j in range(1,len(new)):
    y0.append(new[i].seq)
    
from Encoding_v2 import encoding

X = []
for k in range(len(X0)):
    encoded_X = encoding(X0[k])
    X.append(encoded_X)
    
y = []
for l in range(len(y0)):
    encoded_y = encoding(y0[l])
    y.append(encoded_y)


from sklearn import tree
dtr = tree.DecisionTreeRegressor()
dtr.fit(X,y)

from sklearn import cross_validation
dtrscores = cross_validation.cross_val_score(dtr,X,y,cv=2)
print 'Decision Trees',dtrscores
print("Average Accuracy: %0.2f (+/- %0.2f)" % (dtrscores.mean()*100, dtrscores.std() *100))

from sklearn import ensemble
rfr = ensemble.RandomForestRegressor()
rfr.fit(X,y)

rfrscores = cross_validation.cross_val_score(rfr,X,y,cv=2)
print 'Random Forests',rfrscores
print("Average Accuracy: %0.2f (+/- %0.2f)" % (rfrscores.mean()*100, rfrscores.std() *100))

ext = ensemble.ExtraTreesRegressor()
ext.fit(X,y)

extscores = cross_validation.cross_val_score(ext,X,y,cv=2)
print 'Extra Trees',extscores
print("Average Accuracy: %0.2f (+/- %0.2f)" % (extscores.mean()*100, extscores.std() *100))

#print str.format('{0:.15f}',f)


X_train,X_test,y_train,y_test = cross_validation.train_test_split(X,y,test_size=0.5,random_state=50)

dtr.fit(X_train,y_train)
print dtr.score(X_test,y_test)

rfr.fit(X_train,y_train)
print rfr.score(X_test,y_test)

ext.fit(X_train,y_train)
print ext.score(X_test,y_test)






