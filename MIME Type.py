import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(raw_input())  # Number of elements which make up the association table.
q = int(raw_input())  # Number Q of file names to be analyzed.
dictonary = {}
for i in xrange(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = raw_input().split()
    dictonary[ext.lower()] = mt
for i in xrange(q):
    fname = raw_input()  # One file name per line.
    if "." in fname:
        poz = fname.rfind(".")    
        ext = fname[poz+1::]
        if ext.lower() in dictonary:
            print dictonary[ext.lower()]
        else:
            print "UNKNOWN"

    else: 
        print "UNKNOWN"



        


# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.
