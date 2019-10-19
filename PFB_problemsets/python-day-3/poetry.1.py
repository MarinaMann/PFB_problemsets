#!/usr/bin/env python3

#find every occurence of 'Nobody' in file Python_07_nobody.txt and print out their positions.
import re

with open('Python_07_nobody.txt','r') as poetry, open('New_person_poem.txt','w') as somebody:
	for lines in poetry:
		lines = lines.rstrip('\n')
		#print(lines)
		for new_name in re.sub(r'Nobody','Everybody',lines):
			print(new_name)
#		for words in re.findall(r'Nobody', lines):
#			#print(words)
#			print(re.finditer(r'Nobody', lines))
				#allable_iterator object at 0x109c86cf8 is the output for "location". 
			somebody.write(str(new_name))
print('wrote newly named person to poetry file')


