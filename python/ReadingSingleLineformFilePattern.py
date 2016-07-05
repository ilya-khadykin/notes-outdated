# Opening the file for reading
file = open(filename, 'r')

for line in file:
	# process the current line
	print(line)

# closing the file
file.close()