#import biopython classes
from Bio.Seq import Seq
from Bio import SeqIO

file = open("contigs_1000.fasta")
output_file = open("blast_input.fasta", "w")
  
assembly = ""

n=""

for i in range(50):
  n = n+"N"
  
#pull seqs out of file
for contig in SeqIO.parse(file, "fasta"):
  assembly = assembly + str(contig.seq) + n
    
output_file.write(">assembly\n")
output_file.write(assembly)
output_file.close()
