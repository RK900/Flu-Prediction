# Flu-Prediction
Predicting Future Flu Virus Strains with Machine Learning 
These programs predict future influenza virus strains. The prediction output is a list of floats. Each number in the float corresponds to a base pair:
A to 1, T to 2, G to 3, and C to 4.
###Updates
Looking to add gradient boosting (XGBoost or scikit-learn).
###License
MIT

###Dependencies
Requires numpy, Biopython, and scikit-learn installed. Python 2 required.

##To use:
Input any HA (hemagglutinin) or NA (neuraminidase) flu protein sequence and it's corresponding child sequence into the program and it will output a predicted offspring of that specific flu strain.
###Reading in a FASTA with Biopython
Use the Biopython library to import a sequence ( a FASTA file format). For example:
```python
from Bio import SeqIO
sequence = SeqIO.parse('myfasta.fasta','fasta')
parent_fasta = parent.fasta 
parent_seq = parent.seq

child_fasta = parent.fasta 
child_seq = child.seq
```

###Encoding
Then encode it with the Encoding_v2 module:
```python
from Encoding_v2 import encoding
parent = []
for k in range(len(X0)):
    encoded_parent = encoding(parent_seq[k])
    parent.append(encoded_parent)
    
child = []
for l in range(len(y0)):
    encoded_child = encoding(child_seq[l])
    child.append(encoded_child)
```
This turns the sequence into a list of float64's.
Then, give the X and y to the machine learning algorithm.
Enter any machine learning algorithm (eg, RandomForestsRegressor, DecisionTreeRegressor, etc.) in the 'algorithm' parts of the code.

###Fitting the model
Substitute "algorithm" for any model of your choosing.
```python
algorithm.fit(X,y)
algorithm.predict(new_X)
```

###Computing accuracy using K-Fold cross-validation
```python
algorithm_scores = cross_validation.cross_val_score(algorithm,X,y,cv=2)
print 'Algorithm Trees',algorithm_scores
print("Average Accuracy: %0.2f (+/- %0.2f)" % (algorithm_scores.mean()*100, algorithm_scores.std() *100))
```

###Computing accuracy using Coefficient of determination (R^2 score):
```python
y_pred = algorithm.predict(X_test)
print 'Algorithm R2 score:', metrics.r2_score(y_test,y_pred,multioutput='variance_weighted')
```
