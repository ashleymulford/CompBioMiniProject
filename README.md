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
