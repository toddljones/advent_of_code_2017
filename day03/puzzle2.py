"""
day 3 puzzle 2

--- Part Two ---
As a stress test on the system, the programs here clear the grid and then store the
value 1 in square 1. Then, in the same allocation order as shown above, they store the
sum of the values in all adjacent squares, including diagonals.

So, the first few squares' values are chosen as follows:

Square 1 starts with the value 1.
Square 2 has only one adjacent filled square (with value 1), so it also stores 1.
Square 3 has both of the above squares as neighbors and stores the sum of their values, 2.
Square 4 has all three of the aforementioned squares as neighbors and stores the sum of
their values, 4.
Square 5 only has the first and fourth squares as neighbors, so it gets the value 5.
Once a square is written, its value does not change. Therefore, the first few squares
would receive the following values:

147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...
What is the first value written that is larger than your puzzle input?

Your puzzle input is still 347991.

"""

ubound = 347991

# add the points into a vector array of x, y, value
x = 0
minx = 0
maxx = 0
y = 0
miny = 0
maxy = 0
direction = 'right'
value = 1
array = [0, 0, 1]  # seed the array with the first item
while value < ubound:
    # calculate direction
    if direction == 'right':
        x = x + 1  # make the positional move
        if x > maxx:  # if beyond min/max, change direction, reset min/max
            direction = 'up'
            maxx = x
    elif direction == 'up':
        y = y + 1
        if y > maxy:
            direction = 'left'
            maxy = y
    elif direction == 'left':
        x = x - 1
        if x < minx:
            direction = 'down'
            minx = x
    elif direction == 'down':
        y = y - 1
        if y < miny:
            direction = 'right'
            miny = y
    # calculate the value
        # filter the list to all items that are +/- 1 from the x and y
        # sum the values for the filtered set
        
print(x, y, value)
print(abs(x) + abs(y))
