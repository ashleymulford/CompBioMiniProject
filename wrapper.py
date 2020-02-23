import os
from Bio import Entrez
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

#function to convert sra files to fastq paired-end reads
def 01_fastq_dump(SRR_list):
  for srr in SRR_list:
    dump = "fastq-dump -I --split-files " + srr + ".1"
    os.system(dump)

#function to make fasta file from CDS of NCBI Accession EF999921
def 02a_EF99921_fasta():
  make_fasta = "python3 02_generate_input_HCMV.py" #see script for details on generation of fasta file
  #this call runs command line:
  os.system(make_fasta)

#function to make index with kallisto
def 02b_kallisto():
  run_index = "kallisto index -i hcmv_index.idx HCMV_reads.fasta"
  os.system(run_index)

#function to quantify 
def 03a_kallisto(SRR_list):
  for srr in SRR_list:
    quantify = "kallisto quant -i hcmv_index.idx -o quant_results_" + srr + " -b 30 -t 4 " + srr + ".1_1.fastq " + srr + ".1_2.fastq
    os.system(quantify)
  
  
def 03b_sleuth():
  run_sleuth = "Rscript 03_diff_gene_expression.R"
  os.system(run_sleuth)
  
  
def 04_bowtie2(SRR_list):
  run_bowtie2_build = "bowtie2-build EF999921_reads.fasta HCMV""
  os.system(run_bowtie2_build)
  log_file = open("/home/amulford/mini_project/miniProject.log", "w") #write to file
  for srr in SRR_list:
    run_bowtie2 = "bowtie2 --no-unal --quiet -x HCMV -1 SRR_seq_data/"+ srr +".1_1.fastq -2 SRR_seq_data/" + srr + ".1_2.fastq -S " + srr + "map.sam"
    os.system(run_bowtie2)

    
def 05_spades(SRR_list):
  for srr in SRR_list:
    convert_to_fastq = "samtools fastq /home/amulford/mini_project/" + srr + "map.sam > /home/amulford/mini_project/" + srr + "map.fastq"
    os.system(convert_to_fastq)
  run_spades = "spades -k 55,77,99,127 -t 2 --only-assembler -s " + SRR_list[0] + "map.fastq -s " + SRR_list[1] + "map.fastq -s " + SRR_list[2] + "map.fastq -s " + SRR_list[3] + "map.fastq -o /home/amulford/mini_project/"
  os.system(run_spades)
  log_file = open("/home/amulford/mini_project/miniProject.log", "w") #write to file
  log_file.write("spades -k 55,77,99,127 -t 2 --only-assembler -s SRR5660030map.fastq -s SRR5660033map.fastq -s SRR5660044map.fastq -s SRR5660045map.fastq -o /home/amulford/mini_project/\n")
  log_file.close()
  
  
def 06_subset_contigs():
  subset = "python3 06_count_contigs.py"
  os.system(subset)
  
  
def 07_assembly_length():
  calc_length = "python3 07_assembly_length.py"
  os.system(calc_length)
  
  
def 08_concatenate_contigs():
   concat = "python3 08_concat_contigs.py"
   os.system(concat)
  
  
def 09_blast():
  blast = "python3 09_blast.py"
  os.system(blast)



SRR_list = ["SRR5660030", "SRR5660033", "SRR5660044", "SRR5660045"]










