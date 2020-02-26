from Bio.Seq import Seq
from Bio import SeqIO

#open files
file = open("contigs_1000.fasta")
log_file = open("project.log", "a")

total_bps = 0

#pull seqs out of file
for contig in SeqIO.parse(file, "fasta"):
  #get length and add to total bps
  length = len(contig.seq)
  total_bps = total_bps + length

#update log file
log_file.write("There are " + str(total_bps) + " bp in the assembly.\n")
log_file.close()
  
