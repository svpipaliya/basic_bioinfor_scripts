#!/usr/bin/env python
# This script reads and removes special characters from a fasta file
# open a fasta file for reading
with open("/Users/ShwetaPipaliya/Desktop/naeg_JGI.fa", "r") as reader:
	fasta_file = reader.readlines()
	
#overwrite characters from a fasta line
with open("/Users/ShwetaPipaliya/Desktop/naeg_JGI.fa", "w") as writer"
for i in f:
	if i == ">,|": print("_", end ="")
	else : print(i, end ="")

#end