#!/usr/bin/env python3

"""Must initialize file as a python runnable script by the following command:
		chmod +x <file-to-run.py>
	Then retry running the script using ./<script_name.py>"""

import sys
import re


file = ' '
try:
	file = sys.argv[1]
	print("User provided file:", file)
	fasta_dict = {}
	with open(file,'r') as fasta:
		for lines in fasta:
			lines = lines.rstrip('\n')
			[headers, seqs] = lines.split('^\w\S.+')
			if headers not in fasta_dict:
				fasta_dict[headers] = seqs
				print(fasta_dict)
except:
	print("Please provide a file name in command line, $<script_name.py> <file.in>")




