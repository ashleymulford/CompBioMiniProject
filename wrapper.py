import os
import argparse
from Bio import Entrez
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

#function to convert sra files to fastq paired-end reads
def fastq_dump(SRR_list):
  for srr in SRR_list:
    dump = "fastq-dump -I --split-files " + srr + ".1"
    os.system(dump)

#function to make fasta file from CDS of NCBI Accession EF999921
def EF999921_fasta():
  make_fasta = "python3 02a_generate_HCMV_input.py" #see script for details on generation of fasta file
  #this call runs command line:
  os.system(make_fasta)

#function to make index with kallisto
def kallisto_index():
  run_index = "kallisto index -i hcmv_index.idx HCMV_reads.fasta"
  os.system(run_index)

#function to quantify paired-end reads with kallisto
def kallisto_quant(SRR_list):
  for srr in SRR_list:
    quantify = "kallisto quant -i hcmv_index.idx -o quant_results_" + srr + " -b 30 -t 4 subset_" + srr + ".1_1.fastq subset_" + srr + ".1_2.fastq
    os.system(quantify)
  
#function to run sleuth
def sleuth():
  run_sleuth = "Rscript 03b_diff_gene_expression.R" #see script for details on running sleuth
  os.system(run_sleuth)
  
#function to run bowtie2  
def bowtie2(SRR_list):
  #build bowtie2 index from EF999921 fasta file
  run_bowtie2_build = "bowtie2-build EF999921_reads.fasta HCMV""
  os.system(run_bowtie2_build)
  for srr in SRR_list:
    run_bowtie2 = "bowtie2 --no-unal --al-conc" + srr + "--quiet -x HCMV -1 SRR_seq_data/"+ srr +".1_1.fastq -2 SRR_seq_data/" + srr + ".1_2.fastq -S " + srr + "map.sam"
    os.system(run_bowtie2)

#function to convert sam files to fastq files for SPAdes input, also counts reads before and after filtering with bowtie2
def count_reads(SRR_list):
  log_file = open("miniProject.log", "w")
  for srr in SRR_list:
    rename1 = "mv " + srr + ".1 " + srr + ".1.fastq"
    os.system(rename1) #rename bowtie2 output files to end in fastq
    rename2 = "mv " + srr + ".2 " + srr + ".2.fastq"
    os.system(rename2) #rename bowtie2 output files to end in fastq
    fastq_before = open(srr + ".1_1.fastq")
    fastq_after = open(srr + ".1.fastq")
    count_before = 0
    count_after = 0
    for line in fastq_before:
      count_before = count_before+1
    for line in fastq_after:
      count_after = count_after+1
    count_before = count_before/2
    count_after = count_after/4
    if srr == SRR_list[0]:
      log_file.write("Donor 1 (2dpi) had " + str(count_before) + " read pairs before Bowtie2 filtering and " + str(count_after) + " read pairs after.")
    elif srr == SRR_list[1]:
      log_file.write("Donor 1 (6dpi) had " + str(count_before) + " read pairs before Bowtie2 filtering and " + str(count_after) + " read pairs after.")
    elif srr == SRR_list[2]:
      log_file.write("Donor 3 (2dpi) had " + str(count_before) + " read pairs before Bowtie2 filtering and " + str(count_after) + " read pairs after.")
    elif srr == SRR_list[3]:
      log_file.write("Donor 3 (6dpi) had " + str(count_before) + " read pairs before Bowtie2 filtering and " + str(count_after) + " read pairs after.")    
  log_file.close()
  
#function to run SPAdes  
def spades(SRR_list):
  run_spades = "spades -k 55,77,99,127 -t 2 --only-assembler --pe1-1 " + SRR_list[0] + ".1.fastq --pe1-2 " + SRR_list[0] + ".2.fastq --pe2-1 " + SRR_list[1] + ".1.fastq --pe2-2 " + SRR_list[1] + ".2.fastq --pe3-1 " + SRR_list[2] + ".1.fastq --pe3-2 " + SRR_list[2] + ".2.fastq --pe4-1 " + SRR_list[3] + ".1.fastq --pe4-2 " + SRR_list[3] + ".2.fastq -o /spades" 
  os.system(run_spades)
  log_file = open("miniProject.log", "w")
  log_file.write(run_spades) #write to file
  log_file.close()
  
#function to conunt and subset contigs longer than 1000 bp  
def subset_contigs():
  subset = "python3 06_count_contigs.py" #see script for details
  os.system(subset)
  
#function to calculate assembly length  
def assembly_length():
  calc_length = "python3 07_assembly_length.py" #see script for details
  os.system(calc_length)
  
#function to assemble contigs together, separated by 50 Ns  
def concatenate_contigs():
   concat = "python3 08_concat_contigs.py" #see script for details
   os.system(concat)
  
#function to run blast  
def blast():
  blast = "python3 09_blast.py" #see script for details
  os.system(blast)


  ###############################################################

  
parser = argparse.ArgumentParser()
parser.add_argument("--SRRlist", nargs='+', help = "a list of the SRRs you want to assemble and blast")
p = parser.parse_args()

SRR_list = []

for srr in p.SRRlist:
  SRR_list.append(ssr)


EF99921_fasta()
kallisto_index()
kallisto_quant(SRR_list)
sleuth()
bowtie2(SRR_list)
count_reads(SRR_list)
os.system(mkdir spades)
spades(SRR_list)
subset_contigs()
assembly_length()
concatenate_contigs()
blast()



