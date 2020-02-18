#!/usr/bin/env python

# this script will write FASTA to into a separate file

DNA = ">AccessionCodeHere Genus Species MoreInfo \ATGC"
saveFASTA = open(r'NameOfFile.fa', 'w+')
saveFASTA.write(DNA)
saveFASTA.close()

# End