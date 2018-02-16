import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = raw_input()

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
m_to_bin = ""
output = ""
for i in message:
    bits = bin(ord(i))[2::]
    if len(bits) < 7:
        for i in range(0,(7 - len(bits))):
            bits = "0"+bits
            
    m_to_bin += bits

for k in range(0, len (m_to_bin)):
    if m_to_bin[k] == "1":
        if k == 0:
            output += "0 0"
        else:
            if m_to_bin[k-1] == "1":
                output += "0"
            else:
                output += " 0 0"
    else:
        if k == 0:
            output += "00 0"
        else:
            if m_to_bin[k-1] == "0":
                output += "0"
            else:
                output += " 00 0"           



print output