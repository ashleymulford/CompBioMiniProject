#import biopython classes
from Bio.Seq import Seq
from Bio import SeqIO

#open file
file = open("/spades/contigs.fasta")

log_file = open("miniProject.log", "a")

output_file = open("contigs_1000.fasta", "w")

count = 0

#pull seqs out of file
for contig in SeqIO.parse(file, "fasta"):
  if len(contig.seq) > 1000:
    count = count + 1
    output_file.write(">" + str(contig.id) + "\n")
    output_file.write(str(contig.seq) + "\n")
    
log_file.write("There are " + str(count) + " contigs > 1000 bp in the assembly.\n")
log_file.close()
output_file.close()
  

  
