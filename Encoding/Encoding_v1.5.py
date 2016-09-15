# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 21:54:13 2016

@author: Rohan Koodli
"""

def encoding_test(sequence):
    encoded = []
    for i in sequence: #turns base pairs into numbers
        if i == 'A':
            encoded.append('1')
        if i == 'T':
            encoded.append('2')
        if i == 'G':
            encoded.append('3')
        if i == 'C':
            encoded.append('4')    

    #print encoded prints fine

    seq = []

    for i in range(len(encoded)):
        if i%3 == 0:
            a = encoded[i:i+3]
            a = ''.join(a)
            a = float(a)
            seq.append(a)
        
    return seq


        


import math
from collections import Counter
def entropy(labels):
    num_labels = len(labels)    
    probability = [count / num_labels for count in Counter(labels).values()]            
    if num_labels <= 1:
        return 0
    return sum(-probability * math.log(probability,2)) #this is the formula
    
def encode_bases(sequence):#Bio.seq.seq type is iterable
    encoded = []
    for i in sequence:
        if i == 'A':
            encoded.append('1')
        if i == 'T':
            encoded.append('2')
        if i == 'G':
            encoded.append('3')
        if i == 'C':
            encoded.append('4')
            
    encoded = encoded[:20] + ['.'] + encoded[20:]
    encoded = ''.join(encoded)
    
    encoded = float(encoded)
    encoded1 = []
    encoded1.append(encoded)
    
    return encoded1
    
def encode_bases_2(sequence):#Bio.seq.seq type is iterable
    encoded = []
    for i in sequence:
        if i == 'A':
            encoded.append('1')
        if i == 'T':
            encoded.append('2')
        if i == 'G':
            encoded.append('3')
        if i == 'C':
            encoded.append('4')
            
    encoded = encoded[:20] + ['.'] + encoded[20:]
    encoded = ''.join(encoded)
    
    encoded = float(encoded)
    #print encoded
    return encoded
    
def decrypt(array):#result is numpy.ndarray
    results = []
    results.append(array[0][0])
    if array[0][1] == 0.0:
        results.append('male')
    elif array[0][1] == 1.0:
        results.append('female')
    else:
        results.append('error')
    results.append(array[0][2])
    if array[0][3] == 0.0:
        results.append('resistant to adamantanes')
    elif array[0][3] == 1.0:
        results.append('sensitive to adamantanes')
    else:
        results.append('error')
    if array[0][4] == 0.0:
        results.append('resistant to oseltamvir')
    elif array[0][4] == 1.0:
        results.append('sensitive to oseltamvir')
    else:
        results.append('error')
    if array[0][5] == 0.0:
        results.append('resistant to zanamvir')
    elif array[0][5] == 1.0:
        results.append('sensitive to zanamvir')
    else:
        results.append('error')
        
    return results
    
def encode_bases_3(sequence):
    encoded = []
    for i in sequence:
        if i == 'A':
            encoded.append('1')
        if i == 'T':
            encoded.append('2')
        if i == 'G':
            encoded.append('3')
        if i == 'C':
            encoded.append('4')
            
    e1 = encoded[0:20]
    print (e1)
    print len(e1)
    print e1[0]
    e1 = ''.join(e1)
    print e1
    e1 = float(e1)


    final = []
    final.append(e1)

    return final
    
    oooo = []
    for i in range(len(encoded)):
        if i%20 == 0:
            a = ''.join(encoded[i],encoded[i+20])
    
    
def encode_bases_4(sequence):
    encoded = []
    for i in sequence:
        if i == 'A':
            encoded.append('1')
        if i == 'T':
            encoded.append('2')
        if i == 'G':
            encoded.append('3')
        if i == 'C':
            encoded.append('4')
            
    oooo = []
    for i in range(len(encoded)):
        #print i
        if i%20 == 0:
            #print i
            #i = int(i)
            a = encoded[i:i+20]
            a = ''.join(a)
            a = float(a)
            oooo.append(a)
        
        o1 = []
        o1.append(oooo)
            
    return o1
    
def encode_bases_5(sequence):
    encoded = []
    for i in sequence:
        if i == 'A':
            encoded.append('1')
        if i == 'T':
            encoded.append('2')
        if i == 'G':
            encoded.append('3')
        if i == 'C':
            encoded.append('4')
            
    oooo = []
    for i in range(len(encoded)):
        #print i
        if i%20 == 0:
            #print i
            #i = int(i)
            a = encoded[i:i+20]
            a = ''.join(a)
            a = float(a)
            oooo.append(a)
        
        o1 = []
        o1.append(oooo)
            
    return oooo
    

def encode_bases_np(sequence):
    import numpy as np
    encoded = []
    for i in sequence:
        if i == 'A':
            encoded.append('1')
        if i == 'T':
            encoded.append('2')
        if i == 'G':
            encoded.append('3')
        if i == 'C':
            encoded.append('4')
            
    oooo = []
    for i in range(len(encoded)):
        #print i
        if i%20 == 0:
            #print i
            #i = int(i)
            a = encoded[i:i+20]
            a = ''.join(a)
            a = float(a)
            oooo.append(a)
        
        o1 = []
        o1.append(oooo)
        o2 = np.array(o1)
            
    return o2
    
def encode_bases_6(sequence):
    encoded = []
    for i in sequence:
        if i == 'A':
            encoded.append('1')
        if i == 'T':
            encoded.append('2')
        if i == 'G':
            encoded.append('3')
        if i == 'C':
            encoded.append('4')
            
    oooo = []
    for i in range(len(encoded)):
        #print i
        if i%20 == 0:
            #print i
            #i = int(i)
            a = encoded[i:i+20]
            a = ''.join(a)
            a = float(a)
            oooo.append(a)
        
        o1 = []
        o1.append(oooo)
            
    return oooo
    

def encoding(sequence):
    encoded = []
    for i in sequence:
        if i == 'A':
            encoded.append('1')
        if i == 'T':
            encoded.append('2')
        if i == 'G':
            encoded.append('3')
        if i == 'C':
            encoded.append('4')    

    #print encoded prints fine

    number = []

    for i in range(len(encoded)):
        if i%15 == 0:
            a = encoded[i:i+15]
            a = ''.join(a)
            a = float(a)
            number.append(a)
        
    return number
    
'''
a = list(SeqIO.parse('/Users/rohankoodli/Desktop/Data-Files/Test-multiple-fasta.fasta','fasta'))

#print a[0]

b = encode_bases_4(a[0].seq)
#print 'aaaaa ',b

ab = []
ab.append(b)

#print ('%.20f' % b[0])
'''

