#!/bin/bash


tr --delete '\n\r' < ./gisaid_H3N2_PB1.fasta | sed -z 's/>/\n>/g' | sed '/./,$!d' > ./H3N2PB1.fasta
tr --delete '\n\r' < ./gisaid_H2N2_PB1.fasta | sed -z 's/>/\n>/g' | sed '/./,$!d' > ./H2N2PB1.fasta
tr --delete '\n\r' < ./gisaid_H1N1_PB1.fasta | sed -z 's/>/\n>/g' | sed '/./,$!d' > ./H1N1PB1.fasta


./codoncounts.py ./H3N2PB1.fasta
./codoncounts.py ./H2N2PB1.fasta
./codoncounts.py ./H1N1PB1.fasta
