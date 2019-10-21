#!/usr/bin/env python3

"""Must initialize file as a python runnable script by the following command:
		chmod +x <file-to-run.py>
	Then retry running the script using ./<script_name.py>"""

import sys
import re


file = ''
try:
	file = sys.argv[1]
	print("User provided file:", file)
	fasta = open(file,'r')
	for lines in fasta:
		lines = lines.rstrip('\n')
		for heads in re.search(r'^>.+', lines): #retrieves whole header line
			print(heads)
		for seqs in re.search(r'^\w\S+', lines): #retrieves the sequences lines, since the lines must start with a word character, do not include spaces, and match one or more times. 
			print(seqs)
	
#print(bigDNA.count('T'), "is number of T's and t's")


except:
	print("Please provide a file name in commandline, $<script_name.py> <file.in>")




