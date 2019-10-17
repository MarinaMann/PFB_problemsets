#!/usr/bin/env python3

#change lowercase to uppercase
bird = 'chicken'
upbird = bird.upper()
print(upbird)



#Sequences in python are delt with as strings, see below!

DNA = 'GATGGGATTggggttttccccTCCCATGTGCTCAAGACTGGCGCTaaaaGttttGAGCTTCTCaaaaGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCggggACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGccccCTCTGAGTCAGGAAACAttttCAGACCTATGGAAACTACTTCCTGaaaaCAACGTTCTGTccccCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTccccGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTccccCCGTGGccccTGCACCAGCAGCTCCTACACCGGCGGccccTGCACCAGccccCTCCTGGccccTGTCATCTTCTGTCCCTTCCCAGaaaaCCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTccccTGCCCTCAACAAGATGttttGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACAccccCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGccccCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGccccTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACttttCG'

#count the number of each letter in the sequence of DNA, regardless of their case (upper and lower)
#individually count big and little, then add together manually the integer outputs
A = DNA.count('A')
print(A, 'is A')
print(DNA.count('T'), 'is T')
print(DNA.count('G'), 'is G')
print(DNA.count('C'), 'is C')
a = DNA.count('a')
print(a, 'is a')
print(DNA.count('t'), 'is t')
print(DNA.count('g'), 'is g')
print(DNA.count('c'), 'is c')

#since A and a are now integer outputs, I can add them
print(A+a, "is total A's regardless of case")

#can alternatively replace a with A
bigA = DNA.replace('a','A')
bigC = DNA.replace('c','C')
bigG = DNA.replace('g','G')
bigT = DNA.replace('t','T')

#after replacing, can count total big A
print(bigT.count('T'), "is number of T's and t's")
print(bigG.count('G'), "is number of G's and g's")
print(bigC.count('C'), "is number of C's and  c's")
print(bigA.count('A'), "is number of A's and  a's")

#Third option, is using DNA.upper to convert all to upper (regardless of letter types), then count total bigs as above
bigDNA = DNA.upper()
print(bigDNA)
print(bigDNA.count('T'), "is number of T's and t's")
print(bigDNA.count('G'), "is number of G's and g's")
print(bigDNA.count('C'), "is number of C's and  c's")
print(bigDNA.count('A'), "is number of A's and  a's")

