# this forloop performs a batch filename extension change from 'fasta' to 'fa'
for file in *.fasta; do mv "$file" "${file%.fasta}.fa"; done