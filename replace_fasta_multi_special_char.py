#!/usr/bin/env python

# This script reads and removes special characters from a fasta file
import re
original_fasta = open('/Users/ShwetaPipaliya/Desktop/naeg_JGI.fa').read()
new_fasta = re.sub('[|]', '_', original_fasta)
open('n1.fa', 'w').write(new_fasta)

#end