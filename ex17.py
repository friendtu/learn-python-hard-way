from sys import argv
#from os.path import exists
#import os.path as path

#script, from_file, to_file=argv

#print "Copy %s to %s" % (from_file,to_file)

#fileIn=open(from_file,"r")
#dataIn=fileIn.read()

#print "The input file is %d bytes long" % len(dataIn)

#print "Does the output file exist? %r" % path.exists(to_file)
#print "Ready, hit RETURN to continue, CTRL-C to about."
#raw_input()

#fileOut=open(to_file,'w')
#fileOut.write(dataIn)


#print "Allright, all done."

#fileOut.close()
#fileIn.close()
open(argv[2],'w').write(open(argv[1]).read())