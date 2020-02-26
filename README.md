# CompBioMiniProject

This repo contains a python pipeline that takes sra input reads from the virus family Herpesviridae to produce an assembly which is then blasted.

## Languages Requirements: 
- Python3 https://www.python.org/downloads/
- with libraries:
    - os https://docs.python.org/2/library/os.html
    - Biopython https://biopython.org/wiki/Download

- R https://cran.r-project.org/bin/windows/base/
- with libraries:
    - dplyr, download with: install.packages(dplyr)
    - sleuth, download with: install.packages(sleuth)

## Software Requirements: 
- fastq dump https://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?view=toolkit_doc&f=fastq-dump
- kallisto https://pachterlab.github.io/kallisto/download
- bowtie2 http://bowtie-bio.sourceforge.net/bowtie2/manual.shtml
- SPAdes http://cab.spbu.ru/software/spades/

## How to run:
Clone this repository to your working directory:

    git clone https://github.com/ashleymulford/CompBioMiniProject
    
Next, move into this directory:
     
    cd CompBioMiniProject/
    
### Run wrapper script from the CompBioMiniProject directory:
- required arguments: --SRRlist

To run with test data:
    
    python3 wrapper.py --SRRlist SRR5660030 SRR5660033 SRR5660044 SRR5660045

## Important Output files/directories:
- project.log: 
    - contains all the output from the wrapper script, including counts of CDS, reads, and contigs and different points, signifcant results from Sleuth filtered by FDR<0.05, and 10 top hits from BLASTn
- blast_input.fasta: 
    - contains assembled sequence, input for BLASTn
- kallisto_results (dir): 
    - contains results from quantifying the TPM of each CDS in each transcriptome with kallisto
- spades (dir): 
    - contains all results from SPAdes; results file used in wrapper is contigs.fasta
- additional intermediary files such as indices, .sam files and other .fasta files are generated but do not contain results.
