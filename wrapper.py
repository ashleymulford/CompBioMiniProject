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
  make_fasta = "python3 02a_generate_input_HCMV.py" #see script for details on generation of fasta file
  #this call runs command line:
  os.system(make_fasta)

#function to make index with kallisto
def 02b_kallisto():
  run_index = "kallisto index -i hcmv_index.idx HCMV_reads.fasta"
  os.system(run_index)

#function to quantify paired-end reads with kallisto
def 03a_kallisto(SRR_list):
  for srr in SRR_list:
    quantify = "kallisto quant -i hcmv_index.idx -o quant_results_" + srr + " -b 30 -t 4 " + srr + ".1_1.fastq " + srr + ".1_2.fastq
    os.system(quantify)
  
#function to run sleuth
def 03b_sleuth():
  run_sleuth = "Rscript 03b_diff_gene_expression.R" #see script for details on running sleuth
  os.system(run_sleuth)
  
#function to run bowtie2  
def 04a_bowtie2(SRR_list):
  #build bowtie2 index from EF999921 fasta file
  run_bowtie2_build = "bowtie2-build EF999921_reads.fasta HCMV""
  os.system(run_bowtie2_build)
  for srr in SRR_list:
    run_bowtie2 = "bowtie2 --no-unal --quiet -x HCMV -1 SRR_seq_data/"+ srr +".1_1.fastq -2 SRR_seq_data/" + srr + ".1_2.fastq -S " + srr + "map.sam"
    os.system(run_bowtie2)

#function to convert sam files to fastq files for SPAdes input, also counts reads before and after filtering with bowtie2
def 04b_and_05a_convert_to_fastq_and_count(SRR_list):
  log_file = open("miniProject.log", "w") #write to file
  #convert sam files to fastq files using samtools
  for srr in SRR_list:
    convert_to_fastq = "samtools fastq /home/amulford/mini_project/" + srr + "map.sam > /home/amulford/mini_project/" + srr + "map.fastq"
    os.system(convert_to_fastq)
  #ADD COUNTING AND PUT IN LOG FILE
    
    
    
def 05b_spades(SRR_list):
  run_spades = "spades -k 55,77,99,127 -t 2 --only-assembler -s " + SRR_list[0] + "map.fastq -s " + SRR_list[1] + "map.fastq -s " + SRR_list[2] + "map.fastq -s " + SRR_list[3] + "map.fastq -o /spades/"
  os.system(run_spades)
  log_file = open("miniProject.log", "w") #write to file
  log_file.write(run_spades)
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


  ###############################################################

SRR_list = ["SRR5660030", "SRR5660033", "SRR5660044", "SRR5660045"]

02a_EF99921_fasta()
02b_kallisto()
03a_kallisto(SRR_list)
03b_sleuth()
04a_bowtie2(SRR_list)
04b_and_05a_convert_to_fastq_and_count(SRR_list)

os.system(mkdir spades)

05b_spades()
06_subset_contigs()
07_assembly_length()
08_concatenate_contigs()
09_blast()



