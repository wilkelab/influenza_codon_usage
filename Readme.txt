##Bart's Influenza codon project
.fa files contain sequences.  The format is kinda wonky, it is: 
>accession-strain-name|serotype|year|sequence

.fa.tidy files are tables where each codon is an observation. The columns are:
strain - the assesion number and strain name
sero - the serotype
year - the year the virus was isolated
coryear - the number of years the segment has been circulating in the human population (an estimate)
codon - the codon
numcodon - the number of the codon found in the sequence
numaa - the number of the amino acid coded for by the codon found in the sequence

tidyitup is the python script used to convert the sequence files to the tables

individualcodons.Rmd is the R script I've been working on
