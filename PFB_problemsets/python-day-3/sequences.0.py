#!/usr/bin/env python3

#This is a sequences file has headers and sequences separated by tabs, basically, two columns of data! So I can make a dictionary
#make an empty disctionary, which I'll populate with a for loop
genes = {}

#open file Python_06.seq.txt
with open('Python_06.seq.txt','r') as seq:
	for line in seq: #for every line in the file I"ve read in as seq,
		line = line.rstrip('\n') #remove white spaces at the ends of each line, should create a long string
		#print(line) #looks te same when it prints out....
		gene_id,seq = line.split() #split the lines by their tab, so the left is the gene_it (key) and the right is the sequence (value)
		genes[gene_id] = seq #populate the empty dictionary, prioritizing by gene_id, and pairing the seq to the gene_id
#print(genes) #look at the disctionary to make sure it looks right
		reverse_genes = dict.fromkeys(gene_id,seq) #create new dictionary with keys from first dictionary, values populated by 'value' for now
		#print(reverse-genes)
		#create for loop: for each key, calculate the reverse complement of the associated value
		for gene in genes:
			#print(gene) #prints each key in the dictionary 'genes'
			reverse_genes[gene]=seq[::-1] #populate the second dictionary with reverse complement of values from first

print('added reverse complement values to new dictionary, same keys')

