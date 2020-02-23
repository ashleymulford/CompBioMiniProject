# CompBioMiniProject

This repo contains a python pipeline that takes sra input reads from the virus family Herpesviridae to produce an assembly which is then blasted.

## Languages Requirements: 
Python with the libraries os, Entrez and SeqIO (from Bio), and Seq (from Bio.Seq)
R with the packages dplyr and sleuth

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
