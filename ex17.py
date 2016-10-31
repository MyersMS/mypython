from sys import argv
from os.path import exists

script, from_filename, to_filename = argv

print "Copying from %s to %s" % (from_filename, to_filename)

in_file = open(from_filename)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_filename)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_filename, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()
