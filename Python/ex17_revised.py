from sys import argv
from os.path import exists

script, from_file, to_file = argv


#indata is assigned, open from_file, and then read it
indata = open(from_file).read()

#outfile is opening tofile in writing mode, then writing what is within indata to it
out_file = open(to_file, 'w'); out_file.write(indata)

#This is a simplified program which does everything 