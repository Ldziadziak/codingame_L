import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(raw_input())
h = int(raw_input())
t = raw_input()
output = []
for i in xrange(h):
    output.append(raw_input())

tt=""   
d = 0
for i in range(0, len(t)):
    d = "ABCDEFGHIJKLMNOPQRSTUVWXYZ?abcdefghijklmnopqrstuvwxyz".find(t[i])
    if d == -1:
        tt+="?"
    else:
        tt+=t[i]        
    
slowo = tt.upper()
druk = []
for j in range(0, h):
    for k in range(0, len(slowo)):
        poz = "ABCDEFGHIJKLMNOPQRSTUVWXYZ?".find(slowo[k])
        if len(druk) <= j:
            druk.append('')
        druk[j] += output[j][poz*l:(poz*l)+(l)]
            
for n in range(0, h):
    print druk[n]
            
            
#for j in range(0, h):
#    for k in range(0, len(slowo)):
#        poz = "ABCDEFGHIJKLMNOPQRSTUVWXYZ?".find(slowo[k]) 
#        print output[j][poz*l:(poz*l)+(l)],
#    print \n
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."