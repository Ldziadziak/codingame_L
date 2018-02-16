STDOUT.sync = true # DO NOT REMOVE
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
@w, @h = gets.split(" ").collect {|x| x.to_i}
@n = gets.to_i # maximum number of turns before game over.
x, y = gets.split(" ").collect {|x| x.to_i}

# game loop
xmax = @w
xmin = 0
ymax = @h
ymin = 0

loop do
    bomb_dir = gets.chomp # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    
    # Write an action using puts
    # To debug: STDERR.puts "Debug messages..."
    if bomb_dir.include? "R"
        xmin = x
    end
    
    if bomb_dir.include? "L"
        xmax = x
    end
    
    if bomb_dir.include? "U"
        ymax = y
    end
    
    if bomb_dir.include? "D"
        ymin = y
    end
      
        y = (ymax +ymin)/2.0          
        x = (xmax +xmin)/2.0       
   
    print x.to_i, " ", y.to_i, "\n"
        
    # the location of the next window Batman should jump to.

end