# Convert Teams transcript text to CSV
infile_name = 'sample.txt'
outfile_name = 'sample_out.csv'

infile = open(infile_name, 'r', encoding='UTF-8')
inlist = infile.readlines()
infile.close()

outlist = []
i = 0
while i < len(inlist):
	outlist.append(inlist[i].rstrip('\n') + "," + inlist[i+1])
	i+=2
print(outlist)

# SJIS for Excel
outfile = open(outfile_name, 'w', encoding='SJIS')
outfile.writelines(outlist)
outfile.close()