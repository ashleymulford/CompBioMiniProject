import os
from Bio import Entrez
from Bio.Seq import Seq
from Bio import SeqIO


def 02a_HCMV_fasta():
  Entrez.email = "amulford@luc.edu"
  handle = Entrez.efetch(db="nucleotide", id="EF999921", rettype="gb")
  records = list(SeqIO.parse(handle, "gb"))
  
  rec = records[0]
  count = 0
  log_file = open("/home/amulford/mini_project/miniProject.log", "w") #write to file
  fasta_file = open("/home/amulford/mini_project/EF999921_reads.fasta","w")

  for feature in rec.features:
    if feature.type == "CDS":
      count = count+1
      seq1 = feature.location.extract(rec).seq
      fasta_file.write(">HCMV" + str(count) + "\n")
      fasta_file.write(str(seq1) + "\n")

  log_file.write("The HCMV genome (EF99921) has " + str(count) + " CDS." + "\n")    
  log_file.close() #close file
  fasta_file.close()


def 02b_kallisto():
  run_index = "kallisto index -i hcmv_index.idx HCMV_reads.fasta"
  os.system(run_index)
  
  
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
  file = open("/home/amulford/mini_project/contigs.fasta")
  log_file = open("/home/amulford/mini_project/miniProject.log", "a")
  output_file = open("/home/amulford/mini_project/contigs_1000.fasta", "w")
  
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

  
def 07_assembly_length():
  file = open("/home/amulford/mini_project/contigs_1000.fasta")
  log_file = open("/home/amulford/mini_project/miniProject.log", "a")
  
  total_bps = 0
  
  #pull seqs out of file
  for contig in SeqIO.parse(file, "fasta"):
    length = len(contig.seq)
    total_bps = total_bps + length
      
  log_file.write("There are " + str(total_bps) + " bp in the assembly.\n")
  log_file.close()
  
def 08_concatenate_contigs():
  file = open("/home/amulford/mini_project/contigs_1000.fasta")
  output_file = open("/home/amulford/mini_project/blast_input.fasta", "w")
  
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
  
  
def 09_blast():





SRR_list = ["SRR5660030", "SRR5660033", "SRR5660044", "SRR5660045"]










