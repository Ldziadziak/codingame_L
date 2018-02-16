# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

@n = gets.to_i
t = Array.new
inputs = gets.split(" ")
for i in 0..(@n-1)
    t << inputs[i].to_i
end

# Write an action using puts
# To debug: STDERR.puts "Debug messages..."
max, min = t[0], t[0]
dif = min - max

for k in 0..(@n-2) 
    if t[k] > t[k+1]
        max = t[k] if t[k]>max
        min = t[k]
        min = t[k+1] if t[k+1]<min    
     end

    if min-max < dif
        dif = min-max
    end
end

puts  dif