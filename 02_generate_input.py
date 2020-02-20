from Bio import Entrez
from Bio.Seq import Seq
from Bio import SeqIO

Entrez.email = "amulford@luc.edu"
handle = Entrez.efetch(db="nucleotide", id="EF999921", rettype="fasta")
records = list(SeqIO.parse(handle, "fasta"))
print(records)
