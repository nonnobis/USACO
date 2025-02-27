"""
ID: nonnobis
LANG: PYTHON3
TASK: Cake Game
"""
n_test = int(input()) 

for _ in range(n_test):
    n_cakes = int(input())
    
    cakes = list(map(int, input().split()))
    
    b_sum, e_sum = 0, 0

    if len(cakes) == 2:
        print( sum(cakes), 0 )
        continue

    e_ops = (n_cakes // 2) - 1

    tmp = cakes[-e_ops:]
    curr_sum = sum(tmp)
    curr_max = curr_sum

    tmp = tmp + cakes[:e_ops]

    for i in range(e_ops, len(tmp)):
        curr_sum -= tmp[i - e_ops]
        curr_sum += tmp[i]
        curr_max = max(curr_max, curr_sum)
    


    b_sum = sum(cakes) - curr_max
    e_sum = curr_max

    

    print(b_sum, e_sum)