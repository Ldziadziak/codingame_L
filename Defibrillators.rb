# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

@lon = gets.chomp
@lat = gets.chomp
@n = gets.to_i

arr = Array.new
dott = lambda {|x| x.sub! ",", "."}

@n.times do |i|
    arr << gets.chomp.split(";")
    [arr[i][4], arr[i][5]].each(&dott)
end

[@lon, @lat].each(&dott)

dist = 1000.0
poz = 0
d = 0.0
for i in 0..(@n-1)
    x = (arr[i][4].to_f - @lon.to_f) * Math.cos(((@lat.to_f + arr[i][5].to_f))/2.0) 
    y = (arr[i][5].to_f - @lat.to_f)
    d = (Math.sqrt((x**2)+(y**2)))*6371
    if dist > d
        dist = d
        poz = i
    end
end




# Write an action using puts
# To debug: STDERR.puts "Debug messages..."

puts arr[poz][1]