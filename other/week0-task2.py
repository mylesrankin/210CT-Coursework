'''
by @mylesrankin (github)
Finds where a coord is in relation to a triangle by
using a for loop to check if up/down or left/right
are bigger than the other and a dictionary counter
'''

triangle = []
a = (3,4)
b = (0,5)
c = (6,9)
p = (-2,4)

triangle = [a,b,c]

dirs = {'left':0, 'right':0, 'up': 0, 'down': 0} # dictionary counter

for i in triangle: # checks each direction - cord vs triangle
    if p[0] < i[0]:
        dirs['left']+= 1
    else:
        dirs['right']+= 1
    if p[1] < i[1]:
        dirs['down']+= 1
    else:
        dirs['up']+= 1

print(dirs)
print(max(dirs, key=dirs.get)) # gets biggest counter (direction of coordinate)

