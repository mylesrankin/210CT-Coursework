triangle = []
a = (3,4)
b = (0,5)
c = (6,9)
p = (-2,4)

triangle = [a,b,c]

dirs = {'left':0, 'right':0, 'up': 0, 'down': 0}

for i in triangle:
    if p[0] < i[0]:
        dirs['left']+= 1
    else:
        dirs['right']+= 1
    if p[1] < i[1]:
        dirs['down']+= 1
    else:
        dirs['up']+= 1

print(dirs)
print(max(dirs, key=dirs.get))

