f=open('input.txt','r')
a=f.read().split()
f.close()

op=a[-1]
a=a[:-1]

res=int(a[0])

for x in a[1:]:
    if op=='+':
        res+=int(x)
    elif op=='-':
        res-=int(x)
    elif op=='*':
        res*=int(x)

f=open('output.txt','w')
f.write(str(res))
f.close()
