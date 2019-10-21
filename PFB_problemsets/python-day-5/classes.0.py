#!/usr/bin/env python3

#I want a DNA seq class "DNARecord" with attributes to return the sequence, the name, and the organism. 
#I'll be using the __init__ function
#the __init__ function allows the user to provide any sequence as input

class DNARecord(object):
	#define class attributes using __init__
	def __init__(self, sequence, gene_name, species_name):
		self.sequence = sequence
		self.gene_name = gene_name
		self.species_name = species_name
	
#Now that I've intialized my class, I'm going to start my python script
#I've defined my class object as DNARecord(). I can give this class a reference name, like 'class_variable_name'
#Since I've used __init__, I can simply fill in the () with the three elements my class needs: sequence, gene_name and species_name
#since I haven't DONE anything to these variable, my class will simply spit them back out. If the class prints all 3 elements I give it, It's working.
sequence = 'actgtcagtgatcgactatagc'
gene_name = 'gene1'
species_name = 'cool bug'

class_variable_name = DNARecord('actgtcagtgatcgactatagc','gene1','cool bug')
class_variable_name2 = DNARecord('actgatgacatgacacgggtat','gene2','another cool bug')

for d in [class_variable_name,class_variable_name2]:
	print('name:', d.gene_name,'species:',d.species_name,'seq:',d.sequence)
	


