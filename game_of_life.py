from pprint import pprint
height, width = 10, 10

grid =  [[0 for _ in range(width)]for _ in range (height)] # dead 
grid[2][2] = 1 # alive 
pprint(grid)