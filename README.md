# Flu-Prediction
Predicting Future Flu Virus Strains with Machine Learning 
These programs predict future influenza virus strains. The prediction output is a list of floats. Each number in the float corresponds to a base pair:
A to 1, T to 2, G to 3, and C to 4.

#To use:
Input any HA (hemagglutinin) or NA (neuraminidase) flu protein sequence and it's corresponding child sequence into the program and it will output a predicted offspring of that specific flu strain.
Use the Biopython library to import a sequence ( a FASTA file format). For example:
```python
sequence = Test_Seq.fasta 
sequence = sequence.seq
```
Then encode it with the Encoding_v2 module:
```python
from Encoding_v2 import encoding
X = []
for k in range(len(X0)):
    encoded_X = encoding(X0[k])
    X.append(encoded_X)
    
y = []
for l in range(len(y0)):
    encoded_y = encoding(y0[l])
    y.append(encoded_y)
```
This turns the sequence into a list of float64.
Then, give the X and y to the machine learning algorithm.
Enter any machine learning algorithm in the 'algorithm' parts of the code.
```python
algorithmscores = cross_validation.cross_val_score(algorithm,X,y,cv=2)
print 'Algorithm Trees',algorithmscores
print("Average Accuracy: %0.2f (+/- %0.2f)" % (algorithmscores.mean()*100, algorithmscores.std() *100))
```
