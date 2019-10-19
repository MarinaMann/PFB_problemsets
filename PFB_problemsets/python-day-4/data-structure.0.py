#!/usr/bin/env python3

"""Must initialize file as a python runnable script by the following command:
		<chmod +x <file-to-run.py>
	Then retry running the script using ./<script_name.py>"""

import sys
import re

file = ''
try:
	file = sys.argv[1]
	print("User provided file:", file)
	multi_fasta = open(file,'r')
	for lines in multi_fasta:
		lines = lines.rstrip()
		print(line)	
except:
	print("Please provide a file name in commandline, $<script_name.py> <file.in>




