#!/usr/bin/env python3

#change lowercase to uppercase
bird = 'chicken'
upbird = bird.upper()
print(upbird)



#Sequences in python are delt with as strings, see below!

DNA = 'GATGGGATTggggttttccccTCCCATGTGCTCAAGACTGGCGCTaaaaGttttGAGCTTCTCaaaaGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCggggACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGccccCTCTGAGTCAGGAAACAttttCAGACCTATGGAAACTACTTCCTGaaaaCAACGTTCTGTccccCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTccccGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTccccCCGTGGccccTGCACCAGCAGCTCCTACACCGGCGGccccTGCACCAGccccCTCCTGGccccTGTCATCTTCTGTCCCTTCCCAGaaaaCCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTccccTGCCCTCAACAAGATGttttGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACAccccCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGccccCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGccccTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACttttCG'

#count the number of each letter in the sequence of DNA, regardless of their case (upper and lower)
print(DNA.count('A'), 'is A')
print(DNA.count('T'), 'is T')
print(DNA.count('G'), 'is G')
print(DNA.count('C'), 'is C')
print(DNA.count('a'), 'is a')
print(DNA.count('t'), 'is t')
print(DNA.count('g'), 'is g')
print(DNA.count('c'), 'is c')

bigA = DNA.replace('a','A')
bigC = DNA.replace('c','C')
bigG = DNA.replace('g','G')
bigT = DNA.replace('t','T')

print(bigT.count('T'), "is number of T's and t's")

print(bigG.count('G'), "is number of G's and g's")

print(bigC.count('C'), "is number of C's and  c's")

print(bigA.count('A'), "is number of A's and  a's")


