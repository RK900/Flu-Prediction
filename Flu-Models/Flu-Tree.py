'''
Author: Rohan Koodli
A general Flu Prediction algorithm that can be used with H1N1 & H3N2 HA & NA proteins
'''

from Bio import SeqIO
import os
path = os.getcwd()
print path
seqs = list(SeqIO.parse(path + '\Flu_Data\H1N1\HA\HA-1000.fasta','fasta'))