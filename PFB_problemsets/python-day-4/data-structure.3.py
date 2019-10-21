#!/usr/bin/env python3

"""Must initialize file as a python runnable script by the following command:
		chmod +x <file-to-run.py>
	Then retry running the script using ./<script_name.py>"""

import re
keys = []
values = []
fasta_dict = {}

with open('Python_08.fasta','r') as fasta:
	for lines in fasta:
		lines = lines.rstrip('\n')
		#print(lines)
		reads = lines.split('^>.+')
		print(reads)    												#every line becomes a list with one string inside
		#keys.append(
		#print(keys)

	#how to build a dictionary of nucleotide:count pairs
#	nt_count = {}
#	for nt in dna:				#where dna is a string of sequence
#		if nt in nt_count:
#			nt_count[nt]+=1
#		else:
#			nt_count[nt] = 1
#		print(nt_count)



