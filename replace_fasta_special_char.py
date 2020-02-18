#!/usr/bin/env python
# This script reads and removes a single specified special character from a fasta file
import re
original_fasta = open('path/to/fasta.fa').read()
new_fasta = re.sub('[|]', '_', original_fasta)
open('output.fa', 'w').write(new_fasta)

#end