# Flu-Prediction
[![GitHub release](https://img.shields.io/badge/release-v2.1-brightgreen.svg)](https://github.com/RK900/Flu-Prediction/releases)
[![Python27](https://img.shields.io/badge/python-2.7-blue.svg)](https://www.python.org/download/releases/2.7/)
[![License](https://img.shields.io/cocoapods/l/EasyQL.svg?style=flat)](https://github.com/RK900/Flu-Prediction/blob/master/LICENSE.txt)
[![Twitter](https://img.shields.io/badge/twitter-@RohanKoodli-blue.svg?style=flat)](http://twitter.com/RohanKoodli)

Predicting Future Flu Virus Strains with Machine Learning. 
These programs predict future influenza virus strains based on previous trends in flu mutations.

### Talks
Check out my talks at <a href="https://www.youtube.com/watch?v=j325KOyV-hI">PyData</a> and PyGotham.

### License
Flu-Prediction is available under the [MIT License](https://github.com/RK900/Flu-Prediction/blob/master/LICENSE.txt).

### Dependencies
Python 2.7 or greater with Numpy, Biopython, and Scikit-learn libraries installed.

## To use:
Input any HA (hemagglutinin) or NA (neuraminidase) flu protein sequence and it's corresponding child sequence into the program and it will output a predicted offspring of that specific flu strain.

### Reading in a FASTA file with Biopython
Use the Biopython library to import a sequence (a FASTA file format). You can use any flu FASTA file of your choosing, or you can use the ones in the Flu-Data folder. The data in the Flu-Data folder contain a wide variety of flu FASTA files, from single flu strains up to 1000 flu strains, which are grouped by flu subtype and protein.

```python
from Bio import SeqIO
sequence = SeqIO.parse('myfasta.fasta','fasta') # put your FASTA file here
parent_fasta = parent.fasta 
parent_seq = parent.seq

child_fasta = parent.fasta 
child_seq = child.seq
```

### Encoding
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

### Fitting the model
Substitute "algorithm" for any scikit-learn model of your choosing.
```python
from sklearn.algorithms import algorithm()
alg = algorithm()
alg.fit(X,y)
alg.predict(new_X)
```
The algorithm I use in this project is a Random Forests Regressor model:
```python
from sklearn.ensemble import RandomForestRegressor()
rfr = RandomForestRegressor() # Specify and parameters in the parenthesis
rfr.fit(X,y)
rfr.predict(new_X)
```

### Computing accuracy using K-Fold cross-validation:
```python
from sklearn import cross_validation
algorithm_scores = cross_validation.cross_val_score(algorithm,X,y,cv=2)
print 'Algorithm Trees',algorithm_scores
print("Average Accuracy: %0.2f (+/- %0.2f)" % (algorithm_scores.mean()*100, algorithm_scores.std() *100))
```

### Computing accuracy using R<sup>2</sup> (for linear models):
```python
from sklearn import metrics
y_pred = algorithm.predict(X_test)
print 'Algorithm R2 score:', metrics.r2_score(y_test,y_pred,multioutput='variance_weighted')
```

### Computing accuracy using Mean Squared Error (MSE):
```python
from sklearn import metrics
y_pred = algorithm.predict(X_test)
print 'Algorithm mean squared error:', metrics.mean_squared_error(y_test,y_pred,multioutput='variance_weighted')
```
### Predicting Flu Strains:
```python
y_pred = algorithm.predict(X)
print y_pred
```
The prediction output is a list of floats. Each number in the float corresponds to a base pair:
A to 1, T to 2, G to 3, and C to 4.
