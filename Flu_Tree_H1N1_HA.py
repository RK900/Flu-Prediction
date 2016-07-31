# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 21:49:22 2016

@author: Rohan Koodli
"""

from Bio import SeqIO
'''
new = list(SeqIO.parse('/Users/Rohan Koodli/Desktop/Data-Files/Flu-Strains/Test-15-fastas.fasta','fasta'))
records = list(SeqIO.parse('/Users/Rohan Koodli/Desktop/Data-Files/Flu-Strains/Test-50-fastas.fasta','fasta'))
new7 = list(SeqIO.parse('/Users/Rohan Koodli/Desktop/Data-Files/Flu-Strains/Test-50-fastas-3.fasta','fasta'))
new4 = list(SeqIO.parse('/Users/Rohan Koodli/Desktop/Data-Files/Flu-Strains/Test-20-fastas.fasta','fasta'))
new = list(SeqIO.parse('/Users/Rohan Koodli/Desktop/Data-Files/Flu-Strains/Test-100-fastas-2.fasta','fasta')) #100 HA fastas
new6 = list(SeqIO.parse('/Users/Rohan Koodli/Desktop/Data-Files/Flu-Strains/Test-50-NA-fastas.fasta','fasta'))#50 NA fastas
new = list(SeqIO.parse('/Users/Rohan Koodli/Desktop/Data-Files/Flu-Strains/Test-100-NA-fastas.fasta','fasta'))
new = list(SeqIO.parse('/Users/Rohan Koodli/Desktop/Data-Files/Flu-Strains/Test-200-NA-fastas.fasta','fasta'))
new5 = list(SeqIO.parse('/Users/Rohan Koodli/Desktop/Data-Files/Flu-Strains/Test-300-fastas.fasta','fasta'))
new = list(SeqIO.parse('/Users/Rohan Koodli/Desktop/Data-Files/Flu-Strains/Working Strains/HA-50.fasta','fasta'))
'''
#new = list(SeqIO.parse('/Users/Rohan Koodli/Desktop/Data-Files/Flu-Strains/Working Strains/HA-100.fasta','fasta'))
#new = list(SeqIO.parse('/Users/Rohan Koodli/Desktop/Data-Files/Flu-Strains/Working Strains/HA-50.fasta','fasta'))
#new = list(SeqIO.parse('/Users/Rohan Koodli/Desktop/Data-Files/Flu-Strains/Working Strains/HA-150.fasta','fasta'))

'''
new = list(SeqIO.parse('/Users/Rohan Koodli/Desktop/Data-Files/Flu-Strains/Working Strains/HA-200.fasta','fasta'))

new = list(SeqIO.parse('/Users/Rohan Koodli/Desktop/Data-Files/Flu-Strains/Working Strains/HA-250.fasta','fasta'))

new = list(SeqIO.parse('/Users/Rohan Koodli/Desktop/Data-Files/Flu-Strains/Working Strains/HA-300.fasta','fasta'))

new = list(SeqIO.parse('/Users/Rohan Koodli/Desktop/Data-Files/Flu-Strains/Working Strains/HA-350.fasta','fasta'))

new = list(SeqIO.parse('/Users/Rohan Koodli/Desktop/Data-Files/Flu-Strains/Working Strains/HA-400.fasta','fasta'))

new = list(SeqIO.parse('/Users/Rohan Koodli/Desktop/Data-Files/Flu-Strains/Working Strains/HA-450.fasta','fasta'))
new = list(SeqIO.parse('/Users/Rohan Koodli/Desktop/Data-Files/Flu-Strains/Working Strains/HA-500.fasta','fasta'))
new = list(SeqIO.parse('/Users/Rohan Koodli/Desktop/Data-Files/Flu-Strains/Working Strains/HA-600.fasta','fasta'))
new = list(SeqIO.parse('/Users/Rohan Koodli/Desktop/Data-Files/Flu-Strains/Working Strains/HA-750.fasta','fasta'))
'''
'''
new = list(SeqIO.parse('/Users/Rohan Koodli/Desktop/Data-Files/Flu-Strains/H1N1-HA-100.fasta','fasta'))
new = list(SeqIO.parse('/Users/Rohan Koodli/Desktop/Data-Files/Flu-Strains/H1N1-HA-200.fasta','fasta'))
new = list(SeqIO.parse('/Users/Rohan Koodli/Desktop/Data-Files/Flu-Strains/H1N1-HA-300.fasta','fasta'))
new = list(SeqIO.parse('/Users/Rohan Koodli/Desktop/Data-Files/Flu-Strains/H1N1-HA-400.fasta','fasta'))
new = list(SeqIO.parse('/Users/Rohan Koodli/Desktop/Data-Files/Flu-Strains/H1N1-HA-500.fasta','fasta'))
new = list(SeqIO.parse('/Users/Rohan Koodli/Desktop/Data-Files/Flu-Strains/H1N1-HA-600.fasta','fasta'))
new = list(SeqIO.parse('/Users/Rohan Koodli/Desktop/Data-Files/Flu-Strains/H1N1-HA-700.fasta','fasta'))
new = list(SeqIO.parse('/Users/Rohan Koodli/Desktop/Data-Files/Flu-Strains/H1N1-HA-700-2.fasta','fasta'))
new = list(SeqIO.parse('/Users/Rohan Koodli/Desktop/Data-Files/Flu-Strains/H1N1-HA-800.fasta','fasta'))
new = list(SeqIO.parse('/Users/Rohan Koodli/Desktop/Data-Files/Flu-Strains/H1N1-HA-900.fasta','fasta'))
'''
#Use this one
new = list(SeqIO.parse('/Users/Rohan/Desktop/Data-Files/Flu-Strains/H1N1-HA-1000.fasta','fasta'))

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
'''
print len(X[0])
print len(y[298])

a = [1,2,3,4,5]
print len(a)

from Compare_Strains import test_length

print len(X[0])
print len(y[0])
print len(X[0]) == len(y[0])
#print test_length(X,y)
'''

from sklearn import tree
from sklearn import metrics

dtr = tree.DecisionTreeRegressor()
dtr.fit(X,y)

from sklearn import cross_validation
dtrscores = cross_validation.cross_val_score(dtr,X,y,cv=2)
print 'Decision Trees',dtrscores
print("Average Accuracy: %0.2f (+/- %0.2f)" % (dtrscores.mean()*100, dtrscores.std() *100))

from sklearn import ensemble
rfr = ensemble.RandomForestRegressor(n_estimators=20)
rfr.fit(X,y)

rfrscores = cross_validation.cross_val_score(rfr,X,y,cv=2)
print 'Random Forests',rfrscores
print("Average Accuracy: %0.2f (+/- %0.2f)" % (rfrscores.mean()*100, rfrscores.std() *100))

ext = ensemble.ExtraTreesRegressor(n_estimators=3)
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

# trying different methods of accuracy
y_pred_rfr = rfr.predict(X_test)
print 'Random Forests R2 score:', metrics.r2_score(y_test,y_pred_rfr,multioutput='variance_weighted')

'''
from sklearn import neighbors
knr = neighbors.KNeighborsRegressor()
knr.fit(X,y)

knrscores = cross_validation.cross_val_score(knr,X,y,cv=10)
print knrscores
'''
'''
X_train,X_test,y_train,y_test = cross_validation.train_test_split(X,y)#,test_size=0.5,random_state=10)

dtr2 = tree.DecisionTreeRegressor()
dtr2.fit(X_train,y_train)
print dtr2.score(X_test,y_test)
'''


    
'''    
print X[0][0]
print y[0][0]

from Compare_Strains import compare_strains
print compare_strains(X[0],y[0])
'''




