STDOUT.sync = true # DO NOT REMOVE
# Don't let the machines win. You are humanity's last hope...

@width = gets.to_i # the number of cells on the X axis
@height = gets.to_i # the number of cells on the Y axis
mapa = Array.new (Array.new)
@height.times do    
     # width characters, each either 0 or .
    mapa <<  gets.chomp.split(//) 

end
#print mapa
@height.times do |h|
    @width.times do |w|
       if mapa[h][w] == "0"
           print w, " ", h

                for ww in w...(@width)
                    if ww+1 == @width
                        print " -1 -1"
                    else
                        if mapa[h][ww+1] == "0"
                            print " ", ww+1, " ", h
                            break
                        end
                    end
                end



                for hh in h...(@height)
                    if hh+1 == @height
                        print " -1 -1 \n" 
                    else
                        if mapa[hh+1][w] == "0"
                            print " ", w, " ", hh+1, "\n"
                            break
                        end
                    end
                 end 
        end             
    end
end

    

# Write an action using puts
# To debug: STDERR.puts "Debug messages..."

# Three coordinates: a node, its right neighbor, its bottom neighbor