# opening the file
file = open(filename, 'r')

# reading the first line of file before stepping into while loop
# the code below should vary from your file structure
firstLine = file.readline().strip()

while firstLine != '':
	# read the number of lines you want
	secondLine = file.readline().strip()
	thirdLine = file.readline().strip()
	# ...

	# process the lines you've read
	print(firstLine, secondLine, thirdLine)

	# update the condition statment
	firstLine = file.readline().strip()

# always close the file
file.close()
	