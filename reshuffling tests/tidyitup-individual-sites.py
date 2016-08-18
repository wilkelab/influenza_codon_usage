#!/usr/bin/python3

#ok, what I wanna do here is make a table showing: strain, serotype, year, years circulating, codon, number of that codon, number of that amino acid.
#Let's try it out!

import re
import sys

#shit, I gotta make these lower case?  Is there an easier way to do this??
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
	output = open(filename + '.individualcodoncounts', 'a')
	output.write('strain	position	year	codon\n')
	seqnum=0
	for n in fasta:
		seqnum+=1
		namebegin = n.find('>')
		nameend = n.find('_|_PB1')
		name = n[namebegin+1:nameend]
		#pull out the year!
		findyear = re.search('_\|_\d\d\d\d(_|-)', name)
		year = re.search('\d\d\d\d', findyear.group())
		pos = n.find('atg')
		running = True
		codpos=1
		check = 'what'
		while running:
			cod = n[pos:pos+3]
			if cod == 'tag':
				running = False
			elif cod == 'tga':
				running = False
			elif cod == 'taa':
				running = False
			elif len(cod) <= 2:
				running = False
			else:
				try:
					check == library[cod][0]
					output.write(str(seqnum)+'\t'+str(codpos)+'\t'+str(int(year.group())-1968)+'\t'+cod+'\n')
					pos += 3
					codpos+=1
				except KeyError:
					print(cod, 'Key Error, ignoring codons with non-canonical bases')
					pos += 3
					codpos+=1


				


if len(sys.argv) != 2:
    print('Please provide FASTA as infile as a command-line argument')

else:
    parse_Fasta(sys.argv[1])
