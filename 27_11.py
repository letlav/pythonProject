_m=dict()
_p=dict()
_i=dict()
k1=0
k2=0
k3=0
while True:
    _s=input().split()
    if _s=='':
        break
    else:
        _m[_s[0]+ ' ' + _s[1]]=int(_s[2])
        k1+=1
        print(k1,'_',_s[0][0],'_',len(_s[1]), _s[0],_s[1], end=' ')
while True:
    _s=input().split()
    if _s=='':
        break
    else:
        _i[_s[0]+ ' ' + _s[1]]=int(_s[2])
        k2+=1
while True:
    _s = input().split()
    if _s=='':
         break
    else:
         _p[_s[0] + ' ' + _s[1]] = int(_s[2])
         k3+=1