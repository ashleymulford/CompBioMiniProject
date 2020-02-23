#import biopython classes
from Bio.Seq import Seq
from Bio import SeqIO

file = open("/home/amulford/mini_project/contigs_1000.fasta")
log_file = open("/home/amulford/mini_project/miniProject.log", "a")

total_bps = 0

#pull seqs out of file
for contig in SeqIO.parse(file, "fasta"):
  length = len(contig.seq)
  total_bps = total_bps + length
    
log_file.write("There are " + str(total_bps) + " bp in the assembly.\n")
log_file.close()
  
