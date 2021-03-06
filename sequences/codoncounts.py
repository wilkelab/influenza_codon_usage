#!/usr/bin/python3

#ok, what I wanna do here is make a table showing: strain, serotype, year, years circulating, codon, number of that codon, number of that amino acid.
#Let's try it out!

import re
import sys

#shit, I gotta make these lower case?  Is there an easier way to do this??
#First, something like: tr --delete '\n' <allyears_unpassaged.fasta | sed -z 's/>/\n>/g' > allyears_unpassaged.fasta.fortidy

library = {  'gct' : ['Ala'],
	'gcc' : ['Ala'],
	'gca' : ['Ala'],
	'gcg' : ['Ala'],
	'cgt' : ['Arg'],
	'cgc' : ['Arg'],
	'cga' : ['Arg'],
	'cgg' : ['Arg'],
	'aga' : ['Arg'],
	'agg' : ['Arg'],
	'aat' : ['Asn'],
	'aac' : ['Asn'],
	'gat' : ['Asp'],
	'gac' : ['Asp'],
	'tgt' : ['Cys'],
	'tgc' : ['Cys'],
	'caa' : ['Gln'],
	'cag' : ['Gln'],
	'gaa' : ['Glu'],
	'gag' : ['Glu'],
	'ggt' : ['Gly'],
	'ggc' : ['Gly'],
	'gga' : ['Gly'],
	'ggg' : ['Gly'],
	'cat' : ['His'],
	'cac' : ['His'],
	'att' : ['Ile'],
	'atc' : ['Ile'],
	'ata' : ['Ile'],
	'tta' : ['Leu'],
	'ttg' : ['Leu'],
	'ctt' : ['Leu'],
	'ctc' : ['Leu'],
	'cta' : ['Leu'],
	'ctg' : ['Leu'],
	'aaa' : ['Lys'],
	'aag' : ['Lys'],
	'atg' : ['Met'],
	'ttt' : ['Phe'],
	'ttc' : ['Phe'],
	'cct' : ['Pro'],
	'ccc' : ['Pro'],
	'cca' : ['Pro'],
	'ccg' : ['Pro'],
	'tct' : ['Ser'],
	'tcc' : ['Ser'],
	'tca' : ['Ser'],
	'tcg' : ['Ser'],
	'agt' : ['Ser'],
	'agc' : ['Ser'],
	'act' : ['Thr'],
	'acc' : ['Thr'],
	'aca' : ['Thr'],
	'acg' : ['Thr'],
	'tgg' : ['Trp'],
	'tat' : ['Tyr'],
	'tac' : ['Tyr'],
	'gtt' : ['Val'],
	'gtc' : ['Val'],
	'gta' : ['Val'],
	'gtg' : ['Val'],
	'tga' : ['stop'],
	'tag' : ['stop'],
	'taa' : ['stop']}

def parse_Fasta(filename):
	fasta = open(filename).readlines()
	sequence = ''
	output = open(filename + '.codoncounts', 'a')
	output.write('strain	year	codon	numcodon	numaa\n')
	for n in fasta:
		namebegin = n.find('>')
		nameend = n.find('PB1')
		name = n[namebegin+1:nameend]
		#pull out the year!
		findyear = re.search('_\|_\d\d\d\d(_|-|@)', name)
		year = re.search('\d\d\d\d', findyear.group())
		codseq = list()
		aaseq = list()
		pos = n.find('atg')
		running = True
		while running:
			cod = n[pos:pos+3]
			if cod == 'tag':   
				codseq.append(cod)
				aaseq.append(library[cod][0])
				running = False
			elif cod == 'tga':         
				codseq.append(cod)
				aaseq.append(library[cod][0])
				running = False
			elif cod == 'taa':       
				codseq.append(cod)
				aaseq.append(library[cod][0])
				running = False
			elif len(cod) <= 2:
				running = False
			else:
				try:
					codseq.append(cod)
					aaseq.append(library[cod][0])
					pos += 3
				except KeyError:
					print(cod, 'ignoring codon with non-canonical base(s)')
					pos += 3
		if len(name) >= 1:
			for codon in library:
				output.write(name+'\t'+year.group()+'\t'+codon+'\t'+str(codseq.count(codon))+'\t'+str(aaseq.count(library[codon][0]))+'\n')
		else:
			None

				


if len(sys.argv) != 2:
    print('Please provide FASTA as infile as a command-line argument')

else:
    parse_Fasta(sys.argv[1])
