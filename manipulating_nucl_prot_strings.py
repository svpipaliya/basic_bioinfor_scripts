#!/usr/bin/env python

## Below are simple functions to manipulate and extract information from nucleotide or amino acid sequence string
## Ask Shweta if you are confused

# Remove \n from a DNA fasta sequence using the replace function
gapdh = """tctctctctctaCTTCCTGCAGACAGCTCCTCTCCTACATCACCAAGGACAAGCAGACA
GGAAAAGCTGTGTCAGCGGTTCCGCACATCCCGGTATGCTGCCCTCCCTGAGGGTTCTTTGTGCTGAGCG
GGGCCCTGCAGGGGAGAAAGGCCCATCCCTCACCCCTTCAATGCCCCCACTGTGGCATCCCTGGGACTGG
GGAGGCTGATGGGGAAGGTTGAGCCTTTACTAGCTGGATCTCCCAGTTCCTCACAAAGCCCTTCCTATCT
GCAGAACTGAGCGGCAGCAGCGAGACCTGGCCTACTGTGTGTCACAGCTGCCCCTCACAGAGCGAGGCCT
CCGTAAGATGCTTGACAATTTTGACTGTTTTGGAGACAAACTGTCAGATGAGTCCATCTTCAGTGCTTTT"""
DNA = gapdh.replace('\n', '')
# The len function can be used to find the length of a nucl or prot sequence
print(len(DNA))
# The uppercase function will replace lowercase characters to uppercase in DNA sequence string
U = DNA.upper()
print(U)
# The lowercase function will replace uppercase characters to lowercase in DNA sequence string
l = DNA.lower()
print(l)
# two DNA sequences can be concatenated using + function
tail = "CTCCTCCTCCTCCTCCTCCTCCTCCTCCTCCTCCTCCTCCTCCTCCTCCTCCTCCTCCT"
dna_cat = DNA+tail
print(dna_cat)
# characters in a DNA or a protein string can be replaced using the replace function
my_protein = "vlspadktnv"
my_protein_no_v = my_protein.replace('v','y')
print(my_protein_no_v)
# indices can be used to slice protein data from specified positions
print(my_protein[2:4])
# count() can be used to count sub-strings
print(DNA.count("T"))
# find() can be used to find the index location of an nt or aa in a sequence string
print(my_protein.find('v'))
# split() function can be used to digest the DNA and print out the output (i.e. restriction digestion using an enzyme cut site)
XbaI = 'TCTAGA' # this is the sequence of the enzyme cut site
my_DNA = 'ATGGGTCTAGATTCTGCGGATGA'
md_cut = md_cut.split(XbaI)
print(md_cut.split(XbaI))
#['ATGGG', 'TTCTGCGGATGA'] This is the output
print(md_cut[0]+"|XbaI|"+md_cut[1])
# 'ATGGG|XbaI|TTCTGCGGATGA' This is the output which indicates that there is an XbaI site in here

##End
