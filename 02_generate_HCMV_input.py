from Bio import Entrez
from Bio.Seq import Seq
from Bio import SeqIO

Entrez.email = "amulford@luc.edu"
handle = Entrez.efetch(db="nucleotide", id="EF999921", rettype="gb")
records = list(SeqIO.parse(handle, "gb"))

rec = records[0]

count = 0

file = open("miniProject.log", "w") #write to file

file2 = open("HCMV_reads.fasta","w")

for feature in rec.features:
    if feature.type == "CDS":
        count = count+1
        seq1 = feature.location.extract(rec).seq
        file2.write("@" + str(count))
        file2.write(str(seq1) + "\n")


file.write("The HCMV genome (EF99921) has " + str(count) + " CDS." + "\n")    
file.close() #close file
