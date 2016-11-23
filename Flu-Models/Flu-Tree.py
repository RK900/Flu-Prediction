'''
Author: Rohan Koodli
A general Flu Prediction algorithm that can be used with H1N1 & H3N2 HA & NA proteins
'''

from Bio import SeqIO
import os
path = os.getcwd()

seqs = list(SeqIO.parse(path + '\Flu-Data\H1N1\NA\H1N1-NA-1000.fasta','fasta'))

X0 = []

# adding to X and y

for i in range(0, len(seqs) - 1):
    X0.append(seqs[i].seq)

y0 = []
for j in range(1, len(seqs)):
    y0.append(seqs[i].seq)

from Encoding_v2 import encoding

# Encoding letters into numbers

X = []
for k in range(len(X0)):
    encoded_X = encoding(X0[k])
    X.append(encoded_X)

y = []
for l in range(len(y0)):
    encoded_y = encoding(y0[l])
    y.append(encoded_y)

from sklearn import ensemble, cross_validation, metrics

rfr = ensemble.RandomForestRegressor()
rfrscores = cross_validation.cross_val_score(rfr, X, y, cv=2)

print("Random Forests cross-validation score", rfrscores)
print("Average Cross-Val Accuracy: %0.2f (+/- %0.2f)" % (rfrscores.mean()*100, rfrscores.std() *100))

