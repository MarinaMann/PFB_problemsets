#!/usr/bin/env python3

#using file named Python_06.txt


#remember to look at this file using 'cat' in the command line, it's got losts of '\n' whitespaces separating the lines of the poems

with open('Python_06.txt','r') as poem:
	for line in poem:
		line = line.rstrip('\n') #remove \n from text, making it all a single long string
		new_poem = line.upper() #make all letters in file upper case
		print(new_poem) #print the poem as all uppercase, without whitespaces at the ends of each line. Should appear as a paragraph of text.
	




