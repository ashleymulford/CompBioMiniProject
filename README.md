# CompBioMiniProject

This repo contains a python pipeline that takes sra input reads from the virus family Herpesviridae to produce an assembly which is then blasted.

## Languages Requirements: 
- Python3 https://www.python.org/downloads/
    - os https://docs.python.org/2/library/os.html
    - Biopython https://biopython.org/wiki/Download

- R https://cran.r-project.org/bin/windows/base/
    - install.packages(dplyr)
    - install.packages(sleuth)

## Software Requirements: 
kallisto 
bowtie2 
SPAdes

## How to run:
Clone this repository to your working directory:

    git clone https://github.com/ashleymulford/CompBioMiniProject
    
Netx, move into this directory:
     
    cd CompBioMiniProject/
     
Run wrapper script:

    python3 wrapper.py 
