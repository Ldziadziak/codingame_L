import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in raw_input().split()]

x1 = light_x 
x2 = initial_tx
    
y1 = light_y 
y2 = initial_ty
# game loop
while True:
    remaining_turns = int(raw_input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."

    
    if y1 == y2:
        if x1 > x2:
            r = "E"
            x2 += 1
        if x1 < x2:
            r = "W"
            x2 -= 1
            
    if x1 == x2:
        if y1 > y2:
            r = "S"
            y2 += 1
        if y1 < y2:
            r = "N"
            y2 -= 1
    
    if y1 <> y2 and x1 <> x2:
        if x1 > x2 and y1 > y2:
            r = "SE"
            x2 += 1
            y2 += 1
        if x1 < x2 and y1 > y2:
            r = "SW"
            x2 -= 1
            y2 += 1
        if x1 > x2 and y1 < y2:
            r = "NE"
            x2 += 1
            y2 -= 1
        if x1 < x2 and y1 < y2:
            r = "NW"
            x2 -= 1
            y2 -= 1
            

    # A single line providing the move to be made: N NE E SE S SW W or NW
	
    print r