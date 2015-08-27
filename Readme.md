---
title: "Readme"
author: "Bart"
date: "August 27, 2015"
output: html_document
---

##Bart's Influenza codon project
.fa files contain sequences.  The format is kinda wonky, it is: 
>accession-strain-name|serotype|year|sequence

.tidy.csv files are tables where each codon is an observation. The columns are:
strain - the assesion number and strain name
sero - the serotype
year - the year the virus was isolated
coryear - the number of years the segment has been circulating in the human population (an estimate)
codon - the codon
numcodon - the number of the codon found in the sequence
numaa - the number of the amino acid coded for by the codon found in the sequence

codonvalues.csv is a table containint a number of values that apply to each possible codon.  The columns are:
codon - the codon we're looking at
aa - the amino acid the codon codes for
withIFN - the RSCU based off tRNA sequencing in the treatment with IFN
withIFNmax - the maximum RSCU for the amino acid the given codon codes for based off tRNA sequencing in the treatment with IFN
withIFNmin - the minimum RSCU for the amino acid the given codon codes for based off tRNA sequencing in the treatment with IFN
withIFNreads - the number of sequences mapped to a tRNA that recognizes the codon in the treatment with IFN
noIFN - the RSCU based off tRNA sequencing in the treatment with IFN
noIFNmax - the maximum RSCU for the amino acid the given codon codes for based off tRNA sequencing in the treatment with out IFN
noIFNmin - the minimum RSCU for the amino acid the given codon codes for based off tRNA sequencing in the treatment with out IFN
noIFNreads - the number of sequences mapped to a tRNA that recognizes the codon in the treatment without IFN
CAI - the RSCU based off the top 200 most highly expressed genes across multiple cell types as determined by ATLAS-EMBL database
CAImax - the maximum RSCU for the amino acid the given codon codes for based off the top 200 most highly expressed genes across multiple cell types as determined by ATLAS-EMBL database
CAImin - the minimum RSCU for the amino acid the given codon codes for based off the top 200 most highly expressed genes across multiple cell types as determined by ATLAS-EMBL database
GC - the GC content of the codon

construct_v_WT_change.csv is a table showing how the usage of each codon changed between WT Udorn and my constructs of PB1 that performs better in IFN treated cells
change_new - my more recent construct that nearly exactly reflects codon usage in modern viruses
change_con - my construct designed by altering the CAI of Udorn, but keeping the GC% constant

tidyitupv2.py is the python script used to convert the sequence files to the tables

individualcodons.Rmd is the R script I've been working on.  