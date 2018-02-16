# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
moc = Array.new
div = 1000
@n = gets.to_i
@n.times do
    pi = gets.to_i
    moc.push(pi)
end
moc.sort!
moc.length.times do |i|
    if i < moc.length-1
        if moc[i+1] - moc[i] < div
            div = moc[i+1] - moc[i]
        end
    end
end

# Write an action using puts
# To debug: STDERR.puts "Debug messages..."

puts div