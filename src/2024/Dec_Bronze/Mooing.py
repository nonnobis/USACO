"""
ID: nonnobis
LANG: PYTHON3
TASK: Mooing Time
"""
import collections

#fin = open ('./test_data/2024_12/prob3_bronze_dec24/7.in', 'r')

#n, f = map(int, fin.readline().split())
#s = fin.readline()


n, f = map(int, input().split())
s = input()
list_s = list(s)
# 2, 7, 11, 12, 13

map = collections.defaultdict()
res = set()

def checkMoo(_str):
    if _str[0] != _str[1] and _str[1] == _str[2]:
        return True
    return False

def checkMooRange(i, adjust, reset):
    for j in range(max(i-2, 0), min(i+1, n-2)):

        _moo = ''.join(list_s[j:j+3])
        
        if checkMoo(_moo):
            map[_moo] = map.get(_moo, 0) + adjust

            if map[_moo] >= f:
                res.add(_moo)
            if reset:
                map[_moo] = map.get(_moo, 0) - adjust



for i in range(n-2):
    if checkMoo(s[i:i+3]):
        map[s[i:i+3]] = map.get(s[i:i+3], 0) + 1

for i in range(n):

    checkMooRange(i, -1, False)

    for c in 'abcdefghijklmnopqrstuvwxzy':
        list_s[i] = c
        checkMooRange(i, 1, True)
        list_s[i] = s[i]

    checkMooRange(i, 1, False)


res = sorted(res)

print(len(res))

for elem in res:
    print(elem)