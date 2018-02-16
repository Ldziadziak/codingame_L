import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
n = int(raw_input())  # the number of temperatures to analyse
temps = raw_input()  # the n temperatures expressed as integers ranging from -273 to 5526

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
ar = map(int, temps.split())
if n <> 0:
    a = 10001
else:
    a = 0
    
for i in range(0, n):
    if abs(ar[i]) < abs(a):
        a = ar[i]
    if ar[i] == abs(a):
        a = abs(ar[i])  
print a