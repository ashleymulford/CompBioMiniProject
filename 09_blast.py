from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

#open files
input_file = open("blast_input.fasta").read()
log_file = open("project.log", "a")

#blast
result_handle = NCBIWWW.qblast("blastn", "nr", input_file, entrez_query = "herpes")
#obtain record
blast_record = NCBIXML.read(result_handle)
#write column names to log
log_file.write("seq_title" + "\t" + "align_len" + "\t" + "number_HSPs" + "\t" + "topHSP_ident" + "\t" + "topHSP_gaps" + "\t" + "topHSP_bits" + "\t" + "topHSP_expect\n")

#go through top ten alignments and get desired info
for alignment in (list(blast_record.alignments)[:10]):
    log_file.write(alignment.title + "\t") #get title
    log_file.write(str(alignment.length) + "\t") #get length
    count_hsp = 0
    #count hsps
    for hsp in alignment.hsps:
        count_hsp = count_hsp+1
    log_file.write(str(count_hsp)+"\t")
    #get desired info for top hsp
    for hsp in alignment.hsps:
        log_file.write(str(hsp.identities) + "\t") #get identities
        log_file.write(str(hsp.gaps) + "\t") #get gaps
        log_file.write(str(hsp.bits) + "\t") #get bits
        log_file.write(str(hsp.expect) + "\n") #get expect
        break

log_file.close() #close file
