"""
ID: nonnobis
LANG: PYTHON3
TASK: Cheese Block
"""
#fin = open ('2.in', 'r')
#fout = open ('1.out', 'w')

#cnt_input = int(input()) 
n, cnt_input = map(int, input().split())

x_map, y_map, z_map = {}, {}, {}
res = 0

for _ in range(cnt_input):
    x,y,z = map(int, input().split())

    x_map[(y,z)] = x_map.get((y,z), 0) + 1
    y_map[(x,z)] = y_map.get((x,z), 0) + 1
    z_map[(x,y)] = z_map.get((x,y), 0) + 1

    if x_map[(y,z)] == n:
        res += 1
    
    if y_map[(x,z)] == n:
        res += 1
    
    if z_map[(x,y)] == n:
        res += 1
    
    print(res)


    