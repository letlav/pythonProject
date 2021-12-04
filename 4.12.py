def olymp():
    _u=dict()
    k = 0
    while True:
        _s=input().split()
        if len(_s) == 0:
            break
        else:
            _u[_s[0]+ ' ' + _s[1]]=int(_s[2])
            k+=len(_u)
    return _u

count=int(input())
list=[0]*count
for i in range (count):
    list[i]=olymp()
    print(*list)
    print(k)
