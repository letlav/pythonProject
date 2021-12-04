def olymp():
    _u=dict()
    while True:
        _s = input().split()
        if len(_s) == 0:
            break
        else:
            _u[_s[0] + ' ' + _s[1]] = int(_s[2])
    return _u

count = int(input())
list = [0]*count
b=set()
for i in range (count):
    list[i] = olymp()
print(*list)

_set = set()
for i in range (count):
    for items in list[i].keys():
        _set = _set.add(items())
print(len(_set))


