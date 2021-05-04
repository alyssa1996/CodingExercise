v = []
for _ in range(3):
    x, y = map(int, input().split())
    v.append([x, y])

tx, ty = 0, 0
x = set()
y = set()
    
for loc in v:
    x.add(loc[0])
    y.add(loc[1])
    
for x_loc in x:
    for y_loc in y:
        if not [x_loc, y_loc] in v:
            tx, ty = x_loc, y_loc
            break

print(tx, ty)
