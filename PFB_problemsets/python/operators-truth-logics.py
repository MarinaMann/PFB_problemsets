#!/usr/bin/env python3

import sys

DNAsequence = 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA' #name the sequence 
DNAsequence = sys.argv[1] #allow for searching the full sequence from unix using any serise of letters

if sys.argv[1] in DNAsequence:
	print('found sequence in DNA sequence') #if your sequence of interest is found, print this message
else:
	print('did not find sequence in your DNA sequence') #if your sequence is not found, then print this message



