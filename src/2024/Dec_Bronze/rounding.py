"""
ID: nonnobis
LANG: PYTHON3
TASK: Roundabout Rounding
"""
#fin = open ('./test_data/2024_12/prob1_bronze_dec24/13.in', 'r')
#int(fin.readline())
cnt_input = int(input()) 

# Use preset to reduce calculation
_min = [0, 45, 445, 4445, 44445, 444445, 4444445, 44444445, 444444445, 4444444445]
_max = [0, 49, 499, 4999, 49999, 499999, 4999999, 49999999, 499999999, 4999999999]

for _ in range(cnt_input):
    val = int(input())

    # find digit
    d = 0
    for digit in range(9):
        if val >= 10 ** digit:
            d = digit + 1
        else:
            break
    
    res = 0
    for i in range(d):
        if i >= 1 and i < 9:

            if val >= _min[i] and val <= _max[i]:
                res += min(_max[i], val) - _min[i] + 1
            elif val > _max[i]:
                res += (_max[i] - _min[i] + 1)

    print(res)


    