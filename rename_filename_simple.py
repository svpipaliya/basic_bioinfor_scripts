#!/usr/local/bin/python

import os
old_file = os.path.join("/Users/ShwetaPipaliya/Giardia_genomes/refseq/protozoa/GCF_000002435.1/", "*.gbff")
new_file = os.path.join("/Users/ShwetaPipaliya/Giardia_genomes/refseq/protozoa/GCF_000002435.1/", "*_1.gbff")
os.rename(old_file, new_file)

#end