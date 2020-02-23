from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

input = open("/home/amulford/mini_project/blast_input.fasta").read()

log_file = open("/home/amulford/mini_project/miniProject.log", "a")

result_handle = NCBIWWW.qblast("blastn", "nr", input, entrez_query="taxid[10292]")

blast_record = NCBIXML.read(result_handle)

log_file.write("seq_title" + "\t" + "align_len" + "\t" + "number_HSPs" + "\t" + "topHSP_ident" + "\t" + "topHSP_gaps" + "\t" + "topHSP_bits" + "\t" + "topHSP_expect\n")

for alignment in (list(blast_record.alignments)[:10]):
    log_file.write(alignment.title + "\t")
    log_file.write(str(alignment.length) + "\t")
    count_hsp = 0
    for hsp in alignment.hsps:
        count_hsp = count_hsp+1
    log_file.write(str(count_hsp)+"\t")
    for hsp in (list(alignment.hsp)[0]):
        log_file.write(hsp.identities + "\t")
        log_file.write(hsp.gaps + "\t")
        log_file.write(hsp.bits + "\t")
        log_file.write(hsp.expect + "\n")

log_file.close()
