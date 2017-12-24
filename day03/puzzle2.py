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


# imports
from functools import reduce

ubound = 347991
# ubound = 806

# add the points into a vector array of x, y, value
x = 0
minx = 0
maxx = 0
y = 0
miny = 0
maxy = 0
direction = 'right'
value = 1
box_array = [[0, 0, 1]]  # seed the array with the first item
while value <= ubound:
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
    value = 0
    # print('x=', x)
    # print('y=', y)
    sublist = list(filter(lambda b: (abs(b[0]-x) <= 1 and abs(b[1]-y) <= 1), box_array))
    # print('filtered list=', sublist)
    for item in sublist:
        value = value + item[2]
    box_array.append([x, y, value])
    # print('new output=', box_array)
    # input('press enter to continue')
print(box_array)

"""
output:
[Running] python "/home/toddl/projects/advent_of_code_2017/day03/puzzle2.py"
[[0, 0, 1], [1, 0, 1], [1, 1, 2], [0, 1, 4], [-1, 1, 5], [-1, 0, 10], [-1, -1, 11], [0, -1, 23], [1, -1, 25], [2, -1, 26], [2, 0, 54], [2, 1, 57], [2, 2, 59], [1, 2, 122], [0, 2, 133], [-1, 2, 142], [-2, 2, 147], [-2, 1, 304], [-2, 0, 330], [-2, -1, 351], [-2, -2, 362], [-1, -2, 747], [0, -2, 806], [1, -2, 880], [2, -2, 931], [3, -2, 957], [3, -1, 1968], [3, 0, 2105], [3, 1, 2275], [3, 2, 2391], [3, 3, 2450], [2, 3, 5022], [1, 3, 5336], [0, 3, 5733], [-1, 3, 6155], [-2, 3, 6444], [-3, 3, 6591], [-3, 2, 13486], [-3, 1, 14267], [-3, 0, 15252], [-3, -1, 16295], [-3, -2, 17008], [-3, -3, 17370], [-2, -3, 35487], [-1, -3, 37402], [0, -3, 39835], [1, -3, 42452], [2, -3, 45220], [3, -3, 47108], [4, -3, 48065], [4, -2, 98098], [4, -1, 103128], [4, 0, 109476], [4, 1, 116247], [4, 2, 123363], [4, 3, 128204], [4, 4, 130654], [3, 4, 266330], [2, 4, 279138], [1, 4, 295229], [0, 4, 312453], [-1, 4, 330785], [-2, 4, 349975]]

the answer is: 349975

That's the right answer! You are one gold star closer to debugging the printer.

"""