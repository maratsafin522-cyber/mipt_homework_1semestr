def to_dec(s,b):
    sign=1
    if s[0]=='-':
        sign=-1
        s=s[1:]

    n=0
    for x in s:
        n=n*b+int(x)

    return sign*n


def to_base(n,b):
    if n<0:
        return '-'+to_base(-n,b)

    if n<b:
        return str(n)

    return to_base(n//b,b)+str(n%b)


f=open('input.txt','r')
data=f.read().split()
f.close()

b=int(data[-1])
op=data[-2]
a=data[:-2]

for i in range(len(a)):
    a[i]=to_dec(a[i],b)

res=a[0]

for x in a[1:]:
    if op=='+':
        res+=x
    elif op=='-':
        res-=x
    elif op=='*':
        res*=x

f=open('output.txt','w')
f.write(to_base(res,b))
f.close()
