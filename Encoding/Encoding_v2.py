# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 18:49:40 2016

@author: Rohan Koodli
"""

'''
Encoding DNA bases (adenine, thymine, guanine, cytosine)
changing ints to floats for algorithm
changes Bio.seq to str to list of floats to give to algorithm
'''


def encoding(sequence):
    encoded = []
    for i in sequence: # turns base pairs into numbers
        if i == 'A':
            encoded.append('1')
        if i == 'T':
            encoded.append('2')
        if i == 'G':
            encoded.append('3')
        if i == 'C':
            encoded.append('4')    

    # print encoded prints fine

    seq = []

    for i in range(len(encoded)): # joins chunks of 15 digits together
        if i%15 == 0:
            a = encoded[i:i+15]
            a = ''.join(a)
            a = float(a)
            seq.append(a)
        
    return(seq)
    
def compare_strains(seq1,seq2): # Compare 2 sequences for total number of mutations
    counter = 0
    nums = []
    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
            pass
        else:
            counter += 1
            nums.append(i+1)
    
    return(counter,nums)
    
# Entropy function
import math
from collections import Counter
def entropy(labels):
    num_labels = len(labels)    
    probability = [count / num_labels for count in Counter(labels).values()]            
    if num_labels <= 1:
        return(0)
    return(sum(-probability * math.log(probability,2))) # this is the formula
    
