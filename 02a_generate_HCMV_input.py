#import biopython classes
from Bio import Entrez
from Bio.Seq import Seq
from Bio import SeqIO

Entrez.email = "amulford@luc.edu"
#get record for EF999921
handle = Entrez.efetch(db="nucleotide", id="EF999921", rettype="gb")
records = list(SeqIO.parse(handle, "gb"))

#list only has one item, the record
rec = records[0]
count = 0
file = open("project.log", "w") #write to file
file2 = open("EF999921_reads.fasta","w")

#pull out CDS reads
for feature in rec.features:
    if feature.type == "CDS":
        #count CDS reads
        count = count+1
        #get CDS and write to file
        seq1 = feature.location.extract(rec).seq
        file2.write(">HCMV" + str(count) + "\n")
        file2.write(str(seq1) + "\n")
        
#update log with CDS count
file.write("The HCMV genome (EF99921) has " + str(count) + " CDS." + "\n")    
file.close() #close file
file2.close()
