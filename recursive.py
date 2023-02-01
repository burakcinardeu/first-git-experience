x = 0
previous = 0
current = 1
while x<10:
    
    new = current + previous
    print(new)
    previous = current
    current = new
    x = x+1
print(new)

