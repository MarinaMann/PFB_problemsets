#!/usr/bin/env python3

import re

#find the headers in Python_07.fasta using pattern matching
with open('Python_07.fasta','r') as fasta:
	for lines in fasta:
		lines = lines.rstrip('\n')
		headers = re.search(r'^>\S+\s.+', lines)
		print(headers)

