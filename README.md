# influenza_codon_usage
Data and code for Smith et al., Avian Influenza Virus PB1 Gene in H3N2 Viruses Evolved in Humans To Reduce Interferon Inhibition by Skewing Codon Usage toward Interferon-Altered tRNA Pools, mBio 2018

# Sequences
This folder contains the sequences for the PB1 influenza constructs generated, as well as files containing the number of each codon used in each influenza isolate we analyzed.
The GISAID database does not allow sharing of sequences downloaded, so the acknowledgement tables for the GISAID sequences used are made available instead.
To run our analysis yourself, simply download the desired datasets from GISAID, and first run the script "prep-codoncounts.sh" on the fasta files. Following that, run the "codoncounts.py" on the output from "prep-codoncounts.sh" to generate a file containing the number of each codon used in each isolate of your chosen sequences.

# tRNA Sequencing
This folder contains the codon and anti-codon counts we determined for each tRNA sequencing library we prepared in .csv files. It also contains the aggregated codon counts based on isoaccepting tRNA availability.

# rtAI-CAI
This folder contains the analysis of the CAI and rtAI of influenza genes in R Markdown scripts. "allserofigures.Rmd" contains the scripts for all sequences we analyzed. "H3N2figures.Rmd" contains scripts for our more extensive analysis of the PB1 segment of H3N2.

# reshuffling test
This folder contains the R Markdown scripts required to carry out the reshuffling test described in manuscript. The reshuffling test requires positional sequence information, and so needs to have its' codon information presented in a different format. "tidyitup-individual-sites.py" will do this to a prepped .fasta file.
"reshuffle.Rmd" contains the scripts for the reshuffling test.

# growth curves
This folder contains data in .csv format on the growth curves performed. "growthcurves-figure.Rmd" contains the R Markdown scripts used to analyze and visualize the growth curves.

# RT-PCR
This folder contains the raw RT-PCR data in .csv format. "RT-PCR figures.Rmd" contains the R Markdown scripts used to analyze and visualize the RT-PCR data.
