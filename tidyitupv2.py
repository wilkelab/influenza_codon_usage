#!/usr/bin/python3

#ok, what I wanna do here is make a table showing: strain, serotype, year, years circulating, codon, number of that codon, number of that amino acid.
#Let's try it out!

library = {  'GCT' : ['Ala'],
	'GCC' : ['Ala'],
	'GCA' : ['Ala'],
	'GCG' : ['Ala'],
	'CGT' : ['Arg'],
	'CGC' : ['Arg'],
	'CGA' : ['Arg'],
	'CGG' : ['Arg'],
	'AGA' : ['Arg'],
	'AGG' : ['Arg'],
	'AAT' : ['Asn'],
	'AAC' : ['Asn'],
	'GAT' : ['Asp'],
	'GAC' : ['Asp'],
	'TGT' : ['Cys'],
	'TGC' : ['Cys'],
	'CAA' : ['Gln'],
	'CAG' : ['Gln'],
	'GAA' : ['Glu'],
	'GAG' : ['Glu'],
	'GGT' : ['Gly'],
	'GGC' : ['Gly'],
	'GGA' : ['Gly'],
	'GGG' : ['Gly'],
	'CAT' : ['His'],
	'CAC' : ['His'],
	'ATT' : ['Ile'],
	'ATC' : ['Ile'],
	'ATA' : ['Ile'],
	'TTA' : ['Leu'],
	'TTG' : ['Leu'],
	'CTT' : ['Leu'],
	'CTC' : ['Leu'],
	'CTA' : ['Leu'],
	'CTG' : ['Leu'],
	'AAA' : ['Lys'],
	'AAG' : ['Lys'],
	'ATG' : ['Met'],
	'TTT' : ['Phe'],
	'TTC' : ['Phe'],
	'CCT' : ['Pro'],
	'CCC' : ['Pro'],
	'CCA' : ['Pro'],
	'CCG' : ['Pro'],
	'TCT' : ['Ser'],
	'TCC' : ['Ser'],
	'TCA' : ['Ser'],
	'TCG' : ['Ser'],
	'AGT' : ['Ser'],
	'AGC' : ['Ser'],
	'ACT' : ['Thr'],
	'ACC' : ['Thr'],
	'ACA' : ['Thr'],
	'ACG' : ['Thr'],
	'TGG' : ['Trp'],
	'TAT' : ['Tyr'],
	'TAC' : ['Tyr'],
	'GTT' : ['Val'],
	'GTC' : ['Val'],
	'GTA' : ['Val'],
	'GTG' : ['Val'],
	'TGA' : ['stop'],
	'TAG' : ['stop'],
	'TAA' : ['stop']}

def parse_Fasta():
	fasta = open(filename).readlines()
	sequence = ''
	output = open(filename + '.tidy', 'a')
	output.write('strain	sero	year	coryear	codon	numcodon	numaa\n')
	for n in fasta:
		namebegin = n.find('>')
		nameend = n.find('|')
		name = n[namebegin:nameend]
		sero = n[nameend+1:nameend+5]
		year = n[nameend+6:nameend+10]
		if sero == 'H3N2':
			coryear = str(int(year) + -1968)
		elif sero == 'H1N1':
			if int(year) < 1976:
				coryear = str(int(year) + -1933)
			elif int(year) >= 1976:
				coryear = str(int(year) + -1976)
		elif sero == 'H2N2':
			coryear = str(int(year) + -1957)
		else:
			coryear = 'NAN'
		codseq = list()
		aaseq = list()
		pos = n.find('ATG')
		running = True
		while running:
			cod = n[pos:pos+3]
			if cod == 'TAG':   
				codseq.append(cod)
				aaseq.append(library[cod][0])
				running = False
			elif cod == 'TGA':         
				codseq.append(cod)
				aaseq.append(library[cod][0])
				running = False
			elif cod == 'TAA':       
				codseq.append(cod)
				aaseq.append(library[cod][0])
				running = False
			else:
				try:
					codseq.append(cod)
					aaseq.append(library[cod][0])
					pos += 3
				except KeyError:
					if len(cod) < 3:
						print('NO STOP! RUNAWAY TRANSCRIPTION!')
						running = False
					else:
						print(name, cod, 'CRAPTASTIC CODON. GOOD JOB GUYS.') #should I remove these sequences?  Well, will remove outliers...
						pos += 3
				
		for codon in library:
			output.write(name+'\t'+sero+'\t'+year+'\t'+coryear+'\t'+codon+'\t'+str(codseq.count(codon))+'\t'+str(aaseq.count(library[codon][0]))+'\n')
				


filename = str(input('What file would you like to analyze? '))
parse_Fasta()
