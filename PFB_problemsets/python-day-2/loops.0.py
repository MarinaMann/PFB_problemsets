#!/usr/bin/env python3

#Problemset python4 - lists and loops

taxa = ['sapiens','erectus','neanderthalensis']
print(taxa)
print(taxa[1])
print(type(taxa))

string_taxa_with =  ','.join(taxa)
print(string_taxa_with)
species = string_taxa_with.split(',')
print(species)



