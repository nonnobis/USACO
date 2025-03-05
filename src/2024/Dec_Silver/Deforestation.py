"""
ID: nonnobis
LANG: PYTHON3
TASK: Deforestation
"""
import bisect

#fin = open ('./test_data/2024_12/prob2_silver_dec24/11.in', 'r')

n_test = int(input()) 
#n_test = int(fin.readline())

for _ in range(n_test):
    n, k = map(int, input().split())

    trees = sorted(list(map(int, input().split())))

    restrict = []

    for i in range(k):
        l, r, t = list(map(int, input().split()))
        restrict.append((r,l,t))

    restrict = sorted(restrict)

    trees_in_range = 0

    plants = set()

    planted_tree = []

    for (r, l, t) in restrict:
        i_r = bisect.bisect_right(trees, r)
        i_l = bisect.bisect_left(trees, l)

        p_r = bisect.bisect_right(planted_tree, r)
        p_l = bisect.bisect_left(planted_tree, l)

        n_trees = i_r - i_l
        n_planted = p_r - p_l
        
        for i in range(i_r-1, i_l-1, -1):
            if t > n_planted:
                if trees[i] in plants:
                    continue
                
                idx = bisect.bisect_right(planted_tree, trees[i])
                planted_tree.insert(idx, trees[i])
                n_planted += 1
                plants.add(trees[i])
            else:
                break
                

    print( len(trees) - len(planted_tree) )
