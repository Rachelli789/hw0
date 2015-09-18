import csv 
f = open('iowa-liquor-sample.csv')
reader = csv.reader(f)
i = 0
for row in reader: 
	c = str.lower(row[11])
	if c == 'single malt scotch':
		i = i + 1
print '# of single malt scotches is ' + str(i)
