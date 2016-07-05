import argparse

parser = argparse.ArgumentParser(description='This is a description of')
parser.add_argument('-size', type=str, help='This line should give a short help message', required=True)
parser.add_argument('-o', type=str, help='This line gives the user a description of the argument', required=False)

# saving passed arguments to a variable
args = parser.parse_args()
print(type(args))

# access the parameter based on the flag as property
first_arg = args.size
print('Argument -size: ' + first_arg)
second_arg = args.o
print('Argument -o: ' + second_arg)

'''
Usage:

> python ParsingArgumentsFromCommandLine.py -h
usage: ParsingArgumentsFromCommandLine.py [-h] -size SIZE [-o O]

This is a description of

optional arguments:
  -h, --help  show this help message and exit
  -size SIZE  This line should give a short help message
  -o O        This line gives the user a description of the argument

Output:

> python ParsingArgumentsFromCommandLine.py -size 100 -o test
<class 'argparse.Namespace'>
Argument -i: 100
Argument -o: test
'''