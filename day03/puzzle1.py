"""
--- Day 3: Spiral Memory ---
You come across an experimental new kind of memory stored on an infinite two-dimensional grid.

Each square on the grid is allocated in a spiral pattern starting at a location marked 1 and then
counting up while spiraling outward. For example, the first few squares are allocated like this:

17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...
While this is very space-efficient (no squares are skipped), requested data must be carried back
to square 1 (the location of the only access port for this memory system) by programs that can
only move up, down, left, or right. They always take the shortest path: the Manhattan Distance
between the location of the data and square 1.

For example:

Data from square 1 is carried 0 steps, since it's at the access port.
Data from square 12 is carried 3 steps, such as: down, left, left.
Data from square 23 is carried only 2 steps: up twice.
Data from square 1024 must be carried 31 steps.
How many steps are required to carry the data from the square identified in your puzzle input all
the way to the access port?

Your puzzle input is 347991.
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
value = 0
array = []
for value in range(1, ubound):
    # calculate direction
    if direction == 'right':
        x = x + 1  # make the move
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
print(x, y, value)
print(abs(x) + abs(y))

"""
output:
[Running] python "/home/toddl/projects/advent_of_code_2017/day03/puzzle1.py"
-185 295 347990
480

result from website:
That's the right answer! You are one gold star closer to debugging the printer. [Return to Day 3]
"""
